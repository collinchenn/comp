permutations = []

n = 8

def permute(permutation, used: set):
    if len(permutation) == n:
        permutations.append(permutation[:])
    
    for i in range(1, n + 1):
        if i not in used:
            permutation.append(i)
            used.add(i)
            permute(permutation, used)
            used.remove(i)
            permutation.pop()
    

permute([], set())

print(permutations)
# 1 8 2 