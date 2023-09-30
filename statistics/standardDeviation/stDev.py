# calculate the standard deviation based on a table
from math import sqrt


def standardDev(mean, *table):
    variation = 0
    for element in table:
        variation += ((element[0] - mean)**2)*(element[1])
    return sqrt(variation)

while True:
    mean = float(input("Mean of distribution: "))
    table = []
    try:
        while True:
            table.append([float(input("Element value: ")), float(input("Element probability: "))])
    except:
        pass
    print(standardDev(mean, *table))