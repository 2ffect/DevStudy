# 큐 생성
queue = [0] * 3
front = rear = -1

# 1, 2, 3 enQueue
rear += 1
queue[rear] = 1     # enQueue 1

rear += 1
queue[rear] = 2     # enQueue 2

rear += 1
queue[rear] = 3     # enQueue 3

print(queue)

# 1, 2, 3 deQueue
while front != rear:    # Queue에 원소가 남아있으면,
    front += 1
    t = queue[front]
    print(t)
else:
    print("Queue is Empty")

# front += 1
# print(queue[front])     # deQueue 1
#
# front += 1
# print(queue[front])     # deQueue 2
#
# front += 1
# print(queue[front])     # deQueue 3



# isEmpty(), isFull()
#
# if front == rear:
#     print("Queue is Empty")
#