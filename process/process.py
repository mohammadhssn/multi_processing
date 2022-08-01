import os
from time import sleep, perf_counter
from multiprocessing import Process, current_process

start = perf_counter()


def show(name):
    print(f'starting {name} ...')
    sleep(3)
    print(current_process())
    print(current_process().name)
    print(current_process().pid)

    print(os.getpid())
    print(os.getppid())  # parent process id
    print(f'ending {name} ...')


process_1 = Process(target=show, args=('One',))
process_2 = Process(target=show, args=('Two',))

process_1.start()
process_2.start()

print(process_1.is_alive())  # True
print(process_2.is_alive())  # True

process_1.join()
process_2.join()

print(process_1.is_alive())  # False
print(process_2.is_alive())  # False

end = perf_counter()

print(round(end - start))  # 3
