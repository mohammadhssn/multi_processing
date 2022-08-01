from time import sleep, perf_counter
from multiprocessing import Process

start = perf_counter()


def show(name, delay):
    print(f'starting {name} ...')
    sleep(delay)
    print(f'ending {name} ...')


class ShowProcess(Process):
    def __init__(self, name, delay):
        super().__init__()  # required call super
        self.name = name
        self.delay = delay

    def run(self) -> None:
        show(self.name, self.delay)


process_1 = ShowProcess('One', 3)
process_2 = ShowProcess('Two', 7)

process_1.start()
process_2.start()

process_1.join()
process_2.join()

end = perf_counter()

print(round(end - start))
