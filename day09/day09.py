# Advent of Code 2025 - day09
# Run this file with py .\day09\day09.py
import pyperclip

Point = tuple[int,int]

def rectangleArea(a:Point, b:Point) -> int:
  return (1 + abs(abs(a[0]) - abs(b[0]))) * (1 + abs(abs(a[1]) - abs(b[1])))

# Input file parsing code to be reused for both parts
def readFileIntoObject(inputFilePath:str) -> list[Point]:
  myObject:list[Point] = []
  with open(inputFilePath, "r") as file:
    for line in file:
      numbers = list(map(int,line.strip().split(',')))
      myObject.append((numbers[0],numbers[1]))

  return myObject


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  redTiles = readFileIntoObject(inputFilePath)
  biggestArea = 0

  for i in range(len(redTiles)):
    for j in range(i+1, len(redTiles)):
      area = rectangleArea(redTiles[i], redTiles[j])
      if area > biggestArea:
        biggestArea = area
  
  return biggestArea

# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  myObject = readFileIntoObject(inputFilePath)
  return False


# Run the code for the specified part ----------------------------------
# answer = partOne("day09/test.txt")
answer = partOne("day09/input.txt")

# answer = partTwo("day09/test.txt")
# answer = partTwo("day09/input.txt")

pyperclip.copy(answer)
print(answer)
