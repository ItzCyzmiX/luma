import ctypes

from luma.sdl.bindings import NativeBindings


class SDL_AudioSpec(ctypes.Structure):
    _fields_ = [
        ("format", ctypes.c_uint32),
        ("channels", ctypes.c_int),
        ("freq", ctypes.c_int),
    ]


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

        self.create_track = self.bind(
            "MIX_CreateTrack", [ctypes.c_void_p], ctypes.c_void_p
        )

        self.load_audio = self.bind(
            "MIX_LoadAudio",
            [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool],
            ctypes.c_void_p,
        )

        self.set_track_audio = self.bind(
            "MIX_SetTrackAudio", [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_bool
        )

        self.play_track = self.bind(
            "MIX_PlayTrack", [ctypes.c_void_p, ctypes.c_uint32], ctypes.c_bool
        )

        self.pause_track = self.bind("MIX_PauseTrack", [ctypes.c_void_p], ctypes.c_bool)

        self.resume_track = self.bind(
            "MIX_ResumeTrack", [ctypes.c_void_p], ctypes.c_bool
        )

        self.stop_track = self.bind(
            "MIX_StopTrack", [ctypes.c_void_p, ctypes.c_int64], ctypes.c_bool
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
