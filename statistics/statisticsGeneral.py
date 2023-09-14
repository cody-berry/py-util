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

import scipy.stats as stats
import numpy as np
from scipy.integrate import quad

# defines the normal distribution we're using
def normalProbabilityDensity(i):
    coefficient = 1.0/np.sqrt(2*np.pi)
    return coefficient * np.exp((-i**2) / 2)


