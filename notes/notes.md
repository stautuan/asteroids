## Moving objects

`pygame.Vector2()` is used for moving objects in 2D space

- update the position of an object by adding or subtracting vectors
- for example, if our starting position is at `Vector2(0, 1)` and we want to move the object 1 unit to the right, we write `Vector2(1, 0)`

## Organize and manage multiple objects

`pygame.sprite.Group()` is a tool in which we can move, update, and draw objects at once instead of handling them separately. It does get more cluttered as we create more objects in our game.

```python
import pygame

from asteroid import Asteroid
from player import Player
from shot import Shot

# code hereafter is inside a function

# create a group
drawable = python.sprite.Group()

# add all instances of that class to a group
Asteroid.container(drawable)
Player.container(drawable)
Shot.container(drawable)

# iterate over all the objects in this group
for obj in drawable:
    obj.draw(screen)
```

## Delta Time

What is `dt`?

- It's like a stopwatch that tells you how much time has passed.

Why is delta time important?

- It is important because not all computers run games at the same speed.

How does delta time helps?

- It makes sure objects move based on time and not how fast your computer runs. If your computer slows down, the asteroids shouldn't slow down as well. If your computer speeds up, asteroids shouldn't speed up as well.

## Draw shapes

Draw shapes with `polygon.draw`

Some of the shapes:
`pygame.draw.polygon()`
`pygame.draw.circle()`
