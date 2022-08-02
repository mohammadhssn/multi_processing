import queue

q = queue.Queue()  # FIFO

q.put(3)
q.put(6)
q.put(9)

# print(q.qsize())  # 3

print(q.get())  # 3
print(q.get())  # 6
print(q.get())  # 9

# --------------------------------------
print('-' * 30)

lq = queue.LifoQueue()

lq.put(3)
lq.put(6)
lq.put(9)

print(lq.get())  # 9
print(lq.get())  # 6
print(lq.get())  # 3

# --------------------------------------
print('-' * 30)

pq = queue.PriorityQueue()

pq.put(3)
pq.put(6)
pq.put(1)

print(pq.get())  # 1
print(pq.get())  # 3
print(pq.get())  # 6

print(pq.empty())  # True
