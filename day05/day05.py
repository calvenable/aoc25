# Advent of Code 2025 - day05
# Run this file with py .\day05\day05.py
import pyperclip

def usefulFunction():
  return True

# Input file parsing code to be reused for both parts
def readFileIntoObject(inputFilePath: str) -> tuple[list[list[int]], list[int]]:
  ranges:list[list[int]] = []
  ingredients:list[int] = []
  readingRanges = True
  with open(inputFilePath, "r") as file:
    for line in file:
      line = line.strip()
      if line == "":
        readingRanges = False
        continue

      if readingRanges:
        ranges.append(list(map(int, line.split('-'))))
      else:
        ingredients.append(int(line))

  return (ranges, ingredients)


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  (freshRanges, ingredientIds) = readFileIntoObject(inputFilePath)

  result = 0
  for id in ingredientIds:
    for range in freshRanges:
      if id >= range[0] and id <= range[1]:
        result += 1
        break

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  (freshRanges, _) = readFileIntoObject(inputFilePath)

  distinctIds = 0
  # Compare each range to every range already processed. If it overlaps,
  # reduce this range. Then count the distinct ids in the reduced range.
  for i in range(len(freshRanges)):
    rangeStart = freshRanges[i][0] # Inclusive lower bound
    rangeEnd = freshRanges[i][1] + 1 # Exclusive upper bound
    for j in range(i):
      otherRangeStart = freshRanges[j][0] # Inclusive lower bound
      otherRangeEnd = freshRanges[j][1] + 1 # Exclusive upper bound
      


  return distinctIds


# Run the code for the specified part ----------------------------------
# answer = partOne("day05/test.txt")
answer = partOne("day05/input.txt")

# answer = partTwo("day05/test.txt")
# answer = partTwo("day05/input.txt")

pyperclip.copy(answer)
print(answer)
