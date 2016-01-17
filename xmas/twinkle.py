from random import choice, random, gauss, randint
from time import sleep, time
import sys


def source(gamma):
    value = gamma

    while True:
        change = choice([-1.0, 0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0])

        if not change:
            yield value
            value = min(value + 0.1 * gamma, gamma)
        else:
            steps = randint(1, 15)
            delta = (gauss(value, 0.45) * change) / float(steps)

            for _ in range(steps):
                value += delta
                value = min(max(value, 0), gamma)
                yield value

def twinkle(gammas=(), until=sys.maxsize):
    sources = [source(gamma) for gamma in gammas]
    until = until + 10

    while time() < until:
        yield map(next, sources)
        sleep(0.05)
