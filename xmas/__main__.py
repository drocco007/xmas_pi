from itertools import cycle
import time

from lights import lights, gammas
from util import normalize

from chase import forward, reverse
from fade import fade_in, fade_out
from twinkle import twinkle


# The light programs we want to run, repeated endlessly
programs = iter(cycle([fade_in, forward, twinkle, reverse, fade_out]))


while True:
    program = next(programs)

    # each program should run for at most 5 seconds
    until = time.time() + 5

    # each program is a generator that, at each iteration, yields a list of
    # values, each corresponding to the brightness of the respective light,
    # from a minimum of 0.0 (off) to a maximum of 1.0 (full on)
    for values in program(len(lights), until=until):

        # Normalize each light's value according to its gamma (maximum
        # brightness)
        values = normalize(values, gammas)

        for i, value in enumerate(values):

            # Actually change the light's brightness; see
            # http://pythonhosted.org/gpiozero/outputs/#pwmled
            lights[i].value = value
