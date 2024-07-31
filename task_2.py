#Создать скрипт, который создает пул потоков с ThreadPoolExecutor с 4 рабочими потоками,
# затем отправить 4 задачи на выполнение в пул потоков с помощью executor.submit().
# Как только все задачи отправлены в пул, ждём их завершения с помощью concurrent.futures.wait().
from concurrent.futures import ThreadPoolExecutor, wait


def worker(task_id):
    print(f"task with id {task_id} done")

    return task_id


with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(worker, i) for i in range(4)]

    done, not_done = wait(futures)

    results = [future.result() for future in done]

print(results)
