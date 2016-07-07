"""Sound stuff."""

import re
from random import random
from sound_lib.output import Output

output = Output()

sound_re = re.compile(r'(\*(\d+))')

def get_file(name):
 """Given a filename like sound*5.wav, return a filename between sound1.wav and sound5.wav."""
 def get_number(match):
  """Get a number from the match."""
  return str(int(random() * int(match.groups()[1])) + 1)
 return re.sub(sound_re, get_number, name)
