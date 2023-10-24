from sys import stdin
input = stdin.readline

def sol(n):
    global curr
    while curr <= n:
        st.append(curr)
        res.append('+')
        curr += 1
    if st and st[-1] == n:
        st.pop()
        res.append('-')
    else:
        print('NO')
        exit(0)


n = int(input())
curr = 1
st = []
res = []

for _ in range(n):
    num = int(input())
    sol(num)

print(*res, sep='\n')
