res = []
for _ in range(int(input())):
    n, m, k = tuple(map(int, input().split()))

    if n == 1:
        if (m == 0 and k > 1):
            res.append("YES")
        else:
            res.append("NO")
        continue

    max_nodes = n * (n - 1) // 2
    if m < n - 1 or max_nodes < m:
        res.append("NO")
        continue

    if k <= 2:
        res.append("NO")
    elif k == 3:
        res.append("YES" if m == max_nodes else "NO")
    else:
        res.append("YES")

for line in res:
    print(line)