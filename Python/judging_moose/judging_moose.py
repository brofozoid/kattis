line = input()
info = line.split()
left = int(info[0])
right = int(info[1])

if left == 0 and right == 0:
    print('Not a moose')
elif left == right:
    print('Even {}'.format(left * 2))
elif left > right:
    print('Odd {}'.format(left * 2))
elif right > left:
    print('Odd {}'.format(right * 2))
