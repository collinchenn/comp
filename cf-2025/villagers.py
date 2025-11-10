import heapq

res = []

for _ in range(int(input())):
    cost = 0

    n = int(input())
    max_heap = list(map(lambda n: -int(n), input().split()))
    max_heap.append(0)
    heapq.heapify(max_heap)

    while len(max_heap) >= 2:
        g_i = -heapq.heappop(max_heap)
        g_j = -heapq.heappop(max_heap)

        cost += max(g_i, g_j)
    
    res.append(cost)

for num in res:
    print(num)