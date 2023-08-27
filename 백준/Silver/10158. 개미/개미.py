import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

total_dx = p + t
total_dy = q + t

bw_x = total_dx // w
bw_y = total_dy // h

res_x = total_dx % w
res_y = total_dy % h

if bw_x % 2 == 1:
    res_x = w - res_x
if bw_y % 2 == 1:
    res_y = h - res_y

print(res_x, res_y)
