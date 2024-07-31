# Используя предыдущие знания (asyncio.gather()) создать скрипт,
# который асинхронно пингует список сайтов (штук 5 разных) и выводит время пинга.
# Подставить не корректный сайт и обработать ошибку (когда не получим код 200 в ответе.)
import asyncio
import aiohttp


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientError as e:
        return f"Error fetching {url}: {e}"


async def main():
    urls = [
        'https://httpbin.org/get',
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://api.github.com/users/octocat',
        'https://reqres.in/api/users/1',
        "https://incorrectsite.tu"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for response in responses:
            print(response)


asyncio.run(main())
