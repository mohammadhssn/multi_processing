from multiprocessing import Lock, Process

nums = 0  # shared resource
lock = Lock()


def add(nums):
    with lock:
        for _ in range(100000):
            nums += 1


def subtract(nums):
    with lock:
        for _ in range(100000):
            nums -= 1


proces_add = Process(target=add, args=(nums,))
proces_subtract = Process(target=subtract, args=(nums,))

proces_add.start()
proces_subtract.start()

proces_add.join()
proces_subtract.join()

print(f'nums: {nums}')
