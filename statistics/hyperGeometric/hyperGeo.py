# the purpose of this file is to calculate a hypergeometric probability.
def hyperGeoExact(deckSize, sampleSize, successes, successesToDraw, indents):
    print((indents - 1) * " |", "🍅 →", deckSize, sampleSize, successes,
          successesToDraw)
    # if the successes we need to draw is 0...
    if successesToDraw == 0:
        # if the sample size is 0, return 1.
        if sampleSize == 0:
            print(indents * " |",
                  "🍑 1 → There is no draws left and we're exactly right")
            return 1
        else:
            print(indents * " |", "🍉")
            # return the chance to not draw the card we want times hyperGeoExact
            # with one less deckSize and one less sample size.
            recursiveWhenNotDrawn = hyperGeoExact(deckSize-1, sampleSize-1, successes, successesToDraw, indents+1)
            print(indents * " |", "🍉", (1 - successes / deckSize) * recursiveWhenNotDrawn, "← Chance to not draw any more")
            return (1 - successes / deckSize) * recursiveWhenNotDrawn

    # if the number of successes in deck is 0, there is no chance that we're
    # going to draw one.
    if successes == 0:
        print(indents * " |", "🍊 0 → No successes left in deck")
        return 0

    # if the sample size is greater than or equal to the deck size, then we must
    # be able to draw one.
    if sampleSize >= deckSize:
        print(indents * " |", "🍓 1 → Too many cards to draw")
        return 1

    # if the number of successes we need to draw is greater than the
    # sample size, we don't have enough draws to accommodate the number of
    # the wanted card(s) we want to draw.
    if successesToDraw > sampleSize:
        print(indents * " |", "🍎 0 → Too many successes needed")
        return 0

    # otherwise, return the probability that either you don't draw the wanted
    # card so there is one less deck size and one less sample size, or you draw
    # the wanted card so there is one less deck size, one less sample size, and
    # one less success left to draw.
    recursiveWhenDrawn = hyperGeoExact(deckSize - 1, sampleSize - 1,
                                       successes - 1,
                                       successesToDraw - 1,
                                       indents + 1)

    print(indents * " |", "🍆", recursiveWhenDrawn, "←",
          deckSize - 1,
          sampleSize - 1,
          successes - 1,
          successesToDraw - 1)
    print(indents * " |", "🍇", recursiveWhenDrawn * (successes / deckSize))

    recursiveWhenNotDrawn = hyperGeoExact(deckSize - 1, sampleSize - 1,
                                          successes, successesToDraw,
                                          indents + 1)

    print(indents * " |", "🍆", recursiveWhenNotDrawn, "←",
          deckSize - 1,
          sampleSize - 1,
          successes,
          successesToDraw)
    print(indents * " |", "🍇",
          recursiveWhenNotDrawn * ((deckSize - successes) / deckSize))

    return\
        (successes / deckSize) * recursiveWhenDrawn +\
        ((deckSize - successes) / deckSize) * recursiveWhenNotDrawn


# returns the "or" of 2 probabilities (a and b).
def probabilityOr(a, b):
    return a + b - a*b



def hyperAtLeast(deckSize, sampleSize, successes, minSuccesses):
    return sum([hyperGeoExact(deckSize, sampleSize, successes, i, 1) for i in
                range(minSuccesses, successes + 1)])




while True:
    print("\033[2J")
    print(
        " 🍆", hyperAtLeast(
            int(input("Deck size ")),
            int(input("Sample size ")),
            int(input("Successes in deck ")),
            int(input("Wanted successes "))))
