priority = {'(': 0, '+': 1, '*': 2}

def postfix(lst):
    for i in lst:
        if i.isdigit():
            st.append(int(i))

    pass

for tc in range(1, 11):
    N = int(input())
    s = list(input())
    st = []
    postfix(s)
