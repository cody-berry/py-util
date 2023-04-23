import math

seed = 244
m = 1600
c = 421
a = 161


def random():
    return (seed*a + c) % m

iterations = 1
seed = random()
print(seed/100)
while not seed == 244:
    seed = random()
    print(seed/100)
    iterations += 1


