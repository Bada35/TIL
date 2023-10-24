h, m = map(int, input().split())
t = int(input())
time = 60 * h + m + t
if time >= 60*24:
    time -= 60*24
print(time//60, time%60)