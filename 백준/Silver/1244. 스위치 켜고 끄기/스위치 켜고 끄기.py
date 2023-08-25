def on_off(s):  # 스위치 번호(인덱스)로 받기
    if switch[s]:
        switch[s] = 0
    else:
        switch[s] = 1


def switching(s, n):
    if s == 1:  # 남자면
        for i in range(n-1, T, n):
            on_off(i)
    else:  # 여자면
        on_off(n - 1)
        i = 1
        while 1:
            if switch[n-1-i:n-1] == switch[n+i-1:n-1:-1]:
                on_off(n-1-i)
                on_off(n+i-1)
                i += 1
            else:
                break


T = int(input())  # 스위치 개수
switch = list(map(int, input().split()))
n = int(input())  # 학생 수
for _ in range(n):
    s, sw_n = map(int, input().split())  # 남학생 s=1, 여학생 s=2
    switching(s, sw_n)

for i in range(0, len(switch), 20):
    print(*switch[i:i+20])

