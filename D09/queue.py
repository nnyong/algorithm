Queue=[0]*10
front=-1
rear=-1

rear+=1;Queue[rear]=1
rear+=1;Queue[rear]=2
rear+=1;Queue[rear]=3

while front!=rear: # 큐에 뭔가 있는 경우
    front+=1
    print(Queue[front])

