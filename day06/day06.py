# Advent of Code 2025 - day06
# Run this file with py .\day06\day06.py
import pyperclip
import re
import functools

def readFileIntoObject(inputFilePath: str) -> tuple[list[list[int]],list[str]]:
  numbers = []
  operators = []
  with open(inputFilePath, "r") as file:
    for line in file:
      line = re.split(" +", line.strip())
      if ['*','+'].__contains__(line[0]):
        operators = line
      else:
        numbers.append(list(map(int, line)))
  return (numbers, operators)


def readFileUsingColumnMaths(inputFilePath: str) -> tuple[list[list[int]],list[str]]:
  numberLines = []
  operatorLine = ""

  with open(inputFilePath, "r") as file:
    for line in file:
      line = line.strip("\n")
      if line.startswith(('*','+')):
        # Add a space to overcome the special case of the final operator in the line
        operatorLine = line + " "
      else:
        numberLines.append(line)

  transposedNumberLines = []
  operators = []
  while True:
    firstMatch = re.match("[*+] +", operatorLine)
    if not firstMatch:
      break

    # Use the spaces between the operators to work out how wide each problem column is
    length = len(firstMatch.group(0)) - 1
    operators.append(firstMatch.group(0).strip())
    transposedNumberLines.append([])

    for col in range(length):
      # Iterate through each column in the problem
      newNumber = ""
      for n in range(len(numberLines)):
        # Step down through the rows in this column
        newNumber += numberLines[n][col]
      newNumber = int(newNumber.strip())
      transposedNumberLines[-1].append(newNumber)
    
    # Trim the processed characters from the front of the operator and number lines
    operatorLine = operatorLine[length+1:]
    for n in range(len(numberLines)):
      numberLines[n] = numberLines[n][length+1:]

  return (transposedNumberLines, operators)


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  (operands, operators) = readFileIntoObject(inputFilePath)

  result = 0
  for i in range(len(operators)):
    desiredOperands = []
    for j in range(len(operands)):
      desiredOperands.append(operands[j][i])

    if operators[i] == '*':
      result += functools.reduce(lambda x,y: x * y, desiredOperands)
    else:
      result += functools.reduce(lambda x,y: x + y, desiredOperands)
      
  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  (operands, operators) = readFileUsingColumnMaths(inputFilePath)

  result = 0
  for i in range(len(operators)):
    desiredOperands = operands[i]

    if operators[i] == '*':
      result += functools.reduce(lambda x,y: x * y, desiredOperands)
    else:
      result += functools.reduce(lambda x,y: x + y, desiredOperands)
      
  return result


# Run the code for the specified part ----------------------------------
# answer = partOne("day06/test.txt")
# answer = partOne("day06/input.txt")

# answer = partTwo("day06/test.txt")
answer = partTwo("day06/input.txt")

pyperclip.copy(answer)
print(answer)
