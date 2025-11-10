res = []

for _ in range(int(input())):
    arg = input()
    a, operator, b = int(arg[0]), arg[1], int(arg[2])
    
    if a < b:
        operator = "<"
    elif a > b:
        operator = ">"
    else:
        operator = "="
    
    res.append(str(a)+operator+str(b))

for line in res:
    print(line)