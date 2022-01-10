def minimumBribes(q):
    counter, succesiveCounter = 0, 0
    for i in range(len(q)):
        for j in range(1, len(q)):
            if q[j] <= q[j-1]:
                temp = q[j]
                q[j] = q[j-1]
                q[j-1] = temp
                counter += 1
                succesiveCounter += 1
            else:
                succesiveCounter = 0
            if succesiveCounter >= 3:
                return print("Too chaotic")
    return print(counter)
            
            
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)