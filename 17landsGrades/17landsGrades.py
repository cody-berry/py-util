# Testing section

# Section 1: Testing mean on a distribution.
import numpy as np
distribution = []
done = False

# Input a distribution
while not done:
    dataPoint = input("Enter a number: ")
    try:
        dataPoint = float(dataPoint)
        distribution.append(dataPoint)
        done = True
    except:
        print("Invalid number")

done = False

while not done:
    dataPoint = input("Enter a number (or enter a non-number to say \"done\"): ")
    try:
        dataPoint = float(dataPoint)
        distribution.append(dataPoint)
        print(distribution)
    except:
        done = True


print(distribution)
mean = 0
for dataPoint in distribution:
    mean += dataPoint
mean /= len(distribution)

print(mean)
print(np.mean(distribution))
