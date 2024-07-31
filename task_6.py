# Создать скрипт, где будет 3 асинхронные функции с функционалом из предыдущей таски
# (с принтом, слипом и снова принтом).
# Запустить их при помощи asyncio.gather(). Поэкспериментировать со временем слипа внутри функций.
import asyncio


async def test():
    print("Task started")
    await asyncio.sleep(2)
    print("Task finished")


async def test1():
    print("Task1 started")
    await asyncio.sleep(2)
    print("Task1 finished")


async def test2():
    print("Task2 started")
    await asyncio.sleep(2)
    print("Task2 finished")


async def main():
    result = await asyncio.gather(test(), test1(), test2())
    return result


asyncio.run(main())
