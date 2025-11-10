res = []

n = int(input())

bus_stop = 0
for _ in range(n):
    event = input().split()
    if event[0] == "B":
        seats = int(event[1])
        if bus_stop >= seats:
            bus_stop -= seats
            res.append("NO")
        else:
            bus_stop = 0
            res.append("YES")

    elif event[0] == "P":
        bus_stop += int(event[1])

for line in res:
    print(line)