## Moving objects

`pygame.Vector2()` is used for moving objects in 2D space

- update the position of an object by adding or subtracting vectors
- for example, if our starting position is at `Vector2(0, 1)` and we want to move the object 1 unit to the right, we write `Vector2(1, 0)`

## Organize and manage multiple objects

`pygame.sprite.Group()` is a tool so we can move, update, draw objects at once

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
