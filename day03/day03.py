# Advent of Code 2025 - day03
# Run this file with py .\day03\day03.py
import pyperclip

def largestDigit(digitString):
  largest = 0
  if len(digitString) == 0:
    return 0
  for i in range(len(digitString)):
    if digitString[i].isdigit() and int(digitString[i]) > largest:
      largest = int(digitString[i])
  return largest

def maxJoltage(digitString: str, numBatteries: int) -> str:
  '''Calculate the maximum joltage possible by turning on numBatteries in the provided digitString. Returns a string.'''
  if numBatteries == 0:
    return ""
  
  # Cut off (numBatteries-1) digits from the end
  firstBatteryJoltage = largestDigit(digitString[:len(digitString)-(numBatteries-1)])
  firstBatteryIndex = digitString.index(str(firstBatteryJoltage))
  return str(firstBatteryJoltage) + maxJoltage(digitString[firstBatteryIndex + 1:], numBatteries - 1)

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  banks = []
  with open(inputFilePath, "r") as file:
    for line in file:
      banks.append(line.strip())

  result = 0
  for bank in banks:
    mJ = maxJoltage(bank, 2)
    result += int(mJ)

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  banks = []
  with open(inputFilePath, "r") as file:
    for line in file:
      banks.append(line.strip())

  result = 0
  for bank in banks:
    mJ = maxJoltage(bank, 12)
    result += int(mJ)

  return result


# Run the code for the specified part ----------------------------------
# answer = partOne("day03/test.txt")
# answer = partOne("day03/input.txt")

# answer = partTwo("day03/test.txt")
answer = partTwo("day03/input.txt")

pyperclip.copy(answer)
print(answer)
