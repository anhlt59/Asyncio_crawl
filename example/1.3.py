import asyncio
import time
import pprint

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print('started at', time.strftime('%X'))

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print('finished at', time.strftime('%X'))

# pprint.pprint(asyncio.__all__)
