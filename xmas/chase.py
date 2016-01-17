"""Chase program: run the lights in sequence, one light on at a time.

"""

from collections import deque
from functools import partial
from itertools import cycle
import time
import sys


def chase(gammas=(), until=sys.maxsize, forward=True):
    direction = 1 if forward else -1

    # start with the first light on and the rest off
    lights = deque([True] + [False] * (len(gammas) - 1))

    while time.time() < until:
        yield [on and gamma or 0
               for on, gamma in zip(lights, gammas)]
        time.sleep(0.15)
        lights.rotate(direction)


forward = chase
reverse = partial(chase, forward=False)
