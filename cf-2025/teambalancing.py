import heapq

n = int(input())
set_one = list(map(int, input().split())) # min heap
set_two = list(map(lambda n: -int(n), input().split())) # max heap

heapq.heapify(set_one)
heapq.heapify(set_two)

res = 0

for _ in range(n):
    x, y = heapq.heappop(set_one), -heapq.heappop(set_two)
    res += x * y

print(res)