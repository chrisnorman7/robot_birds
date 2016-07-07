"""Main entry point."""

from time import time
from random import choice, random
from sound import output
import os.path, pyglet, bird, aiming
from handler import Handler

window = pyglet.window.Window(caption = 'Robot Birds')

def generate_bird(dt):
 """Generate a new bird if we're running out."""
 t = time()
 if t - bird.last_generated >= 3.0: # Let's make a new bird.
  bird.last_generated = t
  # Add in some randomness if there's still birds left to shoot at:
  if random() <= 0.5 and bird.birds:
   return # Don't make another bird at this time.
  empty = [aiming.LEFT, aiming.CENTRE, aiming.RIGHT] # The positions which aren't already filled.
  for b in bird.birds:
   empty.remove(b.position)
  if empty:
   bird.birds.append(bird.Bird(choice(empty)))

if __name__ == '__main__':
 window.set_handlers(Handler())
 pyglet.clock.schedule(generate_bird)
 pyglet.app.run()
