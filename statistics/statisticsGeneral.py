# calculate the probability to draw exactly the number of successes we want to
# draw.
def hyperExact(deckSize, sampleSize, successes, successesToDraw):
    # if the successes we need to draw is 0...
    if successesToDraw == 0:
        # if the sample size is 0, return 1.
        if sampleSize == 0:
            return 1
        else:
            # return the chance to not draw the card we want times hyperGeoExact
            # with one less deckSize and one less sample size.
            recursiveWhenNotDrawn = hyperExact(deckSize-1, sampleSize-1, successes, successesToDraw)
            return (1 - successes / deckSize) * recursiveWhenNotDrawn

    # if the number of successes in deck is 0, there is no chance that we're
    # going to draw one.
    if successes == 0:
        return 0

    # if the sample size is greater than or equal to the deck size, then we must
    # be able to draw one.
    if sampleSize >= deckSize:
        return 1

    # if the number of successes we need to draw is greater than the
    # sample size, we don't have enough draws to accommodate the number of
    # the wanted card(s) we want to draw.
    if successesToDraw > sampleSize:
        return 0

    # otherwise, return the probability that either you don't draw the wanted
    # card so there is one less deck size and one less sample size, or you draw
    # the wanted card so there is one less deck size, one less sample size, and
    # one less success left to draw.
    recursiveWhenDrawn = hyperExact(deckSize - 1, sampleSize - 1,
                                       successes - 1,
                                       successesToDraw - 1,
                                       )

    recursiveWhenNotDrawn = hyperExact(deckSize - 1, sampleSize - 1,
                                          successes, successesToDraw,
                                          )

    return\
        (successes / deckSize) * recursiveWhenDrawn +\
        ((deckSize - successes) / deckSize) * recursiveWhenNotDrawn

# returns the "or" of 2 probabilities (a and b).
def probabilityOr(a, b):
    return a + b - a*b

def hyperAtLeast(deckSize, sampleSize, successes, minSuccesses):
    return sum([hyperExact(deckSize, sampleSize, successes, i) for i in
                range(minSuccesses, successes + 1)])

def hyperAtMost(deckSize, sampleSize, successes, maxSuccesses):
    return sum([hyperExact(deckSize, sampleSize, successes, i) for i in
                range(0, maxSuccesses + 1)])

def hyperZero(deckSize, sampleSize, successes):
    return hyperExact(deckSize, sampleSize, successes, 0)

def standardDev(mean, *table):
    variation = 0
    for element in table:
        variation += ((element[0] - mean)**2)*(element[1])
    return sqrt(variation)

def roundNumberToThreeDigitsTotal(number):
    # Determine the number of digits in the integer part
    numDigitsBeforeDecimalPoint = len(str(int(number)))

    # Determine the number of decimal places based on the integer part
    if numDigitsBeforeDecimalPoint >= 3:
        decimalPlaces = 0
    elif numDigitsBeforeDecimalPoint == 2:
        decimalPlaces = 1
    elif numDigitsBeforeDecimalPoint == 1:
        decimalPlaces = 2
    else:
        decimalPlaces = 3

    # Round the number based on the determined decimal places
    rounded_number = round(number, decimalPlaces)

    # Format the number with the determined decimal places
    formatted_number = f'{rounded_number:.{decimalPlaces}f}'

    return formatted_number

def shiftAndScaleMeanAndStandardDeviation(μ, σ, shift, scale):
    return [(μ*scale + shift), (σ*scale)]

import scipy.stats as stats
import numpy as np
from scipy.integrate import quad
from math import sqrt

# defines the normal distribution we're using
def normalProbabilityDensity(i):
    coefficient = 1.0/np.sqrt(2*np.pi)
    return coefficient * np.exp((-i**2) / 2)

while True:
    # choose between modes
    print("Choose between these modes:")
    print("1. Calculate the probability of landing between 2 z-scores")
    print("2. Calculate a z-score from a distribution and a value")
    print("3. Calculate a value from a distribution and a z-score")
    print("4. Calculate a z-score from a percentile")
    print("5. Calculate the hypergeometric probability based on all the hypergeometric arguments")
    print("6. Calculate the standard deviation of a table based on its mean and its elements' values and probabilities. ")
    print("7. Shift and scale a mean and standard deviation")
    try:
        mode = int(input("Please choose a mode. "))
        assert mode in [1, 2, 3, 4, 5, 6, 7]
        if mode == 1:
            lowerBound = float(input('lower integration bound:'))
            upperBound = float(input('upper integration bound:'))
            print(quad(normalProbabilityDensity, lowerBound, upperBound))
            print("")
        if mode == 2:
            value = float(input("Value you want to find the z-score of:"))
            μ = float(input("Mean of the distribution:"))
            σ = float(input("Standard deviation of the distribution:"))
            print((value-μ)/σ)
            print("")
        if mode == 3:
            zScore = float(input("Z-score you want to find the value of:"))
            μ = float(input("Mean of the distribution:"))
            σ = float(input("Standard deviation of the distribution:"))
            print(zScore*σ + μ)
            print("")
        if mode == 4:
            percentile = float(input('percentile:'))
            print(stats.norm.ppf(percentile / 100, loc=0, scale=1))
        if mode == 5:
            deckSize = int(input("Deck size "))
            # sample code used to determine that the sample size hasn't been set
            sampleSize = "1000"
            while int(sampleSize) > 995:
                if not sampleSize == "1000":
                    print("Too big. Maximum sample size is 995.")
                sampleSize = int(input("Sample size "))
            successes = int(input("Successes in deck "))
            successesWanted = int(input("Wanted successes "))
            print(
                f"🍆 Chance to draw at least {successesWanted} of the wanted cards:",
                roundNumberToThreeDigitsTotal((hyperAtLeast(
                    deckSize,
                    sampleSize,
                    successes,
                    successesWanted)) * 100) + "%")
            print(
                f"🍆 Chance to draw exactly {successesWanted} of the wanted cards:",
                roundNumberToThreeDigitsTotal((hyperExact(
                    deckSize,
                    sampleSize,
                    successes,
                    successesWanted)) * 100) + "%")
            print(
                f"🍆 Chance to draw at most {successesWanted} of the wanted cards:",
                roundNumberToThreeDigitsTotal((hyperAtMost(
                    deckSize,
                    sampleSize,
                    successes,
                    successesWanted)) * 100) + "%")
            print(
                f"🍆 Chance to draw 0 of the wanted cards:",
                roundNumberToThreeDigitsTotal((hyperZero(
                    deckSize,
                    sampleSize,
                    successes)) * 100) + "%")
            print("")
        if mode == 6:
            mean = float(input("Mean of distribution: "))
            table = []
            try:
                while True:
                    table.append([float(input("Element value: ")),
                                  float(input("Element probability: "))])
            except:
                pass
            print(standardDev(mean, *table))
        if mode == 7:
            print(shiftAndScaleMeanAndStandardDeviation(
                float(input("Mean of distribution: ")),
                float(input("Standard deviation of distribution: ")),
                float(input("Shift of new distribution: ")),
                float(input("Scale of new distribution: "))
            ))
    except:
        print("The mode chosen is invalid. You must choose a mode from 1 to 6. \n")
