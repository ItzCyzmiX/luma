from typing import TYPE_CHECKING

from luma.core.error import Luma_Error
from luma.sdl.mixer import C_TRACK_STOP_CALLBACK

if TYPE_CHECKING:
    from luma.core.engine import Luma


class Luma_AudioManager:
    AUDIO_DEVICE_DEFAULT_PLAYBACK = 0xFFFFFFFF

    def __init__(self, engine: "Luma"):
        self.engine = engine
        self._sounds: list[Luma_Sound] = []

        if not self.sdl_mixer.mix_init():
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self._mixer = self.sdl_mixer.create_mixer(
            Luma_AudioManager.AUDIO_DEVICE_DEFAULT_PLAYBACK, None
        )

        if not self._mixer:
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

    def loadSound(self, path: str):
        s = Luma_Sound(self, path)
        self._sounds.append(s)
        return s

    @property
    def sdl(self):
        return self.engine.sdl

    @property
    def sdl_mixer(self):
        return self.engine.sdl_mixer

    def _cleanup(self):
        for sound in self._sounds:
            sound.kill()
        self._sounds.clear()

        if self._mixer:
            self.sdl_mixer.destroy_mixer(self._mixer)
            self._mixer = None

        self.sdl_mixer.mix_quit()


class Luma_Sound:
    def __init__(self, audio_manager: Luma_AudioManager, path: str):
        self._path = path
        self._audio_manager = audio_manager
        self._track = self.sdl_mixer.create_track(self._audio_manager._mixer)

        if not self._track:
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self._audio = None
        self._gain: float = 1.0
        self._position: int = 0
        self.loop = False
        self.paused = False
        self.playing = False
        self.is_killed = False

        self._track_finish_callback = C_TRACK_STOP_CALLBACK(
            self._on_track_finish_callback
        )
        self.sdl_mixer.set_track_stopped_callback(
            self._track, self._track_finish_callback, None
        )

        self._load_sound()

    def _on_track_finish_callback(self, data: None, track: int):
        if self.is_killed or track != self._track:
            return

        self.playing = False
        self.paused = False
        self.position = 0

        if self.loop:
            self.play()
        else:
            if not self._is_cleaning_up:
                self.on_finish()

    def on_finish(self):
        pass

    def _load_sound(self):
        if not self._track or self.is_killed:
            return

        self.stop()

        if self._audio:
            self.sdl_mixer.destroy_audio(self._audio)
            self._audio = None

        self._audio = self.sdl_mixer.load_audio(
            self._audio_manager._mixer, self._path.encode(), True
        )

        if not self._audio:
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        if not self.sdl_mixer.set_track_audio(self._track, self._audio):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

    def pause(self):
        if (
            self.is_killed
            or not self._track
            or not self._audio
            or not self.playing
            or self.paused
        ):
            return

        if not self.sdl_mixer.pause_track(self._track):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self.paused = True
        self.playing = False

    def _resume(self):
        if (
            self.is_killed
            or not self._track
            or not self._audio
            or self.playing
            or not self.paused
        ):
            return

        if not self.sdl_mixer.resume_track(self._track):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self.paused = False
        self.playing = True

    def play(self):
        if self.is_killed or not self._audio or not self._track:
            return

        if self.paused:
            self._resume()
            return

        if not self.sdl_mixer.play_track(self._track, 0):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self.playing = True
        self.paused = False

    def stop(self):
        if self.is_killed or not self._audio or not self._track:
            return

        if not self.sdl_mixer.stop_track(self._track, 0):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self.playing, self.paused, self.position = False, False, 0

    @property
    def duration(self):
        if not self._audio or not self._track:
            return 0

        return max(
            self.sdl_mixer.trackframes_to_ms(
                self._track, self.sdl_mixer.get_audio_duration(self._audio)
            ),
            0,
        )

    @property
    def volume(self):
        return self._gain

    @volume.setter
    def volume(self, new_volume: float):
        if not self.sdl_mixer or not self._track:
            return
        new_volume = max(float(new_volume), 0.0)
        if not self.sdl_mixer.set_track_gain(self._track, new_volume):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self._gain = new_volume

    @property
    def position(self):
        if not self._track or not self._audio:
            return -1

        self._position = int(
            self.sdl_mixer.trackframes_to_ms(
                self._track, self.sdl_mixer.get_track_playback_position(self._track)
            )
        )

        return max(self._position, 0)

    @position.setter
    def position(self, pos: int):
        if not self._track or not self._audio:
            return

        duration = self.duration

        clamped_pos = max(0, min(int(pos), duration))

        trackframes = self.sdl_mixer.ms_to_trackframes(self._track, clamped_pos)

        if trackframes == -1:
            return

        if not self.sdl_mixer.set_track_playback_position(self._track, trackframes):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self._position = clamped_pos

    @property
    def sdl_mixer(self):
        return self._audio_manager.sdl_mixer

    @property
    def sdl(self):
        return self._audio_manager.engine.sdl

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path: str):
        if self._path == new_path:
            return

        self._path = new_path

        self._load_sound()

    def kill(self):
        if self.is_killed and not self._audio and not self._track:
            return

        self._is_cleaning_up = True

        self.stop()

        if self._audio:
            self.sdl_mixer.destroy_audio(self._audio)
            self._audio = None

        if self._track:
            self.sdl_mixer.destroy_track(self._track)
            self._track = None

        self.is_killed = True
        self.playing = False
        self.paused = False

    def isKilled(self):
        return self.is_killed
