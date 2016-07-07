"""Aiming stuff."""

from sound_lib.stream import FileStream
import os.path

LEFT = 0
CENTRE = 1
RIGHT = 2

aim_sound = FileStream(file = os.path.join('sounds', 'aim.wav'))

aiming = CENTRE
