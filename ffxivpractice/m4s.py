# possibilities for all mechanics in AAC Light-Heavyweight M4 Illustrated,
# or M4S.
import random



# the below prints possible possibilities.
print("When printing locations, the 🔴red dot is RDM position, 🟢green dot is SGE position.")
print("A ⚫black dot is a filler emoji (empty positions).")
print("Other emojis are used for other people's spots.")
print("Please catch these characters: a️b️️️d️e️f️g️h️i️j️k️l️m️n️o️p️q️r️s️t️u️v️w️x️y️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️️z️ these are caused by bugs from accidental pasting.")
print("Above letters can split into half when wrapping for no reason.")
print("Generally 🔥 means a bug happened too. It's usually paired with a 🐦‍ somewhere in the code lol.")
print("Other letters that look weird (️l️i️k️e️ '️t️️h️a️t️'️)️ are also bad.️")

# example: "in lines exploding. supports bait...far."
# other example "out lines exploding. DPS bait...near."
def BewitchingFlight():
	print("\033[35mBewitching Flight\033[0m")
	linesExplodingFirst = random.choice(["in", "out"]) + " lines exploding. "
	DPSOrSupportsTargetedWithJump = random.choice(["DPS", "supports"]) + " bait"
	bait = random.choice(["near", "far"])


	print(linesExplodingFirst, end="")
	print(DPSOrSupportsTargetedWithJump, end="")
	print("...", end="")
	print(bait)

	input("Display first locations? (any content works, just ensure you press Enter when you're ready)")
	if linesExplodingFirst == "in lines exploding. ":
		print("🐦‍🔥xxx🐅")
		print("🐇xxx🐷")
		print("🐉xxx🔴")
		print("🟢xxx🥝")
	if linesExplodingFirst == "out lines exploding. ":
		print("x🐦‍🔥🐅x")
		print("x🐇🐷x")
		print("x🐉🔴x")
		print("x🟢🥝x")

	input("Display second locations? Remember, " + DPSOrSupportsTargetedWithJump + " " + bait + ". Same procedure as last time.")
	if linesExplodingFirst == "in lines exploding. ":
		if ((DPSOrSupportsTargetedWithJump == "DPS bait" and bait == "near") or
		   (DPSOrSupportsTargetedWithJump == "supports bait" and bait == "far")):
			print("x🐇🐷x")
			print("x🐦‍🔥🐅x")
			print("x🐉🔴x")
			print("x🟢🥝x")
		if ((DPSOrSupportsTargetedWithJump == "DPS bait" and bait == "far") or
		   (DPSOrSupportsTargetedWithJump == "supports bait" and bait == "near")):
			print("x🐦‍🔥🐅x")
			print("x🐇🐷x")
			print("x🟢🥝x")
			print("x🐉🔴x")
	if linesExplodingFirst == "out lines exploding. ":
		if ((DPSOrSupportsTargetedWithJump == "DPS bait" and bait == "near") or
		   (DPSOrSupportsTargetedWithJump == "supports bait" and bait == "far")):
			print("🐇xxx🐷")
			print("🐦‍🔥xxx🐅")
			print("🐉xxx🔴")
			print("🟢xxx🥝")
		if ((DPSOrSupportsTargetedWithJump == "DPS bait" and bait == "far") or
		   (DPSOrSupportsTargetedWithJump == "supports bait" and bait == "near")):
			print("🐦‍🔥xxx🐅")
			print("🐇xxx🐷")
			print("🟢xxx🥝")
			print("🐉xxx🔴")



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

	print("\033[35m" + cast + " Witch Hunt\033[0m")
	print("Baits " + baits)

	for callout in callouts:
		print(callout)


# example: Spreads at 2.
def EE1():
	print("\033[35mEE1\033[0m")

	safeQuadrant = random.randint(1, 4)
	spreadsOrStack = random.choice(["spreads", "stacks"])
	print(spreadsOrStack, end="")
	print(" at ", end="")
	print(safeQuadrant)


# example:
# you have short 3.
# spreads at left part.
def EE2():
	print("\033[35mEE2\033[0m")

	debuffTimer = random.choice(["short", "long"])
	numTimesYouGotHit = random.randint(2, 3)
	print("Debuff status:", end=" ")
	print(debuffTimer, end=" ")
	print(numTimesYouGotHit)


	spreadsOrStack = random.choice(["spreads", "stacks"])
	safeSide = random.choice(["left", "right"])
	print(spreadsOrStack, end=" ")
	print("on the", end=" ")
	print(safeSide, end=" ")
	print("side.")


# example:
# 1st: you have....donut debuff!
# 2nd: you have....circle debuff!
# 3rd: you have....far baiting debuff!
# another example:
# 1st: you have....near baiting debuff!
# 2nd: you have....need-to-get-hit debuff!
# 3rd: you have....far baiting debuff!
def IonCluster():
	print("\033[33mIon \033[34mCluster\033[0m")
	debuff = random.choice(["\033[34mcircle\033[0m", "\033[38;2;8;73;158mdonut\033[0m",
							"\033[36mnear baiting\033[0m", "\033[32mfar baiting\033[0m",
							"\033[35mneed-to-get-hit\033[0m"])
	print("1st:", debuff, "debuff")
	debuff = random.choice(["\033[34mcircle\033[0m", "\033[38;2;8;73;158mdonut\033[0m",
							"\033[36mnear baiting\033[0m", "\033[32mfar baiting\033[0m",
							"\033[35mneed-to-get-hit\033[0m"])
	print("2nd:", debuff, "debuff")
	debuff = random.choice(["\033[34mcircle\033[0m", "\033[38;2;8;73;158mdonut\033[0m",
							"\033[36mnear baiting\033[0m", "\033[32mfar baiting\033[0m",
							"\033[35mneed-to-get-hit\033[0m"])
	print("3rd:", debuff, "debuff")


# example:
# ←↑↑←   — a random row is selected to have 2 lefts
# →↓↓←   — there will be 1-3 downs and the opposite number of ups.
# →↑↑→   — another random row is selected to have 2 rights
# →↑↑←   — all others are opposite, facing inwards (just like with row 2)
def Exaflares():
	print("\033[35mExaflares\033[0m")

	# for the sake of having the grid, we'll select 1-3 unique rows to have down.
	# others have ups.
	numDownArrows = random.randint(1, 3)
	numUpArrows = 4 - numDownArrows
	downArrowRows = []
	upArrowRows = []
	for i in range(4):
		if len(downArrowRows) >= numDownArrows:
			upArrowRows.append(i + 1) # we use row 1-4, not rows 0-3
		elif len(upArrowRows) >= numUpArrows:
			downArrowRows.append(i + 1) # we use row 1-4, not rows 0-3
		else:
			arrowDirection = random.choice(["up", "down"])
			if arrowDirection == "up":
				upArrowRows.append(i + 1)
			if arrowDirection == "down":
				downArrowRows.append(i + 1)

	# then, we select which row on the left faces outside. then we do the same
	# for the right. they will never be on the same row, so we do the right until
	# they are unequal
	availableRows = [1, 2, 3, 4]
	leftRowFacingOutward = random.choice(availableRows)
	rightRowFacingOutward = leftRowFacingOutward
	while leftRowFacingOutward == rightRowFacingOutward:
		rightRowFacingOutward = random.choice(availableRows)

	# now we know what the arrows are
	for row in availableRows:
		# first: the left arrow
		# always faces right unless specified
		if row == leftRowFacingOutward:
			print("←", end="")
		else:
			print("→", end="")

		# then we display the middle arrows (arrows on middle column)
		# if it's part of the downArrowRows, we display ↓↓; otherwise it's ↑↑
		if downArrowRows.__contains__(row):
			print("↓↓", end="")
		else:
			print("↑↑", end="")

		# after all that the right arrow
		# always faces left unless specified
		if row == rightRowFacingOutward:
			print("→")
		else:
			print("←")


def selectMechanic(integer):
	if integer == 1:
		BewitchingFlight()
		return
	elif integer == 2:
		NarrowingWideningWitchHunt()
		return
	elif integer == 3:
		EE1()
		return
	elif integer == 4:
		EE2()
		return
	elif integer == 5:
		IonCluster()
		return
	elif integer == 6:
		Exaflares()
		return
	else:
		print(integer, "is not a valid input.")


while __name__ == "__main__":
	# UI: select a mechanic
	integer = input(
		"Enter mechanic that you want to generate a random scenario for.\n"
		"1. Bewitching Flight\n"
		"2. Narrowing/Widening Witch Hunt\n"
		"3. EE1 (Electrope Edge 1)\n"
		"4. EE2 (Electrope Edge 2)\n"
		"5. Ion Cluster\n"
		"6. Exaflares (phase change)\n"
		"Type in here: ")
	selectMechanic(int(integer))
	print("\n\n")



