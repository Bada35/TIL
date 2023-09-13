h, m = map(int, input().split())
time = 60 * h + m - 45
if time < 0:
    time += 60*24
print(time//60, time%60)