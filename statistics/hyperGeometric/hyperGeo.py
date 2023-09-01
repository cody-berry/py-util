# the purpose of this file is to calculate a hypergeometric probability.
def hyperGeoExact(deckSize, sampleSize, successes, successesToDraw):
    # if the successes we need to draw is 0...
    if successesToDraw == 0:
        # if the sample size is 0, return 1.
        if sampleSize == 0:
            return 1
        # otherwise...
        else:
            # return the chance to not draw the card we want times hyperGeoExact
            # with one less deckSize and one less sample size.
            return (1 - successes / deckSize)**sampleSize

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
    # one less successes left to draw.
    return probabilityOr(
        (successes / deckSize) * hyperGeoExact(deckSize - 1, sampleSize - 1,
                                               successes - 1,
                                               successesToDraw - 1),
        (1 - successes / deckSize) * hyperGeoExact(deckSize - 1, sampleSize - 1,
                                                   successes, successesToDraw)
    )

# the theoretical "or" of 2 probabilities.
def probabilityOr(a, b):
    return a + b


print(hyperGeoExact(3, 2, 1, 1))
