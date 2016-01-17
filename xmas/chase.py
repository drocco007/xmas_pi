"""Chase program: run the lights in sequence, one light on at a time.

"""

from collections import deque
from functools import partial
from itertools import cycle
import time
import sys


def chase(n_lights, until=sys.maxsize, forward=True):
    direction = 1 if forward else -1

    # start with the first light on and the rest off
    lights = deque([1.0] + [0.0] * (n_lights - 1))

    while time.time() < until:
        yield lights
        time.sleep(0.15)
        lights.rotate(direction)


forward = chase
reverse = partial(chase, forward=False)
