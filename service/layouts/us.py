# USB HID Keycode constants.
#    This list is modeled after the names for USB keycodes defined in
#    https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf#page:53.
#    This list does not include every single code, but does include all the keys on
#    a regular PC or Mac keyboard.
#    Remember that keycodes are the names for key *positions* on a US keyboard, and may
#    not correspond to the character that you mean to send if you want to emulate non-US keyboard.
#    For instance, on a French keyboard (AZERTY instead of QWERTY),
#    the keycode for 'q' is used to indicate an 'a'. Likewise, 'y' represents 'z' on
#    a German keyboard. This is historical: the idea was that the keycaps could be changed
#    without changing the keycodes sent, so that different firmware was not needed for
#    different variations of a keyboard.

kbd = {
        "modifiers" : {
                "CTRL" : chr(0x01),
                "SHIFT" : chr(0x02),
                "ALT" : chr(0x04),
                "GUI" : chr(0x08),

                "LEFT_CTRL" : chr(0x01),
                "LEFT_SHIFT" : chr(0x02),
                "LEFT_ALT" : chr(0x04),
                "LEFT_GUI" : chr(0x08),
                "RIGHT_CTRL" : chr(0x10),
                "RIGHT_SHIFT" : chr(0x20),
                "RIGHT_ALT" : chr(0x40),
                "RIGHT_GUI" : chr(0x80),

                "MEDIA_VOLUME_INC" : chr(0x80),
                "MEDIA_VOLUME_DEC" : chr(0x81),
                "MEDIA_MUTE" : chr(0x7F),
                "MEDIA_PLAY_PAUSE" : chr(0x08),
                "MEDIA_NEXT_TRACK" : chr(0x10),
                "MEDIA_PREV_TRACK" : chr(0x20)
        },

        "keycode" : {
                "a" : chr(0x04),
                "b" : chr(0x05),
                "c" : chr(0x06),
                "d" : chr(0x07),
                "e" : chr(0x08),
                "f" : chr(0x09),
                "g" : chr(0x0A),
                "h" : chr(0x0B),
                "i" : chr(0x0C),
                "j" : chr(0x0D),
                "k" : chr(0x0E),
                "l" : chr(0x0F),
                "m" : chr(0x10),
                "n" : chr(0x11),
                "o" : chr(0x12),
                "p" : chr(0x13),
                "q" : chr(0x14),
                "r" : chr(0x15),
                "s" : chr(0x16),
                "t" : chr(0x17),
                "u" : chr(0x18),
                "v" : chr(0x19),
                "w" : chr(0x1A),
                "x" : chr(0x1B),
                "y" : chr(0x1C),
                "z" : chr(0x1D),

                "1": chr(0x1E),
                "2" : chr(0x1F),
                "3" : chr(0x20),
                "4" : chr(0x21),
                "5" : chr(0x22),
                "6" : chr(0x23),
                "7" : chr(0x24),
                "8" : chr(0x25),
                "9" : chr(0x26),
                "0" : chr(0x27),

                "ENTER" : chr(0x28),
                "ESCAPE" : chr(0x29),
                "BACKSPACE" : chr(0x2A),
                "TAB" : chr(0x2B),
                "SPACEBAR" : chr(0x2C), # spacebar
                " " : chr(0x2C), # spacebar

                "[" : chr(0x2F),
                "]" : chr(0x30),
                "\\" : chr(0x31),
                "#" : chr(0x32),
                ";" : chr(0x33),
                "'" : chr(0x34),
                "`" : chr(0x35),
                "," : chr(0x36),
                "." : chr(0x37),
                "/" : chr(0x38),
                " " : chr(0x2C), # spacebar
                "-" : chr(0x2D),
                "=" : chr(0x2E),

                "CAPS_LOCK" : chr(0x39),

                "F1" : chr(0x3A),
                "F2" : chr(0x3B),
                "F3" : chr(0x3C),
                "F4" : chr(0x3D),
                "F5" : chr(0x3E),
                "F6" : chr(0x3F),
                "F7" : chr(0x40),
                "F8" : chr(0x41),
                "F9" : chr(0x42),
                "F10" : chr(0x43),
                "F11" : chr(0x44),
                "F12" : chr(0x45),

                "PRINT_SCREEN" : chr(0x46),
                "SCROLL_LOCK" : chr(0x47),
                "PAUSE" : chr(0x48),

                "INSERT" : chr(0x49),
                "HOME" : chr(0x4A),
                "PAGE_UP" : chr(0x4B),
                "DELETE" : chr(0x4C),
                "END" : chr(0x4D),
                "PAGE_DOWN" : chr(0x4E),

                "RIGHT_ARROW" : chr(0x4F),
                "LEFT_ARROW" : chr(0x50),
                "DOWN_ARROW" : chr(0x51),
                "UP_ARROW" : chr(0x52),

                "KEYPAD_NUMLOCK" : chr(0x53),
                "KEYPAD_FORWARD_SLASH" : chr(0x54),
                "KEYPAD_ASTERISK" : chr(0x55),
                "KEYPAD_MINUS" : chr(0x56),
                "KEYPAD_PLUS" : chr(0x57),
                "KEYPAD_ENTER" : chr(0x58),
                "KEYPAD_ONE" : chr(0x59),
                "KEYPAD_TWO" : chr(0x5A),
                "KEYPAD_THREE" : chr(0x5B),
                "KEYPAD_FOUR" : chr(0x5C),
                "KEYPAD_FIVE" : chr(0x5D),
                "KEYPAD_SIX" : chr(0x5E),
                "KEYPAD_SEVEN" : chr(0x5F),
                "KEYPAD_EIGHT" : chr(0x60),
                "KEYPAD_NINE" : chr(0x61),
                "KEYPAD_ZERO" : chr(0x62),
                "KEYPAD_PERIOD" : chr(0x63),
                "KEYPAD_BACKSLASH" : chr(0x64),

                "APPLICATION" : chr(0x65),
                "POWER" : chr(0x66),
                "KEYPAD_EQUALS" : chr(0x67),
                "F13" : chr(0x68),
                "F14" : chr(0x69),
                "F15" : chr(0x6A),
                "F16" : chr(0x6B),
                "F17" : chr(0x6C),
                "F18" : chr(0x6D),
                "F19" : chr(0x6E),
                
                "LEFT_CONTROL" : chr(0xE0),
                "LEFT_SHIFT" : chr(0xE1),
                "LEFT_ALT" : chr(0xE2),

                "LEFT_GUI" : chr(0xE3),

                "RIGHT_CONTROL" : chr(0xE4),
                "RIGHT_SHIFT" : chr(0xE5),
                "RIGHT_ALT" : chr(0xE6),
                "RIGHT_GUI" : chr(0xE7),

                # aliases
                "GUI" : chr(0xE3),
                "SHIFT" : chr(0xE1),
                "CONTROL" : chr(0xE0),
                "ALT" : chr(0xE2),
        },
        "shifted" : {
            # shift : normal
                "~" : "`",
                "!" : "1",
                "@" : "2",
                "#" : "3",
                "$" : "4",
                "%" : "5",
                "^" : "6",
                "&" : "7",
                "*" : "8",
                "(" : "9",
                ")" : "0",
                "{" : "[",
                "}" : "]",
                "+" : "=",
                "_" : "-",
                ":" : ";",
                "?" : "/",
                "<" : ",",
                ">" : ".",
                "|" : "\\",
                "\"": "'"
        },

        "altgr" : {
            # altgr : normal
        }
}