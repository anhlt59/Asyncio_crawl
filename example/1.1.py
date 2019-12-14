import asyncio
import random

# config
COUNT = 0


async def print_every_second():
    """Print seconds."""
    for i in range(30):
        print(i, 's')
        await asyncio.sleep(1)


async def print_every_minute():
    for i in range(4):
        print('>>>', i * 10)
        await asyncio.sleep(10)


async def do_some_thing():
    COUNT += 1
    time = random.randint(0, 10)
    print('do some thing complete in {}'.format(time))
    await asyncio.sleep()


async def last_job():
    COUNT += 1
    print('end')
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    loop.ensure_future(print_every_minute(),
                       print_every_second())

    loop.run_forever()
    loop.close()


if __name__ == '__main__':
    main()
