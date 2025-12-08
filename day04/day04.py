# Advent of Code 2025 - day04
# Run this file with py .\day04\day04.py
import pyperclip

def replaceAccessibleRollsWithX(forkliftMap):
  '''Replace all rolls with less than 4 "@" neighbours with the "x" character. Returns the modified array.'''
  for y in range(len(forkliftMap)):
    newRow = ''
    for x in range(len(forkliftMap[0])):
      if forkliftMap[y][x] == '@':
        adjacentRolls = 0
        for xStep in range(-1, 2):
          for yStep in range(-1, 2):
            if xStep == 0 and yStep == 0:
              continue
            if x + xStep < len(forkliftMap[y]) and x + xStep >= 0 and y + yStep < len(forkliftMap) and y + yStep >= 0:
              if forkliftMap[y + yStep][x + xStep] == '@' or forkliftMap[y + yStep][x + xStep] == 'x':
                adjacentRolls += 1
        
        if adjacentRolls < 4:
          newRow += 'x'
        else:
          newRow += '@'
      else:
        newRow += '.'
    forkliftMap[y] = newRow

  return forkliftMap

# Input file parsing code to be reused for both parts
def readFileIntoObject(inputFilePath):
  myObject = []
  with open(inputFilePath, "r") as file:
    for line in file:
      myObject.append(line.strip())

  return myObject


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  forkliftMap = readFileIntoObject(inputFilePath)

  result = 0

  for y in range(len(forkliftMap)):
    for x in range(len(forkliftMap[0])):
      if forkliftMap[y][x] == '@':
        adjacentRolls = 0
        for xStep in range(-1, 2):
          for yStep in range(-1, 2):
            if xStep == 0 and yStep == 0:
              continue
            if x + xStep < len(forkliftMap[y]) and x + xStep >= 0 and y + yStep < len(forkliftMap) and y + yStep >= 0:
              if forkliftMap[y + yStep][x + xStep] == '@':
                adjacentRolls += 1
        
        if adjacentRolls < 4:
          result += 1

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  forkliftMap = readFileIntoObject(inputFilePath)
  rollsRemoved = 0

  while True:
    prevRollsRemoved = rollsRemoved
    forkliftMap = replaceAccessibleRollsWithX(forkliftMap)

    # Count and remove all accessible rolls
    for l in range(len(forkliftMap)):
      rollsRemoved += forkliftMap[l].count('x')
      forkliftMap[l] = forkliftMap[l].replace('x', '.')
    
    # Run until no more rolls can be removed
    if rollsRemoved == prevRollsRemoved:
      break

  return rollsRemoved

  


# Run the code for the specified part ----------------------------------
# answer = partOne("day04/test.txt")
# answer = partOne("day04/input.txt")

# answer = partTwo("day04/test.txt")
answer = partTwo("day04/input.txt")

pyperclip.copy(answer)
print(answer)
