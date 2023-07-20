dic = {}
j = 0
kor = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

for i in kor:
    dic[j] = i
    j += 1

def Korean_number(num):
    print(dic[num])

Korean_number(5)