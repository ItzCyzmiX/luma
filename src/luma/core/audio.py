import ctypes
from typing import TYPE_CHECKING

from luma.core.error import Luma_Error

if TYPE_CHECKING:
    from luma.core.engine import Luma


class Luma_AudioManager:
    AUDIO_DEVICE_DEFAULT_PLAYBACK = 0xFFFFFFFF

    def __init__(self, engine: "Luma"):
        self.engine = engine

        if not self.sdl_mixer.mix_init():
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self._mixer = self.sdl_mixer.create_mixer(
            Luma_AudioManager.AUDIO_DEVICE_DEFAULT_PLAYBACK, None
        )

        # self._sounds_track = self.sdl_mixer.create_track(self._mixer)
        # self._music_track = self.sdl_mixer.create_track(self._mixer)

        # if not self._music_track or not self._sounds_track:
        #     msg = self.sdl.get_error()
        #     raise Luma_Error(msg)

    def loadSound(self, path: str):
        return Luma_Sound(self, path)

    @property
    def sdl(self):
        return self.engine.sdl

    @property
    def sdl_mixer(self):
        return self.engine.sdl_mixer

    def _cleanup(self):

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
        self._load_sound()
        self.loop = False
        self.paused = False
        self.playing = False

    def _load_sound(self):
        self._audio = self.sdl_mixer.load_audio(
            self._audio_manager._mixer, self._path.encode(), True
        )

        if not self._audio:
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

    def pause(self):
        if not self._track or self.paused:
            return

        self.sdl_mixer.pause_track(self._track)
        self.paused = True
        self.playing = False

    def resume(self):
        if not self._track or not self.paused:
            return

        self.sdl_mixer.resume_track(self._track)
        self.paused = False
        self.playing = True

    def play(self):
        if not self._audio or not self._track or self.playing:
            return

        self.playing = True

        if not self.sdl_mixer.set_track_audio(self._track, self._audio):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        if not self.sdl_mixer.play_track(self._track, 0):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

    def rewind(self):
        if not self._audio or not self._track:
            return

        self.position = 0

 
    @property
    def position(self):
        if not self._track:
            return -1

        return int(
            self.sdl_mixer.trackframes_to_ms(
                self._track, self.sdl_mixer.get_track_playback_position(self._track)
            )
        )

    @position.setter
    def position(self, pos: int):
        if not self._track:
            return

        trackframes = self.sdl_mixer.ms_to_trackframes(self._track, pos)
        if trackframes == -1:
            return

        if not self.sdl_mixer.set_track_playback_position(self._track, trackframes):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

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
