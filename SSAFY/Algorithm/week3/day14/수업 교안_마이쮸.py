def mychew(n):
    while 1:
        n -= Q[0][1]
        if n <= 0:
            return Q[0][0]
        print(Q)
        Q.append(Q.pop())
        Q.append(P.pop(0))


P = [[i, 1] for i in range(1, 11)]
Q = [P.pop(0)]
print(mychew(20))
