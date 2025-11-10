from math import sqrt

lower, upper = map(int, input().split())

interval_len = upper - lower + 1
no_squares = [1] * interval_len

largest_root = int(sqrt(upper))

for r in range(2, largest_root + 1):
    square = r * r
    start = ((lower + square - 1) // square) * square
    
    for num in range(start, upper + 1, square):
        no_squares[num - lower] = 0

print(sum(no_squares))