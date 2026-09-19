from enum import IntFlag


class SDL_WindowFlags(IntFlag):
    DEFAULT = 0
    """default window flag"""
    FULLSCREEN = 0x0000000000000001
    """window is in fullscreen mode"""
    OPENGL = 0x0000000000000002
    """window usable with OpenGL context"""
    OCCLUDED = 0x0000000000000004
    """window is occluded"""
    HIDDEN = 0x0000000000000008
    """window is neither mapped onto the desktop nor shown in the taskbar/dock/window list;
    SDL_ShowWindow() is required for it to become visible"""
    BORDERLESS = 0x0000000000000010
    """no window decoration"""
    RESIZABLE = 0x0000000000000020
    """window can be resized"""
    MINIMIZED = 0x0000000000000040
    """window is minimized"""
    MAXIMIZED = 0x0000000000000080
    """window is maximized"""
    MOUSE_GRABBED = 0x0000000000000100
    """window has grabbed mouse input"""
    INPUT_FOCUS = 0x0000000000000200
    """window has input focus"""
    MOUSE_FOCUS = 0x0000000000000400
    """window has mouse focus"""
    EXTERNAL = 0x0000000000000800
    """window not created by SDL"""
    MODAL = 0x0000000000001000
    """window is modal"""
    HIGH_PIXEL_DENSITY = 0x0000000000002000
    """window uses high pixel density back buffer if possible"""
    MOUSE_CAPTURE = 0x0000000000004000
    """window has mouse captured (unrelated to MOUSE_GRABBED)"""
    MOUSE_RELATIVE_MODE = 0x0000000000008000
    """window has relative mode enabled"""
    ALWAYS_ON_TOP = 0x0000000000010000
    """window should always be above others"""
    UTILITY = 0x0000000000020000
    """window should be treated as a utility window, not showing in the task bar and window list"""
    TOOLTIP = 0x0000000000040000
    """window should be treated as a tooltip and does not get mouse or keyboard focus,
    requires a parent window"""
    POPUP_MENU = 0x0000000000080000
    """window should be treated as a popup menu, requires a parent window"""
    KEYBOARD_GRABBED = 0x0000000000100000
    """window has grabbed keyboard input"""
    FILL_DOCUMENT = 0x0000000000200000
    """window is in fill-document mode (Emscripten only), since SDL 3.4.0"""
    VULKAN = 0x0000000010000000
    """window usable for Vulkan surface"""
    METAL = 0x0000000020000000
    """window usable for Metal view"""
    TRANSPARENT = 0x0000000040000000
    """window with transparent buffer"""
    NOT_FOCUSABLE = 0x0000000080000000
    """window should not be focusable"""
