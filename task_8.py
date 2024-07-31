# пишем корутину без использования async
import asyncio


@asyncio.coroutine
def my_coroutine():
    print('Start of the coroutine')
    yield from asyncio.sleep(1)
    print('End of the coroutine')


loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
loop.close()