# Advent of Code 2025 - day07
# Run this file with py .\day07\day07.py
import pyperclip
from collections import defaultdict

# Input file parsing code to be reused for both parts
def readFileIntoObject(inputFilePath) -> list[str]:
  myObject = []
  with open(inputFilePath, "r") as file:
    for line in file:
      myObject.append(line)

  return myObject


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  manifoldMap = readFileIntoObject(inputFilePath)

  result = 0
  beamLocations:set[tuple[int,int]] = set()
  beamLocations.add((manifoldMap[0].index('S'), 0))

  while len(beamLocations) > 0:
    newBeamLocations:set[tuple[int,int]] = set()
    for beam in beamLocations:
      if beam[1] < len(manifoldMap) - 1:
        # The beam is on the map and has space to move down
        if manifoldMap[beam[1] + 1][beam[0]] == '.':
          newBeamLocations.add((beam[0], beam[1] + 1))
        elif manifoldMap[beam[1]+1][beam[0]] == '^':
          result += 1
          if beam[0] > 0:
            newBeamLocations.add((beam[0] - 1, beam[1] + 1))
          if beam[0] < len(manifoldMap[0]) - 1:
            newBeamLocations.add((beam[0] + 1, beam[1] + 1))

    beamLocations = newBeamLocations

  return result

# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  manifoldMap = readFileIntoObject(inputFilePath)

  # Record how many "timeline" beams there are at each map location
  beamLocations:defaultdict[tuple[int,int],int] = defaultdict(int)
  beamLocations[(manifoldMap[0].index('S'), 0)] = 1

  while len(beamLocations) > 0:
    newBeamLocations:defaultdict[tuple[int,int],int] = defaultdict(int)
    for beam in beamLocations.keys():
      if beam[1] < len(manifoldMap) - 1:
        # The beam(s) are on the map and have space to move down
        if manifoldMap[beam[1] + 1][beam[0]] == '.':
          newBeamLocations[(beam[0], beam[1] + 1)] += beamLocations[beam]
        elif manifoldMap[beam[1]+1][beam[0]] == '^':
          if beam[0] > 0:
            newBeamLocations[(beam[0] - 1, beam[1] + 1)] += beamLocations[beam]
          if beam[0] < len(manifoldMap[0]) - 1:
            newBeamLocations[(beam[0] + 1, beam[1] + 1)] += beamLocations[beam]
            
    if len(newBeamLocations) == 0:
      return sum(beamLocations.values())
    beamLocations = newBeamLocations

  return 0


# Run the code for the specified part ----------------------------------
# answer = partOne("day07/test.txt")
# answer = partOne("day07/input.txt")

# answer = partTwo("day07/test.txt")
answer = partTwo("day07/input.txt")

pyperclip.copy(answer)
print(answer)
