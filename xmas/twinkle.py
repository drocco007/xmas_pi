from random import choice, random, gauss, randint
from time import sleep, time
import sys


def source():
    value = 1.0

    while True:
        change = choice([-1.0, 0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0])

        if not change:
            yield value

            # make the light tend to drift toward on
            value = min(value + 0.1, 1.0)
        else:
            # twinkle in the direction indicated by the change value
            steps = randint(1, 15)
            delta = (gauss(value, 0.45) * change) / float(steps)

            for _ in range(steps):
                value += delta
                value = min(max(value, 0), 1.0)
                yield value


def twinkle(n_lights, until=sys.maxsize):
    sources = [source() for _ in xrange(n_lights)]
    until = until + 10

    while time() < until:
        yield map(next, sources)
        sleep(0.05)
