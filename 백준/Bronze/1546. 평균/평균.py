N = int(input())
scores = list(map(float, input().split()))
print(sum(scores)*100/(max(scores)*N))