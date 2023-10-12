def sol(n):
    if not st:
        st.append(nums.pop())
        res.append('+')
    if n > st[-1]:
        while st[-1] != n:
            if not nums:
                print('NO')
                exit(0)
            st.append(nums.pop())
            res.append('+')
        st.pop()
        res.append('-')
    elif n == st[-1]:
        res.append('-')
        st.pop()
    else:
        print('NO')
        exit(0)


n = int(input())
nums = [i for i in range(n, 1, -1)]
res = ['+']
st = [1]
for i in range(n):
    tmp = int(input())
    sol(tmp)

print(*res, sep='\n')