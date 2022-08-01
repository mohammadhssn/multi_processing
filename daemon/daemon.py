import sys
from time import sleep, perf_counter
from multiprocessing import Process

start = perf_counter()


def show(name):
    print(f'starting {name} ...')
    sleep(3)
    print(f'ending {name} ...')


process_1 = Process(target=show, args=('One',), daemon=True)
process_2 = Process(target=show, args=('Two',), daemon=True)

process_1.start()
process_2.start()

end = perf_counter()

print(round(end - start))  # 0

sys.exit()
