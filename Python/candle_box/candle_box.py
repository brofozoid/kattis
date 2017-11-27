import sys, io

file = open('test.txt')  # A text file we'll use as stdin
sys.stdin = file  # Assign stdin the file object, so it will read from it
array = []

for line in sys.stdin:
    array.append(line.strip())

diff_in_age = array[0]
ritas = array[1]
theos = array[2]

# Rita
# Started doing it from 4yr
#
#
# Theo
# Started from 3yrs




diff_in_age = 2  # so 30/28, 28/26 etc
ritas = 26  # Number of candles in Rita's box
theos = 8  # Number of candles in Rita's box

