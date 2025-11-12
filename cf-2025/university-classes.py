def solve():
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(input())
    
    maximum_classes = 0
    for i in range(7):
        classes = 0
        for j in range(n):
            if mat[j][i] == "1":
                classes += 1
        maximum_classes = max(maximum_classes, classes)
    
    return maximum_classes

if __name__ == '__main__':
    print(solve())