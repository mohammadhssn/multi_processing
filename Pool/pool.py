import time
from multiprocessing import Pool


def init():
    print('this is init.')


def show(name):
    print(f'stating {name} ...')
    time.sleep(3)
    print(f'ending {name} ...')


names = ['One', 'Two', 'Three', 'Four']

pool = Pool(processes=2, initializer=init)
pool.map(show, names)
pool.close()

pool.join()
