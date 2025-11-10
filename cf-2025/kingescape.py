n = int(input())
alice, bob, target = None, None, None

alice = tuple(map(int, input().split())) # x, y
bob = tuple(map(int, input().split()))
target = tuple(map(int, input().split()))

invalid = set()

# eliminate red spots
for i in range(1, n + 1): # vertical
    invalid.add((alice[0], i))

for i in range(1, n + 1): # horizontal
    invalid.add((i, alice[1]))

# get diagonals

for i in range(1, n):
    invalid.add((alice[0] - i, alice[1] - i))
    invalid.add((alice[0] + i, alice[1] - i))
    invalid.add((alice[0] - i, alice[1] + i))
    invalid.add((alice[0] + i, alice[1] + i))

if target in invalid:
    print("NO")
else:
    # check if they're in the same quadrant
    king_quadrant, target_quadrant = None, None
    if bob[0] > alice[0] and bob[1] > alice[1]:
        king_quadrant = 1
    elif bob[0] < alice[0] and bob[1] > alice[1]:
        king_quadrant = 2
    elif bob[0] < alice[0] and bob[1] < alice[1]:
        king_quadrant = 3
    else:
        king_quadrant = 4
    
    if target[0] > alice[0] and target[1] > alice[1]:
        target_quadrant = 1
    elif target[0] < alice[0] and target[1] > alice[1]:
        target_quadrant = 2
    elif target[0] < alice[0] and target[1] < alice[1]:
        target_quadrant = 3
    else:
        target_quadrant = 4
    
    if king_quadrant == target_quadrant:
        print("YES")
    else:
        print("NO")