"""D."""
import asyncio
import time


async def task1():
    """Task1."""
    await asyncio.sleep(0.5)


async def task2():
    """Task2."""
    await asyncio.sleep(0.5)


async def task3():
    """Task3."""
    await asyncio.sleep(10)


async def handler(name):
    """Handle."""
    # task1
    total = 0
    start = time.time()

    print('{}--task1 0.5s'.format(name))
    await task1()
    finish = time.time() - start
    total += finish
    print('{}--task1 realtime {}s'.format(name, finish))

    # task2
    start = time.time()
    print('{}--task1 0.5s'.format(name))
    await task2()
    finish = time.time() - start
    total += finish
    print('{}--task2 realtime {}s'.format(name, finish))

    # task3
    start = time.time()
    print('{}--task1 10s'.format(name))
    await task3()
    finish = time.time() - start
    total += finish
    print('{}--task3 realtime {}s'.format(name, finish))

    print('{} done for {} seconds'.format(name, 11))


def main():
    """Main."""
    # Generate timings task
    total_sleep = 11 * 3

    # Wait.
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(handler('handler-{}'.format(1)),
                                           handler('handler-{}'.format(2)),
                                           handler('handler-{}'.format(3))))
    total = time.time() - start
    loop.close()

    print('====')
    print('3 handler done in parallel for {} seconds'.format(total))
    print('total sleep time: {} seconds'.format(total_sleep))


if __name__ == '__main__':
    main()
