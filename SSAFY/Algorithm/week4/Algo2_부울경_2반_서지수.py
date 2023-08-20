# 스택 두 개로 큐 구현하기 (클래스 사용하지 않음)
stack1 = []
stack2 = []

def enqueue(item):
    stack1.append(item)

def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        raise Exception("Queue is empty!")
    return stack2.pop()

# [1,2,3]을 예시로 사용하고 결과를 출력
enqueue(1)
enqueue(2)
enqueue(3)

results_no_class = [dequeue(), dequeue()]
enqueue(4)
results_no_class.extend([dequeue(), dequeue()])

results_no_class
