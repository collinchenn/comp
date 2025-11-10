input_n = int(input())

res = []

def solve(n, arr):
    max_val = arr[0]
    max_indicies = []
    for i, num in enumerate(arr):
        if num > max_val:
            max_val = arr[i]
            max_indicies = [i]
        if num == max_val:
            max_indicies.append(i)

    max_score = 0
    for index in max_indicies:
        score = max_val + 1
        score += (index) // 2
        score += (n - (index + 1)) // 2
        max_score = max(max_score, score)

    return max_score

for _ in range(input_n):
    n = int(input())
    arr = list(map(int, input().split()))
    res.append(solve(n, arr))

for num in res:
    print(num)