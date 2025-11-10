input_size = int(input())

res = []

def solve(n, arr):
    dp = [0] * (n)
    dp[n - 1] = arr[n - 1]

    # dp = [7,6,3,2,3]

    for i in range(n - 2, -1, -1):
        if i + arr[i] < n:
            dp[i] = max(arr[i] + dp[i + arr[i]], dp[i] + arr[i])
        else:
            dp[i] = dp[i] + arr[i]

    return max(dp)

for _ in range(input_size):
    n = int(input())
    arr = list(map(int, input().split()))
    res.append(solve(n, arr))

for num in res:
    print(num)