import asyncio
import random

async def coro():
    print('coro is running')
    await asyncio.sleep(1)
    for i in range(5):
        sub = await asyncio.ensure_future(sub_coro(i))
        print('sub  {} result {}'.format(i, sub))
    print('coro completed')
    return 1

async def sub_coro(i):
    ran = random.randint(1,9)
    print('sub {} is completed {}s'.format(i,ran))
    await asyncio.sleep(ran)
    return 1

if __name__ == '__main__':
    co = coro()
    print('>>> running ...')
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(co)
    print(result)
    loop.close()