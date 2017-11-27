import sys, io

file = open('test.txt')  # A text file we'll use as stdin
sys.stdin = file  # Assign stdin the file object, so it will read from it
line = input()  # Read a line from file
print(line)
line = input()
print(line)
line = input()
print(line)
line = input()
sys.stdin = sys.__stdin__  # Reset the stdin to its default value
