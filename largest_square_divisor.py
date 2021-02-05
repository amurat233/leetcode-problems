def largest_divisor(n, start):
    largest = start**2
    largest_i = start
    if n
    for i in range(start+1, int((n//2)**0.5 + 1)):
        if n%i**2 == 0 and i**2 >= largest:
            largest = i**2
            largest_i = i
    return largest, largest_i

def s(N):
    start = 1
    for i in range(1, N+1):
        pass

print(largest_divisor(4, 1))