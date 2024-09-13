# the goal of this project:
# C₆H₁₂O₆ → whatever the atomic weight is
# something like C6H12O6 is also compilable

# download the molecule data
import json

with open('../chemicalData.json') as data:
	print(data)
	chemicalData = json.load(data)
print(chemicalData)


def findMolecularWeight(moleculeString):
	global elementDataForCurrentChemicalSymbol
	resultingAtomicWeight = 0
	currentChemicalSymbol = ""
	currentNumber = ""

	currentAtomicWeightInParens = 0
	isInParen = False

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
			# we want to check if the character is uppercase or lowercase, as
			# the difference between "HF" (hydrofluoric acid) and "Hf" (hafnium)
			# is huge
			if char.isupper():
				# if it's an uppercase character, we want to check whether the
				# current chemical symbol is empty. if it is, we don't need to
				# do anything; if it isn't, we'll need to compile what is
				# inside currentChemicalSymbol and currentNumber.
				if len(currentChemicalSymbol) > 0:
					print("🍓 🍓 🍓" + currentChemicalSymbol + currentNumber)

					# find the element's data by iterating through each element
					# in chemicalData and searching
					for elementData in chemicalData["elements"]:
						if elementData["symbol"] == currentChemicalSymbol:
							elementDataForCurrentChemicalSymbol = elementData

					resultingAtomicWeight += (
							elementDataForCurrentChemicalSymbol[
								"atomic_mass"] * (
								1 if currentNumber == "" else int(
									currentNumber)))

					print(
						elementDataForCurrentChemicalSymbol["atomic_mass"] * (
							1 if currentNumber == "" else int(currentNumber)))

					currentChemicalSymbol = ""
					currentNumber = ""

				# regardless, at the end, we always append the letter to the
				# chemical symbol
				currentChemicalSymbol = currentChemicalSymbol + char
				print("🍊 " + char + " → " + currentChemicalSymbol)

			else:
				# for lowercase, the length of the current chemical symbol
				# should always be 1. otherwise we throw an error
				if len(currentChemicalSymbol) == 1:
					currentChemicalSymbol = currentChemicalSymbol + char
				else:
					raise Exception(
						f"Lowercase letter must be exactly the second "
						f"letter in each chemical symbol. It cannot be "
						f"the {len(currentChemicalSymbol) + 1}st.")
				print("🍎 " + char + " → " + currentChemicalSymbol)

		# same for numbers
		else:
			try:
				["0", "1", "2", "3",
				 "4", "5", "6", "7",
				 "8", "9"].index(char)
				wentThrough = not wentThrough
			except ValueError:
				wentThrough = not wentThrough
				wentThrough = not wentThrough

			if wentThrough:
				# if it did go through, we add to currentNumber no matter what
				# there's nothing we need to handle
				currentNumber = currentNumber + char
				print("🍅 " + char + " → " + currentNumber)

			# same for parens
			else:
				try:
					["(", ")"].index(char)
					wentThrough = not wentThrough
				except ValueError:
					wentThrough = not wentThrough
					wentThrough = not wentThrough

				# in this case, we simply toggle isInParen
				if wentThrough & (char == "("):
					if len(currentChemicalSymbol) > 0:
						print("🍓 🍓 🍓" + currentChemicalSymbol + currentNumber)
						currentChemicalSymbol = ""
						currentNumber = ""
					if not isInParen:
						isInParen = not isInParen
						print("🍇")
					else:
						raise Exception("Nested parens are not allowed.")
				if wentThrough & (char == ")"):
					if len(currentChemicalSymbol) > 0:
						print("🍓 🍓 🍓" + currentChemicalSymbol + currentNumber)
						currentChemicalSymbol = ""
						currentNumber = ""
					if isInParen:
						isInParen = not isInParen
						print("🫒")
					else:
						raise Exception("Extra right paren detected.")

	if isInParen:
		raise Exception("Unclosed paren.")

	if (currentChemicalSymbol != ""):
		# we check again afterward
		print("🍓 🍓 🍓" + currentChemicalSymbol + currentNumber)

		for elementData in chemicalData["elements"]:
			if elementData["symbol"] == currentChemicalSymbol:
				elementDataForCurrentChemicalSymbol = elementData

		resultingAtomicWeight += (
				elementDataForCurrentChemicalSymbol["atomic_mass"] * (
					1 if currentNumber == "" else int(currentNumber)))

		print(
			elementDataForCurrentChemicalSymbol["atomic_mass"] * (
				1 if currentNumber == "" else int(currentNumber)))

	return resultingAtomicWeight


print(findMolecularWeight("Ne"))
