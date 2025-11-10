import math

input_size = int(input())

res = []

def solve(arr, n, k):
    # solve k = 4 seperately? lol
    closest_mod = k
    if k == 4:
        evens = 0
        odds = 0
        for num in arr:
            if num % 2 == 0:
                evens += 1
            else:
                odds += 1
        if evens >= 2: closest_mod = 0
        if evens == 1: closest_mod = 1
        if evens == 0: closest_mod = 2

    for num in arr:
        closest_upper_k = math.ceil(num / k) * k
        closest_mod = min(closest_mod, closest_upper_k - num)

    return closest_mod

for _ in range(input_size):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res.append(solve(arr, n, k))

for num in res:
    print(num)