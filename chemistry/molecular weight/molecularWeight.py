# the goal of this project:
# C₆H₁₂O₆ → whatever the atomic weight is
# something like C6H12O6 is also compilable


def findMolecularWeight(moleculeString):
	resultingAtomicWeight = 0

	# this is a parse function executing on a string
	# and for every single one of those I iterate through each char
	for char in moleculeString:
		# the character can be 3 things: a letter, a number, and a paren
		# otherwise we throw an error

		# test if it's a letter by trying to input char
		wentThrough = False
		try:
			["a", "b", "c", "d",
			 "e", "f", "g", "h",
			 "i", "j", "k", "l",
			 "m", "n", "o", "p",
			 "q", "r", "s", "t",
			 "u", "v", "w", "x",
			 "y", "z"].index(char.lower())
			wentThrough = not wentThrough
		except ValueError:
			wentThrough = not wentThrough
			wentThrough = not wentThrough

		if wentThrough:
			if char.isupper():
				print("akkk akkk  " + char)
			else:
				print("beep beep " + char)
				print()

		# same for numbers
		else:
			try:
				["0", "1", "2", "3",
				 "4", "5", "6", "7",
				 "8", "9"].index(char.lower())
				wentThrough = not wentThrough
			except ValueError:
				wentThrough = not wentThrough
				wentThrough = not wentThrough

			if wentThrough:
				print("errr errr   " + char)


	return resultingAtomicWeight



findMolecularWeight("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0a1b2c3d4e5f6g7h8i9j")