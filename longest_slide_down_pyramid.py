#    /3/
#   \7\ 4 
#  2 \4\ 6 
# 8 5 \9\ 3
#Given a pyramid find the largest sum sliding downwards
#E.g for the pyramid above this should return 3+7+4+9 = 23

def longest_slide_down(pyramid):
    for i in range(len(pyramid) - 1, 0, -1):
        btm = pyramid[i]
        top = pyramid[i-1]
        pyramid[i-1] = slide_up(btm, top)
    return pyramid[0][0]

def slide_up(btm, top):
    for i,n in enumerate(top):
        top[i] += max(btm[i],btm[i+1])
    return top

array = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20,  4, 82, 47, 65],
        [19,  1, 23, 75,  3, 34],
        [88,  2, 77, 73,  7, 63, 67],
        [99, 65,  4, 28,  6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
        ]
print(longest_slide_down(array))

