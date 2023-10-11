from sys import stdin
input = stdin.readline

while 1:
    s = input()
    if s.rstrip() == '.':  # rstrip()으로 오른쪽 공백(특히 줄바꿈 문자)만 제거
        break

    li = ''.join([ch for ch in s if ch in '()[]'])

    for _ in range(len(li) // 2):
        li = li.replace('()', '')
        li = li.replace('[]', '')

    if len(li):
        print('no')
    else:
        print('yes')
