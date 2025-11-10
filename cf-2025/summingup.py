n, m = map(int, input().split())

#1 2 4
#8 16 32

#1 3 7
#8 24 56

mat = []

for _ in range(n):
    input_row = list(map(int, input().split()))
    mat.append(input_row)

prefix_sum = [row[:] for row in mat]

for i in range(len(prefix_sum)):
    for j in range(1, len(prefix_sum[0])):
        prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i][j]

res = []

def solve(i, j, x, y):
    
    print(i,j,x,y)
    total = 0

    for row in range(i, x+1):
        pass
    
    print(total)
    res.append(total)

for _ in range(int(input())):
    i, j, x, y = tuple(x - 1 for x in list(map(int, input().split())))
    solve(i, j, x, y)

###########################################################

for num in res:
    print(num)