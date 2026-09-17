import ctypes

from luma.sdl.bindings import NativeBindings


class SDL_AudioSpec(ctypes.Structure):
    _fields_ = [
        ("format", ctypes.c_uint32),
        ("channels", ctypes.c_int),
        ("freq", ctypes.c_int),
    ]


C_TRACK_STOP_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)


class SDLMixerBindings(NativeBindings):
    def __init__(self, library: ctypes.CDLL):
        super().__init__(library)

        self.mix_init = self.bind("MIX_Init", [], ctypes.c_bool)
        self.mix_quit = self.bind("MIX_Quit", [], None)

        self.create_mixer = self.bind(
            "MIX_CreateMixerDevice",
            [ctypes.c_uint32, ctypes.POINTER(SDL_AudioSpec)],
            ctypes.c_void_p,
        )

        self.destroy_mixer = self.bind("MIX_DestroyMixer", [ctypes.c_void_p], None)

        self.create_track = self.bind(
            "MIX_CreateTrack", [ctypes.c_void_p], ctypes.c_void_p
        )

        self.load_audio = self.bind(
            "MIX_LoadAudio",
            [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool],
            ctypes.c_void_p,
        )

        self.get_audio_duration = self.bind(
            "MIX_GetAudioDuration", [ctypes.c_void_p], ctypes.c_int64
        )

        self.set_track_audio = self.bind(
            "MIX_SetTrackAudio", [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_bool
        )

        self.set_track_gain = self.bind(
            "MIX_SetTrackGain", [ctypes.c_void_p, ctypes.c_float], ctypes.c_bool
        )

        self.destroy_audio = self.bind("MIX_DestroyAudio", [ctypes.c_void_p], None)

        self.play_track = self.bind(
            "MIX_PlayTrack", [ctypes.c_void_p, ctypes.c_uint32], ctypes.c_bool
        )

        self.destroy_track = self.bind("MIX_DestroyTrack", [ctypes.c_void_p], None)

        self.pause_track = self.bind("MIX_PauseTrack", [ctypes.c_void_p], ctypes.c_bool)

        self.resume_track = self.bind(
            "MIX_ResumeTrack", [ctypes.c_void_p], ctypes.c_bool
        )

        self.stop_track = self.bind(
            "MIX_StopTrack", [ctypes.c_void_p, ctypes.c_int64], ctypes.c_bool
        )

        self.set_track_stopped_callback = self.bind(
            "MIX_SetTrackStoppedCallback",
            [ctypes.c_void_p, C_TRACK_STOP_CALLBACK, ctypes.c_void_p],
            ctypes.c_bool,
        )

        self.set_track_loop = self.bind(
            "MIX_SetTrackLoops", [ctypes.c_void_p, ctypes.c_int], ctypes.c_bool
        )

        self.trackframes_to_ms = self.bind(
            "MIX_TrackFramesToMS", [ctypes.c_void_p, ctypes.c_int64], ctypes.c_int64
        )

        self.ms_to_trackframes = self.bind(
            "MIX_TrackMSToFrames", [ctypes.c_void_p, ctypes.c_int64], ctypes.c_int64
        )

        self.get_track_playback_position = self.bind(
            "MIX_GetTrackPlaybackPosition", [ctypes.c_void_p], ctypes.c_int64
        )

        self.set_track_playback_position = self.bind(
            "MIX_SetTrackPlaybackPosition",
            [ctypes.c_void_p, ctypes.c_int64],
            ctypes.c_bool,
        )
