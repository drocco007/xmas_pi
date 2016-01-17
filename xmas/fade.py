from collections import deque
from functools import partial
from itertools import cycle
import time
import sys


def fade(gammas=(), until=sys.maxsize, out=True):
    until = min(time.time() + 3, until)
    steps = 20.0
    delta_pct = 1.0 / steps
    
    if out:
        direction = -1
        values = gammas[:]
    else:
        direction = 1
        values = [0.0] * len(gammas)

    while time.time() < until:
        values = [max(min(value + delta_pct * gamma * direction, 1.0), 0.0)
                  for value, gamma in zip(values, gammas)]
        yield values
        time.sleep(0.15)


fade_out = fade
fade_in = partial(fade, out=False)
