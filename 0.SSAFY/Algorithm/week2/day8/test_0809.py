# li = [1, 2, 3, 4]
# if li[1:3] == [1, 3]:
#     print(1)
# print(li[1:3])

def main():
    def a():
        return 1
    def b():
        return 2
    def c():
        return a() + b()
    print(c())

main()