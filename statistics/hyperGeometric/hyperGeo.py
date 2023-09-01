# the purpose of this file is to calculate a hypergeometric probability.
def hyperGeoExact(deckSize, sampleSize, successes, successesToDraw):
    # if the successes we need to draw is 0...

        # if the sample size is 0, return 1.

        # otherwise...

            # return the chance to not draw the card we want times hyperGeoExact
            # with one less deckSize and one less sample size.

    # if the number of successes in deck is 0, there is no chance that we're
    # going to draw one.

    # if the sample size is greater than or equal to the deck size, then we must
    # be able to draw one.

    # if the number of successes we need to draw is greater than the
    # sample size, we don't have enough draws to accommodate the number of
    # the wanted card(s) we want to draw.

    # otherwise, return the probability that either you don't draw the wanted
    # card so there is one less deck size and one less sample size, or you draw
    # the wanted card so there is one less deck size, one less sample size, and
    # one less successes left to draw.

# the theoretical "or" of 2 probabilities.
def probabilityOr(a, b):
    return 1 - (1-a)*(1-b) # "either a or b" is "(not a) nand (not b)"



