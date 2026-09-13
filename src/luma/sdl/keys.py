from enum import Enum


class KEYS(Enum):
    RETURN = 0x0000000D
    ESCAPE = 0x0000001B
    BACKSPACE = 0x00000008
    TAB = 0x00000009
    SPACE = 0x00000020
    EXCLAIM = 0x00000021
    DBLAPOSTROPHE = 0x00000022
    HASH = 0x00000023
    DOLLAR = 0x00000024
    PERCENT = 0x00000025
    AMPERSAND = 0x00000026
    APOSTROPHE = 0x00000027
    LEFTPAREN = 0x00000028
    RIGHTPAREN = 0x00000029
    ASTERISK = 0x0000002A
    PLUS = 0x0000002B
    COMMA = 0x0000002C
    MINUS = 0x0000002D
    PERIOD = 0x0000002E
    SLASH = 0x0000002F
    NUM_0 = 0x00000030
    NUM_1 = 0x00000031
    NUM_2 = 0x00000032
    NUM_3 = 0x00000033
    NUM_4 = 0x00000034
    NUM_5 = 0x00000035
    NUM_6 = 0x00000036
    NUM_7 = 0x00000037
    NUM_8 = 0x00000038
    NUM_9 = 0x00000039
    COLON = 0x0000003A
    SEMICOLON = 0x0000003B
    LESS = 0x0000003C
    EQUALS = 0x0000003D
    GREATER = 0x0000003E
    QUESTION = 0x0000003F
    AT = 0x00000040
    LEFTBRACKET = 0x0000005B
    BACKSLASH = 0x0000005C
    RIGHTBRACKET = 0x0000005D
    CARET = 0x0000005E
    UNDERSCORE = 0x0000005F
    GRAVE = 0x00000060
    A = 0x00000061
    B = 0x00000062
    C = 0x00000063
    D = 0x00000064
    E = 0x00000065
    F = 0x00000066
    G = 0x00000067
    H = 0x00000068
    I = 0x00000069
    J = 0x0000006A
    K = 0x0000006B
    L = 0x0000006C
    M = 0x0000006D
    N = 0x0000006E
    O = 0x0000006F
    P = 0x00000070
    Q = 0x00000071
    R = 0x00000072
    S = 0x00000073
    T = 0x00000074
    U = 0x00000075
    V = 0x00000076
    W = 0x00000077
    X = 0x00000078
    Y = 0x00000079
    Z = 0x0000007A
    LEFTBRACE = 0x0000007B
    PIPE = 0x0000007C
    RIGHTBRACE = 0x0000007D
    TILDE = 0x0000007E
    DELETE = 0x0000007F
    PLUSMINUS = 0x000000B1
    CAPSLOCK = 0x40000039
    F1 = 0x4000003A
    F2 = 0x4000003B
    F3 = 0x4000003C
    F4 = 0x4000003D
    F5 = 0x4000003E
    F6 = 0x4000003F
    F7 = 0x40000040
    F8 = 0x40000041
    F9 = 0x40000042
    F10 = 0x40000043
    F11 = 0x40000044
    F12 = 0x40000045


import ctypes


class SDL_KeyboardEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("scancode", ctypes.c_uint32),
        ("key", ctypes.c_uint32),
        ("mod", ctypes.c_uint32),
        ("raw", ctypes.c_uint16),
        ("down", ctypes.c_bool),
        ("repeat", ctypes.c_bool),
    ]
