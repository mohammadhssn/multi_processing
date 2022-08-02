from multiprocessing import Process, Queue

numbers = []


def p1_func(queue):
    nums = queue.get()
    nums.extend([1, 2, 3])
    queue.put(nums)  # [1, 2, 3]
    print(nums)


def p2_func(queue):
    nums = queue.get()
    nums.extend([4, 5, 6])
    queue.put(nums)  # [1, 2, 3, 4, 5, 6
    print(nums)


queue = Queue()
queue.put(numbers)

p1 = Process(target=p1_func, args=(queue,))
p2 = Process(target=p2_func, args=(queue,))

p1.start()
p2.start()

p1.join()
p2.join()

print(queue.get())  # [1, 2, 3, 4, 5, 6
