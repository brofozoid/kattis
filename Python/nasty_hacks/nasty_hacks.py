total = int(input())
i = 0
while i < total:
    scenario = input().split()
    r = int(scenario[0])
    e = int(scenario[1])
    c = int(scenario[2])
    ec = e - c
    if r > ec:
        print("do not advertise")
    elif r == ec:
        print("does not matter")
    else:
        print("advertise")
    i += 1
