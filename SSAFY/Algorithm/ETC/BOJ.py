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
        max_len = min(n-1, T - n)
        print(max_len)
        while max_len:
            if switch[n - 1 - max_len:n - 1] == switch[n - 1 + max_len:n - 1:-1]:
                for i in range(n - 1 - max_len, n - 1 + max_len + 1):
                    on_off(i)
                break
            max_len -= 1


T = int(input())  # 스위치 개수
switch = list(map(int, input().split()))
n = int(input())  # 학생 수
for _ in range(n):
    s, sw_n = map(int, input().split())  # 남학생 s=1, 여학생 s=2
    switching(s, sw_n)

print(*switch)

