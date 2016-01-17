from itertools import cycle
import time

from lights import lights, gammas

from chase import forward, reverse 
from fade import fade_in, fade_out
from twinkle import twinkle


programs = iter(cycle([fade_in, forward, twinkle, reverse, fade_out]))


while True:
    program = next(programs)
    until = time.time() + 5

    for values in program(gammas, until=until):
        for i, value in enumerate(values):
            lights[i].value = value
