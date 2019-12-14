"""Producer."""
import asyncio
import random


async def produce(queue, n):
    """Produce item for consume."""
    count = 0
    for x in range(1, n + 1):
        count += 1
        # produce an item
        print('produce|await\n-----producing {}/{}--{}'.format(x, n, count))
        # simulate i/o operation using sleep
        await asyncio.sleep(count)
        print('produce|waiting....')
        item = str(x)
        # put the item in the queue
        await queue.put(item)

    # indicate the producer is done
    await queue.put(None)


async def consume(queue):
    """Consume."""
    while True:
        # wait for an item from the producer
        print('consume|await')
        item = await queue.get()
        print('consume|', item)
        if item is None:
            # the producer emits None to indicate that it is done
            break

    # process the item
    print('consume|consuming item {}...'.format(item))
    # simulate i/o operation using sleep
    await asyncio.sleep(random.random())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)
    producer_coro = produce(queue, 3)
    consumer_coro = consume(queue)
    loop.run_until_complete(asyncio.gather(producer_coro, consumer_coro))
    loop.close()
