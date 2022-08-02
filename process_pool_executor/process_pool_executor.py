import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count


def show(name):
    print(f'starting {name} ...')
    time.sleep(3)
    print(f'ending {name} .')


def main():
    with ProcessPoolExecutor(max_workers=cpu_count()) as executer:
        names = ['One', 'Two', 'Three', 'Four', 'Five']
        executer.map(show, names)


main()
