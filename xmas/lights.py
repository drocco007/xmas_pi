from gpiozero import PWMLED


white1 = PWMLED(15)
green = PWMLED(18)
blue = PWMLED(17)
red = PWMLED(27)


# Relative brightness for each light. Since I'm using scrounged LEDs, the
# apparent maximum brightness at full power varies from light to light. This
# list lets us tune the maximum brightness values we will use for each light
# so that the lights in the display appear visually balanced with each other.
# For example, I've set the maximum brightness of the blue LED to 0.3 since it
# is a high-efficiency device.
gammas = [0.3, 1.0, 1.0, 0.1]
lights = [blue, red, green, white1]
