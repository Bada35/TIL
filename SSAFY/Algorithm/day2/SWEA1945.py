T = int(input())
DIV = [2, 3, 5, 7, 11]
cnt = 0

for tc in range(1, T + 1):
    number = int(input())
    print(f'#{tc}', end=' ')

    for i in DIV:
        while number % i == 0:
            cnt += 1
            number //= i # while문은 종료조건을 향해가도록..! 이거 빼서 헤맴
        print(cnt, end=' ')
        cnt = 0

    print('') #줄바꿈용. \n 안 넣어도 되는게 print자체에 줄바꿈 있음 =print('\n\,end='')
