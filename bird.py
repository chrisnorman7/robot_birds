"""The bird class."""

import os, os.path
from aiming import LEFT, RIGHT
from sound_lib.stream import FileStream
from sound import get_file
from random import random, choice
from threading import Thread # For playing sounds after the object has been destroyed.

birds_path = os.path.join('sounds', 'birds')

birds = [] # The birds that are currently instantiated.

last_generated = 0.0 # The time the last bird was generated.

class Bird(object):
 """This should start making a sound as soon as it is created, and stop the sound when it is destroyed."""
 
 def __init__(self, pos):
  """Create the object."""
  self.sound = FileStream(file = os.path.join(birds_path, choice(os.listdir(birds_path))))
  if pos == LEFT:
   pan = -1.0
  elif pos == RIGHT:
   pan = 1.0
  else:
   pan = 0.0
  self.pan = pan
  self.sound.pan = pan
  self.position = pos
  self.sound.looping = True
  self.sound.play(True)
  self.hp = int(random() * 9)
  self.hit_sound = FileStream(file = os.path.join('sounds', 'hit.wav'))
  self.hit_sound.pan = pan
 
 def destroy(self):
  """Destroy the bird."""
  birds.remove(self)
  sound = FileStream(file = os.path.join('sounds', get_file('OtherDestroyed*11.wav')))
  sound.pan = self.pan
  self.sound.stop()
  Thread(target = sound.play_blocking, args = [True]).start()
 
 def hit(self):
  """This bird has been hit."""
  self.hp -= 1
  if self.hp <= 0:
   self.destroy()
  else:
   self.hit_sound.play(True)
