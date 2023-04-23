import math

# declaration values. when c != 0, if you want to make a good
# random number generator:
#   m and c are relatively prime
#   a-1 is divisible by all of the prime factors of m
#   a-1 is divisible by 4 if m is divisible by 4
# I don't know why, though.
seed = 244
m = 1600
c = 421
a = 161


# the core of the linear congruential generator, the formula.
def random():
    return (seed*a + c) % m

# starter to make sure that seed doesn't originally equal 244.
# because of potential use in 2048, dividing by 100 to make m 16.
seed = random()
print(seed/100)
while not seed == 244:
    seed = random()
    print(seed/100)


