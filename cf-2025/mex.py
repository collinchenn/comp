def solve(arr, k, n):
    count = 0
    excluded = [0] * (n + 1)
    for num in arr:
        if num == k:
            count += 1
        excluded[num] =  1
    total_excluded = sum(1 for i in range(k) if excluded[i] == 0)
    return max(count, total_excluded)

res = []

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res.append(solve(arr, k, n))

for num in res:
    print(num)