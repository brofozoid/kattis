number_of_tests = int(input())
i = 0
while i < number_of_tests:
    print('Test {}'.format(i + 1))
    rows = int(input().split()[0])
    j = 0
    lines = []
    i += 1
    while j < rows:
        line = input()
        lines.append(line)
        j += 1
    lines.reverse()
    for line in lines:
        print(line[::-1])
