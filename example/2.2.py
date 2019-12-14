import asyncio
import random

# config
COUNT = 0
KEY = 0

# function

async def task_1(key, loop):
    """ Task 1
        start
    """
    if key > 0:
        time = random.randint(0,10)
        print('task_1 will be completed in {}'.format(time))
        await asyncio.sleep(time) 
        print('task_1 done')
        return 1
    print('task_1 Fail\nEnd process!!!')
    loop.stop()
    
async def task_2(key, loop):
    """ Task 2
        processing
    """
    if key > 0:
        time = random.randint(0,10)
        print('task_2 will be completed in {}'.format(time))
        await asyncio.sleep(time) 
        print('task_2 done')
        return 2
    print('task_2 Fail\nEnd process!!!')
    loop.stop()

async def task_3(key, loop):
    """ Task 3
        must be completed
    """
    if key > 0:
        time = random.randint(0,10)
        await asyncio.sleep(time) 
        print('task_3 will be completed in {}'.format(time))
        print('task_3 done')
        return 3
    print('task_3 Fail\nEnd process!!!')
    loop.stop()

async def task_4(key, loop):
    """ Task 4
        end   
    """
    if key > 0:
        time = random.randint(0,10)
        print('task_4 will be completed in {}'.format(time))
        await asyncio.sleep(time) 
        print('task_4 done')
        return 4
    print('task_4 Fail\nEnd process!!!')
    loop.stop()


async def main(key):
    """ main
    """
    loop = asyncio.get_event_loop()
    result = asyncio.create_task(
        asyncio.gather(task_1(key, loop),
                       task_2(key, loop))
    )
    print(result)
    loop.c(task_3(key, loop))
    loop.run_until_complete(task_4(key, loop))
    loop.close()


if __name__ == '__main__':
    key = range(3)
    # loop.run_in_executor(None, main, i)
    main(1)
