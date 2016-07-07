"""Keyboard handler."""

import aiming, os, os.path, bird, pyglet
from accessibility import system
from random import random
from pyglet.window import key
from sound_lib.stream import FileStream

weapons_path = os.path.join('sounds', 'weapons')
weapons = [x[:x.find('.')] for x in os.listdir(weapons_path)]

class Handler(object):
 """Handle all keyboard events."""
 
 def __init__(self):
  """Start the background music."""
  self.background = FileStream(file = os.path.join('sounds', 'background.wav'))
  self.background.looping = True
  self.background.play(True)
  self.weapon = 0
  self.arm()
  self.miss_sound = FileStream(file = os.path.join('sounds', 'miss.wav'))
 
 def arm(self, offset = 0):
  """Change weapon."""
  self.weapon += offset
  if self.weapon >= len(weapons):
   self.weapon = 0
  elif self.weapon < 0:
   self.weapon = len(weapons) - 1
  if offset:
   system.speak(weapons[self.weapon])
  self.weapon_sound = FileStream(file = os.path.join(weapons_path, weapons[self.weapon] + '.wav'))
 
 def aim(self, direction):
  """Start aiming."""
  aiming.aiming = direction
  aiming.aim_sound.stop()
  if direction == aiming.LEFT:
   pan = -1.0
  elif direction == aiming.RIGHT:
   pan = 1.0
  else:
   pan = 0.0
  aiming.aim_sound.pan = pan
  aiming.aim_sound.play(True)
 
 def fire(self):
  """Fire the current weapon."""
  self.weapon_sound.play(True)
  for b in bird.birds:
   if b.position == aiming.aiming:
    b.hit()
    break
  else:
   pyglet.clock.schedule_once(self.miss, 0.25)
 
 def miss(self, dt):
  """The player missed."""
  self.miss_sound.pan = (random() * 2) - 1.0
  self.miss_sound.play(True)
 
 def on_key_press(self, single, modifiers):
  """A key was pressed."""
  if single == key.LEFT:
   self.aim(aiming.LEFT)
  elif single == key.UP:
   self.aim(aiming.CENTRE)
  elif single == key.RIGHT:
   self.aim(aiming.RIGHT)
  elif single == key.SPACE:
   self.fire()
  elif single == key.BRACKETLEFT:
   self.arm(-1)
  elif single == key.BRACKETRIGHT:
   self.arm(1)
  elif single == key.RETURN:
   if self.background.volume == 1.0:
    self.background.volume = 0.0
   else:
    self.background.volume = 1.0