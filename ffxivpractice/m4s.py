# possibilities for all mechanics in AAC Light-Heavyweight M4 Illustrated,
# or M4S.
import random

# the below prints possible possibilities.

# example: "in lines exploding. supports bait...far."
# other example "out lines exploding. DPS bait...near."
def BewitchingFlight():
	print("\033[33mBewitching Flight\033[0m")
	linesExplodingFirst = random.choice(["in", "out"]) + " lines exploding. "
	DPSOrSupportsTargetedWithJump = random.choice(["DPS", "supports"]) + " bait"
	bait = random.choice(["near", "far"])


	print(linesExplodingFirst, end="")
	print(DPSOrSupportsTargetedWithJump, end="")
	print("...", end="")
	print(bait)

# this will print something like:
# Tanks in, so the easy pattern.
# Healers out.
# Melees in.
# Ranged out.
def NarrowingWideningWitchHunt():
	# Narrowing/Widening Witch Hunt
	callouts = random.choice([
		["Tanks in, so the easy pattern.", "healers out.",
		 "melees in.", "ranged out."], # Narrowing, near baits first
		["Healers out. Sames.", "tanks in.",
		 "melees in.", "ranged out."], # Widening, far baits first.
		["Tanks on waymark, so it's the...um, hard pattern.", "healers on waymark",
		 "melees on waymark", "ranged on waymark."], # Widening, near baits first.
		["Healers on waymark. Opposites.", "Tanks on waymark.",
		 "Melees on waymark.", "Ranged on waymark."] # Narrowing, far baits first.
	])
	cast = "Widening"
	if (callouts == [
		"Tanks in, so the easy pattern.", "healers out.",
		 "melees in.", "ranged out."] or callouts == [
		"Healers on waymark. Opposites.", "Tanks on waymark.",
		 "Melees on waymark.", "Ranged on waymark."]):
		cast = "Narrowing"

	baits = "♦🔶♦ ♦——🔷——♦ ♦🔶♦ ♦——🔷——♦"
	if (callouts == ["Healers out. Sames.", "tanks in.",
		 "melees in.", "ranged out."] or callouts == [
		"Healers on waymark. Opposites.", "Tanks on waymark.",
		 "Melees on waymark.", "Ranged on waymark."]):
		baits = "♦——🔷——♦ ♦🔶♦ ♦——🔷——♦ ♦🔶♦"

	print("\033[33m" + cast + " Witch Hunt\033[0m")
	print("Baits " + baits)

	for callout in callouts:
		print(callout)


# example: Spreads at 2.
def EE1():
	print("\033[33mEE1\033[0m")

	safeQuadrant = random.randint(1, 4)
	spreadsOrStack = random.choice(["spreads", "stacks"])
	print(spreadsOrStack, end="")
	print(" at ", end="")
	print(safeQuadrant)



def selectMechanic(integer):
	if integer == 1:
			BewitchingFlight()
			return
	if integer == 2:
			NarrowingWideningWitchHunt()
			return
	if integer == 3:
			EE1()
			return


while __name__ == "__main__":
	# UI: select a mechanic
	integer = input(
		"Enter mechanic that you want to generate a random scenario for.\n"
		"1. Bewitching Flight\n"
		"2. Narrowing/Widening Witch Hunt\n"
		"3. EE1 (Electrope Edge 1)\n"
		"Type in here: ")
	selectMechanic(int(integer))
	print("\n\n")



