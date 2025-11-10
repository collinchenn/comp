n = int(input())

a = b = c = n 
planks = 0
while a or b or c:
    plank = 60

    while plank >= 25 and a > 0:
        a -= 1
        plank -= 25

    while plank >= 21 and b > 0:
        b -= 1
        plank -= 21

    while plank >= 18 and c > 0:
        c -= 1
        plank -= 18

    planks += 1

print(planks)
