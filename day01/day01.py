# Advent of Code 2025 - day01
import math
import pyperclip

def usefulFunction():
  return True


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  result = 0
  dialPosition = 50

  with open(inputFilePath, "r") as file:
    for line in file:
      if (line.startswith("L")):
        dialPosition -= int(line.strip('L'))
      elif (line.startswith("R")):
        dialPosition += int(line.strip('R'))
      dialPosition %= 100

      if (dialPosition == 0):
        result += 1

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  result = 0
  dialPosition = 50

  with open(inputFilePath, "r") as file:
    for line in file:
      change = 0
      if (line.startswith("L")):
        change = int(line.strip('L')) * -1
      elif (line.startswith("R")):
        change = int(line.strip('R'))

      if (abs(change) > 99):
        # Increment result by # of full rotations
        fullRotations = abs(change) // 100
        result += fullRotations
        if (change < 0):
          change += 100 * fullRotations
        else:
          change -= 100 * fullRotations
        
        if (change == 0):
          continue

      initialPosition = dialPosition
      dialPosition += change
      if ((dialPosition < 0 and initialPosition > 0) or dialPosition > 100):
        result += 1

      dialPosition %= 100

      if (dialPosition == 0):
        result += 1

  return result


# Run the code for the specified part ----------------------------------
# answer = partOne("day01/test.txt")
# answer = partOne("day01/input.txt")

# answer = partTwo("day01/test.txt")
answer = partTwo("day01/input.txt")

pyperclip.copy(answer)
print(answer)
