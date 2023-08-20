# # 큐 두 개를 사용하여 스택 구현하기 (deque X)
# queue1 = []
# queue2 = []
#
#
# def push(item):
#     queue1.append(item)
#
#
# def pop():
#     while len(queue1) > 1:
#         queue2.append(queue1.pop(0))
#
#     popped_item = queue1.pop(0)
#     queue1[:], queue2[:] = queue2, []
#
#     return popped_item
#
# push(1)
# push(2)
# push(3)
#
# results_stack = [pop(), pop()]
# push(4)
# results_stack.extend([pop(), pop()])



# 큐 두 개를 사용하여 스택 구현하기 (deque O)
from collections import deque

queue1 = deque()
queue2 = deque()


def push(item):
    queue1.append(item)


def pop():
    global queue1, queue2
    # queue1에 있는 모든 항목을 queue2로 옮긴다.
    while len(queue1) > 1:
        queue2.append(queue1.popleft())

    # queue1의 마지막 항목이 스택의 맨 위 항목이므로 이를 pop한다.
    popped_item = queue1.popleft()

    # queue2와 queue1의 역할을 바꾼다.
    queue1, queue2 = queue2, queue1

    return popped_item


# 예제 실행
push(1)
push(2)
push(3)

results_deque_stack = [pop(), pop()]
push(4)
results_deque_stack.extend([pop(), pop()])