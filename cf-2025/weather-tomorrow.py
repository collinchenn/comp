def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    diff = arr[1] - arr[0]
    for i in range(2, n):
        if arr[i] - arr[i-1] == diff:
            continue
        
        else:
            return arr[n-1]
    
    return arr[n-1] + diff

print(solve())