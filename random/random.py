import math

# declaration values. when c != 0, if you want to make a good
# random number generator:
#   m and c are relatively prime
#   a-1 is divisible by all of the prime factors of m
#   a-1 is divisible by 4 if m is divisible by 4
# Allows for a 1600 period.
seed = 244
originSeed = 244
m = 1600
c = 421
a = 161


# the core of the linear congruential generator, the formula.
# a is the multiplier, c is a constant that adds to seed*a,
# seed is the starter value that becomes the result of the
# random() function in the end, and m is the modulus or max
# (exclusive at max and inclusive at min).
def random():
    return (seed*a + c) % m


# starter to make sure that seed doesn't originally equal 244.
# because of potential use in 2048, dividing by 100 makes m 16,
# the maximum that is used in 2048.
seed = random()
print(seed/100)
while not seed == originSeed:
    seed = random()
    print(seed/100)
