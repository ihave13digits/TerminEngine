from os import O_NONBLOCK, system
from sys import stdin
from termios import tcgetattr, ICANON, TCSANOW, ECHO, TCSAFLUSH, tcsetattr
from fcntl import fcntl, F_SETFL, F_GETFL

class InputMap:

    def __init__(self):
        self.K = Keys()

class Keys:
    ARROW_UP: str = "\x1b[A"
    ARROW_DOWN: str = "\x1b[B"
    ARROW_RIGHT: str = "\x1b[C"
    ARROW_LEFT: str = "\x1b[D"
    ESC: str = "\x1b"
    ENTER: str = "\n"
    TAB: str = "\t"
    SPACE_BAR: str = " "
    F1: str = "\x1bOP"
    F2: str = "\x1bOQ"

##-- Grabs Key --##

class Event():

    def get_text():
        txt = input()
        return txt

    def get_char(f=str):
        # Linux support only
        system("stty raw -echo")
        c = stdin.read(1)
        system("stty -raw echo")
        return f(c)

    def keypress(keys_len=5):
        # This code was provided by a friend, Linnux support only
        fd = stdin.fileno()

        oldterm = tcgetattr(fd)
        newattr = tcgetattr(fd)
        newattr[3] = newattr[3] & ~ICANON & ~ECHO
        tcsetattr(fd, TCSANOW, newattr)

        oldflags = fcntl(fd, F_GETFL)
        fcntl(fd, F_SETFL, oldflags | O_NONBLOCK)

        try:
            while True:
                try:
                    key = stdin.read(keys_len)
                    break
                except IOError:
                    pass
        finally:
            tcsetattr(fd, TCSAFLUSH, oldterm)
            fcntl(fd, F_SETFL, oldflags)
        return key
