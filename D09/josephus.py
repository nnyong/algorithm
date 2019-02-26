# Josephus Problem
# 마지막 남은 두 사람 위치
front=rear=-1
queue=[0]*100

def enQueue(item):
    global rear
    rear+=1
    queue[rear]=item

def deQueue():
    global front
    front+=1
    return queue[front]

for i in ['A','B','C','D','E','F','G','H','I','J']:
    enQueue(i)

print(queue)

for i in range(8):
    for j in range(3):
        # if j==2:
        #     item = deQueue()
        #     enQueue(False)
        item=deQueue()
        enQueue(item)

print(queue)
print(front%10)

