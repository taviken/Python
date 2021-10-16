import httpx
import re
import requests
import time
import subprocess
import sys
import asyncio

# builtin profiling packages
import cProfile
import pstats


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func()
        elapsed = time.perf_counter() - start
        print(f'{func.__code__.co_name} in {elapsed:.2f}s')
        return res

    return wrapper


@timeit
def slow_function():
    with open('websites.txt') as f:
        urls = [line.strip() for line in f.readlines()]

    htmls = []
    for url in urls:
        htmls += [requests.get(url).text]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall('https://', html))
        count_http += len(re.findall('http://', html))

    time.sleep(2.0)
    print(f'{count_https=}')
    print(f'{count_http=}')
    if count_http != 0 and count_https != 0:
        print(f'{count_https/count_http=}')


async def fast_function():
    with open('websites.txt') as f:
        urls = [line.strip() for line in f.readlines()]

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        requested = await asyncio.gather(*tasks)
    htmls = [request.text for request in requested]
    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall('https://', html))
        count_http += len(re.findall('http://', html))

    print(f'{count_https=}')
    print(f'{count_http=}')
    if count_http != 0 and count_https != 0:
        print(f'{count_https/count_http=}')


def main():
    # slow_function()

    with cProfile.Profile() as pr:
        slow_function()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='slow_function.prof')
    # run 'snakeviz.exe slow_function.prof' for visual breakdown of stats

    with cProfile.Profile() as pr:
        asyncio.run(fast_function())
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='fast_function.prof')


if __name__ == '__main__':
    main()
