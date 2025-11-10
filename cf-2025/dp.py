line = [1,0,0,0,1,1,3,4,0,1]
n = len(line)

def skittles(i, current):
    if i >= n:
        return 0
    
    dont_trade = skittles(i + 1, current)
    delta = 1 if current == line[i] else -1
    trade = delta + skittles(i + 1, line[i])

    return max(trade, dont_trade)

def dp_skittles(i, current):
    max_score = [[0 for _ in range(5)] for _ in range(n+1)]
    
    for k in range(5):
        for j in range(n-1, -1, -1):
            dont_trade = max_score[j + 1][k]
            delta = 1 if k == line[j] else -1
            trade = delta + max_score[j + 1][line[j]]
            max_score[j][k] = max(dont_trade, trade)
    
    return max_score

res = dp_skittles(0, 2)

for row in res:
    print(row)
