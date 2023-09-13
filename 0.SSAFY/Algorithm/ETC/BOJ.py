from itertools import combinations
import sys
input = sys.stdin.readline


def greedy(k, words, u):  # n자리일때 제일 많이 만들 수 있는게 n+1자리일때 제일 많이 만들 수 있는 조합에 포함되지 않을까?
    while k:
        max_char = ''
        max_cnt = float('-inf')
        st = [e for word in words for e in word]
        for ch in u:
            if st.count(ch) > max_cnt:
                max_cnt = st.count(ch)
                max_char = ch
        for s in words:
            s.discard(max_char)
        k -= 1
    cnt = 0
    for word in words:
        if not word:
            cnt += 1
    print(cnt)


def brute_force(k, words, u):  # U안에서 K길이만큼의 부분집합을 다 만들어서 걍 다 비교(돌아갈까?? => 5% 안 돌아간다)
    max_cnt = float('-inf')
    for subset in combinations(u, k):
        cnt = 0
        for word in words:
            if word.issubset(subset):
                cnt += 1
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)


def init():
    N, K = map(int, input().split())  # N:단어수(자연수 <= 50)  K:글자수(0 or 자연수 <= 26)

    if K < 5:
        print(0)
        exit(0)
    else:
        K -= 5

    s = 'antic'
    words = []

    for i in range(N):
        tmp = list(input().strip())
        # tmp = tmp[4:len(tmp)-4]  굳이 자를필요 없네
        w = {w for w in tmp if w not in s}
        if len(w) <= K:  # 애초에 K보다 길이 긴 건 고려할 필요 X => 이렇게 해도 brute-force는 안됨
            words.append(w)
    U = set()
    for s in words:
        U = U.union(s)
    return K, words, U


'''
K: 1
words: [{'r'}, {'l', 'o', 'e', 'h'}, {'r'}]
U: {'l', 'r', 'e', 'h', 'o'}
'''
K, words, U = init()
brute_force(K, words, U)
# greedy(K, words, U)
