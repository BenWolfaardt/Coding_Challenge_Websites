def minimumBribes(q):
    n = len(q)
    if n <= 1:
        return 0
    if n == 2:
        return int(q[-2] > q[-1])

    bribesCounter = 0

    for i in range(n):
        if q[i] - (i + 1) > 2:
            return print("Too chaotic")
        for j in range(max(0, q[i] - 2), i):
            bribesCounter += q[j] > q[i]
    return print(bribesCounter)
            
# TODO write unittests
            
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
        