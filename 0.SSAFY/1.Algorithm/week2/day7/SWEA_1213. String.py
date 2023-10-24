for _ in range(10):
    tc = int(input())
    F = input()
    st = input()
    cnt = 0

    while len(st) >= len(F):
        if st.find(F) == -1:
            break
        cnt += 1
        st = st[st.find(F)+len(F):]
    print(f'{tc} {cnt}')

# # 현중 코드
# for _ in range(10):
#     t = input()
#     word = input()
#     data = input()
#     sol = data.count(word)
#     print(f'#{t} {sol}')