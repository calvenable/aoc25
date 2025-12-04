# Advent of Code 2025 - day02
import pyperclip
import re

def isValid(id):
  if (re.match('^(\\d+)\\1$', str(id)) is None):
    return True
  return False

def isValidPart2(id):
  if (re.match('^(\\d+)\\1+$', str(id)) is None):
    return True
  return False


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  with open(inputFilePath, "r") as file:
    for line in file:
      # Produces a list of lists like [[11, 22], [95, 115]...]
      idRanges = list(map(lambda range : range.split('-'), line.split(',')))
  
  result = 0

  for idRange in idRanges:
    rangeStart = int(idRange[0])
    rangeEnd = int(idRange[1])
    for i in range(rangeStart, rangeEnd + 1):
      if (not isValid(i)):
        result += i

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  with open(inputFilePath, "r") as file:
    for line in file:
      # Produces a list of lists like [[11, 22], [95, 115]...]
      idRanges = list(map(lambda range : range.split('-'), line.split(',')))
  
  result = 0

  for idRange in idRanges:
    rangeStart = int(idRange[0])
    rangeEnd = int(idRange[1])
    for i in range(rangeStart, rangeEnd + 1):
      if (not isValidPart2(i)):
        result += i

  return result


# Run the code for the specified part ----------------------------------
# answer = partOne("day02/test.txt")
# answer = partOne("day02/input.txt")

# answer = partTwo("day02/test.txt")
answer = partTwo("day02/input.txt")

pyperclip.copy(answer)
print(answer)
