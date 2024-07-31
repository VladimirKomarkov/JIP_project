# Создать функцию которая будет принтовать что-то,
# потом асинхронно спать и снова принтовать, затем вызвать эту функцию с помощью asyncio.run.
# Посмотреть на результат и понять, почему так произошло.
import asyncio


async def test():
    print("Task started")
    await asyncio.sleep(2)
    print("Task finished")


asyncio.run(test())
