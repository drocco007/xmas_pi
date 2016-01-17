from gpiozero import PWMLED


white1 = PWMLED(15)
green = PWMLED(18)
blue = PWMLED(17)
red = PWMLED(27)


gammas = [0.3, 1.0, 1.0, 0.1]
lights = [blue, red, green, white1]
