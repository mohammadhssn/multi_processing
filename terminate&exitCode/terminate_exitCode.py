from time import sleep, perf_counter
from multiprocessing import Process

start = perf_counter()


def show(name):
    print(f'starting {name} ...')
    sleep(3)
    print(f'ending {name} ...')


process_1 = Process(target=show, args=('One',))
process_2 = Process(target=show, args=('Two',))

process_1.start()
process_2.start()

print(process_1.is_alive())
print(process_2.is_alive())

process_1.terminate()
process_2.kill()

process_1.join()
process_2.join()

end = perf_counter()

print(round(end - start))  # 0
print(process_1.exitcode)  # -15
print(process_2.exitcode)  # -9
