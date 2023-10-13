from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
pokemon = {i: input().strip() for i in range(1, N + 1)}
pokemon_r = {name: num for num, name in pokemon.items()}

for _ in range(M):
    tmp = input().strip()

    if tmp.isdigit():
        print(pokemon[int(tmp)])
    else:
        print(pokemon_r[tmp])
