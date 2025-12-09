# Advent of Code 2025 - day05
# Run this file with py .\day05\day05.py
import pyperclip

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
  smallestRangeStart = min(list(map(lambda r: r[0], freshRanges)))
  largestRangeEnd = max(list(map(lambda r: r[1], freshRanges)))

  currentId = smallestRangeStart
  while currentId <= largestRangeEnd:
    matchedAnyRange = False

    for r in freshRanges:
      if currentId >= r[0] and currentId <= r[1]:
        matchedAnyRange = True
        distinctIds += r[1] - currentId + 1
        currentId = r[1] + 1
        break

    if not matchedAnyRange:
      # Jump up to the next lowest range start
      currentId = min(list(filter(lambda i: i >= currentId, map(lambda r: r[0], freshRanges))))

  return distinctIds


# Run the code for the specified part ----------------------------------
# answer = partOne("day05/test.txt")
# answer = partOne("day05/input.txt")

# answer = partTwo("day05/test.txt")
answer = partTwo("day05/input.txt")

pyperclip.copy(answer)
print(answer)
