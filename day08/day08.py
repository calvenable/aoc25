# Advent of Code 2025 - day08
# Run this file with py .\day08\day08.py
import pyperclip
from math import sqrt,pow

from UnionFind import UnionFind
Point = tuple[int,int,int]

def distanceBetween(a:Point, b:Point) -> float:
  '''Returns the pythagorean straight-line distance between two points in 3D space.'''
  return sqrt(pow(b[0]-a[0], 2) + pow(b[1]-a[1], 2) + pow(b[2]-a[2], 2))

# Input file parsing code to be reused for both parts
def readFileIntoObject(inputFilePath:str) -> list[Point]:
  myObject:list[Point] = []
  with open(inputFilePath, "r") as file:
    for line in file:
      numbers = list(map(int,line.strip().split(',')))
      myObject.append((numbers[0],numbers[1],numbers[2]))

  return myObject


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath, numConnections):
  boxes = readFileIntoObject(inputFilePath)
  distancesBetween:dict[frozenset[Point,Point], float] = dict()

  for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
      distancesBetween[frozenset([boxes[i], boxes[j]])] = distanceBetween(boxes[i], boxes[j])

  distancesBetween = dict(sorted(distancesBetween.items(), key=lambda item: item[1]))

  boxCircuits = UnionFind[Point](boxes)
  
  # Make <numConnections> many new connections between boxes
  for i in range(numConnections):
    newConnection = next(iter(distancesBetween.keys()))
    firstConnectedBox, secondConnectedBox = newConnection
    del distancesBetween[newConnection]
    boxCircuits.union(firstConnectedBox, secondConnectedBox)

  circuitSizes = sorted(map(lambda c: boxCircuits.size(c), boxCircuits.list()), reverse=True)
  return circuitSizes[0] * circuitSizes[1] * circuitSizes[2]


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  boxes = readFileIntoObject(inputFilePath)
  distancesBetween:dict[frozenset[Point,Point], float] = dict()

  for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
      distancesBetween[frozenset([boxes[i], boxes[j]])] = distanceBetween(boxes[i], boxes[j])

  distancesBetween = dict(sorted(distancesBetween.items(), key=lambda item: item[1]))

  boxCircuits = UnionFind[Point](boxes)
  
  while True:
    newConnection = next(iter(distancesBetween.keys()))
    firstConnectedBox, secondConnectedBox = newConnection
    del distancesBetween[newConnection]
    boxCircuits.union(firstConnectedBox, secondConnectedBox)
    if len(boxCircuits) == 1:
      return firstConnectedBox[0] * secondConnectedBox[0]


# Run the code for the specified part ----------------------------------
# answer = partOne("day08/test.txt", 10)
# answer = partOne("day08/input.txt", 1000)

# answer = partTwo("day08/test.txt")
answer = partTwo("day08/input.txt")

pyperclip.copy(answer)
print(answer)
