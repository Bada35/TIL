s = list(input())
s = [ord(i) - 32 if ord(i) > 96 else ord(i) for i in s]
d = {i:s.count(i) for i in set(s)}
re = [key for key, value in d.items() if value == max(d.values())]

if len(re) == 1:
    print(chr(*re))
else:
    print('?')