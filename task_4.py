# Создать скрипт, который создаёт 4 процесса с использованием пула процессов
from multiprocessing import Pool


def worker(n):
    return n * n


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        result = pool.map(worker, (4,))

    print(result)
