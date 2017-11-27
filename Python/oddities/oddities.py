import sys

sys.stdin = open('test.txt')

number_of_tests = int(input())
i = 0
while i < number_of_tests:
    number = int(input())
    if number % 2:
        print('{} is odd'.format(number))
    else:
        print('{} is even'.format(number))
    i += 1
