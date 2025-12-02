# Advent of Code 2025 - day01
import pyperclip

def usefulFunction():
  return True


# Code for Part One ----------------------------------------------------
def partOne(inputFilePath):
  result = 0
  dialPosition = 50

  with open(inputFilePath, "r") as file:
    for line in file:
      if (line.startswith("L")):
        dialPosition -= int(line.strip('L'))
      elif (line.startswith("R")):
        dialPosition += int(line.strip('R'))
      dialPosition %= 100

      if (dialPosition == 0):
        result += 1

  return result


# Code for Part Two ----------------------------------------------------
def partTwo(inputFilePath):
  return False


# Run the code for the specified part ----------------------------------
# answer = partOne("day01/test.txt")
answer = partOne("day01/input.txt")

# answer = partTwo("day01/test.txt")
# answer = partTwo("day01/input.txt")

pyperclip.copy(answer)
print(answer)
