L = int(input())
s = input()
print(sum([(ord(s[i]) - 96) * (31**i) for i in range(L)]) % 1234567891)