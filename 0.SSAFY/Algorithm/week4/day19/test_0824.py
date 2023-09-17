
decode = {13: 0, 25: 1, 19: 2, 61: 3, 35: 4, 49: 5, 47: 6, 59: 7, 55: 8, 11: 9}

s = '163589926345A30'


def read_code(cd):
    cd = ''.join(format(int(c, 16), '04b') for c in cd)  # 2진수로 변환
    return cd


i = read_code(s)
print(i, len(i))

def str2code(cd):  # 이진코드를 십진수로
    lst = []
    l = 56 * ((cd.rfind('1') - cd.find('1')) // 56 + 1)
    cd = cd[cd.find('1'):cd.rfind('1')+1]
    print(cd, len(cd))
    cd = cd.zfill(l)
    cd = cd[::l//56]
    print(cd)
    for i in range(0, 56, 7):
        lst.append(decode[int(cd[i:i + 7], 2)])  # 해독해서 append
    return lst

print(str2code(i))

# print(len('00110010011001011000100100110111011010111100110010010011'))

# cd = ''.join(format(int(c, 16), '04b') for c in 'C99624DDAF324C')  # 2진수로 변환
# print(cd, len(cd))

# print(sum([1, 8, 6, 9, 4, 9, 5, 6]))

#




# if '163589926345A3003746EDE8B626468' in cd:
#     print('hihi')
#     id = cd.index('163589926345A3003746EDE8B626468')
#     cd.pop(id)
#     cd.insert(id, '163589926345A3')
#     cd.insert(id + 1, '3746EDE8B626468')
#
# if '349BB6EDD88B7A0001E667F9E7E07987861E1819E0678' in cd:
#     print('hihi')
#     id = cd.index('349BB6EDD88B7A0001E667F9E7E07987861E1819E0678')
#     cd.pop(id)
#     cd.insert(id, '349BB6EDD88B7A')
#     cd.insert(id + 1, '1E667F9E7E07987861E1819E0678')
#
# if '376EED18D1AC4580078618799FE1E19F9E07987861878' in cd:
#     print('hihi')
#     id = cd.index('376EED18D1AC4580078618799FE1E19F9E07987861878')
#     cd.pop(id)
#     cd.insert(id, '376EED18D1AC458')
#     cd.insert(id + 1, '78618799FE1E19F9E07987861878')
#
# if '71FFE3F1FF007E38FC01C7E3FE3F1FF0071F803F1C000CF0F0CF033C0CCFF3F3C0CF03CC' in cd:
#     print('hihi')
#     id = cd.index('71FFE3F1FF007E38FC01C7E3FE3F1FF0071F803F1C000CF0F0CF033C0CCFF3F3C0CF03CC')
#     cd.pop(id)
#     cd.insert(id, '71FFE3F1FF007E38FC01C7E3FE3F1FF0071F803F1C')
#     cd.insert(id + 1, 'CF0F0CF033C0CCFF3F3C0CF03CC')
#
# if '1E1819E79F87867F99FE6607819E00137AC51995EBD88' in cd:
#     print('hihi')
#     id = cd.index('1E1819E79F87867F99FE6607819E00137AC51995EBD88')
#     cd.pop(id)
#     cd.insert(id, '1E1819E79F87867F99FE6607819E')
#     cd.insert(id + 1, '137AC51995EBD88')