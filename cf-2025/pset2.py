Score = [3,7,4,3,9,1]
n = 6

# Iterative Solution
def maxScore(i, k): # Returns the max score possible from i...n
    global Score, n
    if i >= n: return 0

    sleep = maxScore(i + 1, 0)
    work = maxScore(i + 1, k + 1) + ((Score[i]) / (2 ** (k)))

    return max(sleep, work)

# DP Solution
Score = [3,7,4,3,9,1]
n = 6

def dp_maxScore():
    max_scores = [[0 for _ in range(n + 1)] for _ in range(n + 1)] # max_scores[i][j] = max possible score from i...n with k = j
    for i in range(n-1, -1, -1): # i
        for j in range(n): # k 
            sleep = max_scores[i+1][0]
            work = max_scores[i+1][j+1] + ((Score[i]) / (2 ** j))
            max_scores[i][j] = max(sleep, work)
    
    print(max_scores[0][0])

def problem3():
    course_list = [[0, 1, 2.5, 3.2, 3.4, 3.45, 3.46, 3.47, 3.48], 
                   [0, 0.5, 1.5, 2.8, 3.6, 3.9, 4.1, 4.15, 4.2], 
                   [0, 0.7, 1.6, 2.0, 2.3, 2.9, 3.4, 3.8, 4.0]]
    def bestStudy(i, H):
        nonlocal course_list

        if H == 0: return 0
        if i >= len(course_list): return 0

        max_score = 0
        for h in range(H + 1):
            if h >= len(course_list[i]): break
            study_for_course_i_for_h_hours = course_list[i][h] + bestStudy(i + 1, H - h)
            max_score = max(max_score, study_for_course_i_for_h_hours)
        
        return max_score

    print("bestStudy():", bestStudy(0, 8))

# subset sum
def problem4():
    arr = [30,50,90,20]

    def subsetSum(i, target):
        nonlocal arr
        if target == 0:
            return 1
        
        if i == len(arr):
            return 0

        take_i = 0
        if arr[i] <= target: 
            take_i = subsetSum(i + 1, target - arr[i])

        leave_i = subsetSum(i + 1, target)

        return take_i + leave_i

    print("subsetSum():", subsetSum(0, 50))

def dp1():
    free_food_dates = {1,2,5,6}
    n = 10

    def schedule(i): # Returns the minimum money you must spend to make sure you have dinner each night from i...n
        nonlocal n
        food = [0] * n
        for i in range(n-2, -1, -1):
            if i in free_food_dates:
                take_free_food = food[i + i]
            

    print(schedule())

if __name__ == '__main__':
    # problem number
    dp1()