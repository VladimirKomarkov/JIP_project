# Создать скрипт, который создаёт 4 процесса.
# Воркер в данном случае пусть так же выводит инфу о id и слипается на пару секунд.
from multiprocessing import Process
import time


def worker(taks_id):
    print(f"start {taks_id}")
    time.sleep(2)
    print(f"end {taks_id}")


if __name__ == "__main__":
    processes = []

    for i in range(4):
        process = Process(target=worker, args=(i,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print("All tasks finished")
