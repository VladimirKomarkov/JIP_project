# Написать скрипт, который создает 3 потока и каждый поток прибавляет к глобальному счётчику
# 100 раз, используя мьютекс для синзронизации доступа к общим ресурсам
import threading

mutex = threading.Lock()

counter = 0


def increment_counter():
    global counter
    with mutex:
        counter += 100


threads = []

for i in range(3):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(counter)
