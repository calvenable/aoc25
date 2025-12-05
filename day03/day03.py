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

def maxJoltage(digitString, numBatteries):
  '''Calculate the maximum joltage possible by turning on numBatteries in the provided digitString.'''

# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  banks = []
  with open(inputFilePath, "r") as file:
    for line in file:
      banks.append(line)

  result = 0
  for bank in banks:
    # Find the largest digit that's not at the end
    firstBatteryJoltage = largestDigit(bank[:len(bank)-2])
    # Get its index
    firstBatteryIndex = bank.index(str(firstBatteryJoltage))
    # Get the largest digit after this battery
    secondBatteryJoltage = largestDigit(bank[firstBatteryIndex+1:])
    result += int(str(firstBatteryJoltage) + str(secondBatteryJoltage))

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  return False


# Run the code for the specified part ----------------------------------
# answer = partOne("day03/test.txt")
answer = partOne("day03/input.txt")

# answer = partTwo("day03/test.txt")
# answer = partTwo("day03/input.txt")

pyperclip.copy(answer)
print(answer)
