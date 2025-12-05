# Advent of Code 2025 - [DAY]
# Run this file with py .\[DAY]\[DAY].py
import pyperclip

def usefulFunction():
  return True

# Input file parsing code to be reused for both parts
def readFileIntoObject(inputFilePath):
  myObject = []
  with open(inputFilePath, "r") as file:
    for line in file:
      myObject.append(line)

  return myObject


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  myObject = readFileIntoObject(inputFilePath)

  result = 0


  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  myObject = readFileIntoObject(inputFilePath)
  return False


# Run the code for the specified part ----------------------------------
answer = partOne("[DAY]/test.txt")
# answer = partOne("[DAY]/input.txt")

# answer = partTwo("[DAY]/test.txt")
# answer = partTwo("[DAY]/input.txt")

pyperclip.copy(answer)
print(answer)