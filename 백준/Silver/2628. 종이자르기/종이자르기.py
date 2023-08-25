W, H = map(int, input().split())  # W:width H:height
cut_cnt = int(input())
cut = [list(map(int, input().split())) for _ in range(cut_cnt)]  # 0:가로width, 1:세로height

W_cut = [0, H]
H_cut = [0, W]
for i in cut:
    if i[0] == 0:
        W_cut.append(i[1])
    else:
        H_cut.append(i[1])

W_cut.sort()
H_cut.sort()

max_w = 0
max_h = 0

for i in range(len(W_cut) - 1):
    max_w = max(max_w, W_cut[i + 1] - W_cut[i])
for i in range(len(H_cut) - 1):
    max_h = max(max_h, H_cut[i + 1] - H_cut[i])

print(max_w * max_h)

