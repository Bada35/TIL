from sys import stdin
input = stdin.readline

st = []
for _ in range(int(input())):
    tmp = int(input())
    if not tmp:
        st.pop()
    else:
        st.append(tmp)
print(sum(st))