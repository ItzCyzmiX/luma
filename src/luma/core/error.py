class Luma_Error(Exception):
    def __init__(self, sdl_error_message: bytes) -> None:
        super().__init__(
            "\n--LUMA ERROR--\nSDL_GetError returned:\n"
            + (sdl_error_message.decode() or "Unknown SDL error")
        )
