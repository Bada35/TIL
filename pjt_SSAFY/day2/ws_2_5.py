import copy

catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성']
]

# deep copy로 얕은 복사의 오류 피하기
backup_catalog = copy.deepcopy(catalog)

# 기존 카탈로그 도서명 수정
catalog[3] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']

# 원본과 백업 비교 후 결과 출력
print('catalog와 backup_catalog를 비교한 결과')


def is_same():  # 기존과 백업을 비교해서 bool값을 반환하는 함수
    for i in range(len(catalog)):
        for j in range(len(catalog[i])):
            if not catalog[i][j] == backup_catalog[i][j]:  # if catalog[i][j] != backup_catalog[i][j] 두개가 다르다면
                return False
    return True


print(is_same())

print('backup_catalog : ')
print(backup_catalog)

print('catalog : ')
print(catalog)
