import asyncio
async def holacoro():
	for i in range(3):
		await asyncio.sleep(1)
		print("Hola %d" % i)

async def chaocoro():
	for i in range(3):
		await asyncio.sleep(2)
		print("Chao %d" % i)

async def doscoro():
	await asyncio.ensure_future(holacoro()) 
	await asyncio.ensure_future(chaocoro()) 



if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	# loop.run_until_complete(doscoro()) 
	tasks = [asyncio.ensure_future (holacoro()),
			asyncio.ensure_future (chaocoro())]
	loop.run_until_complete(asyncio.gather(*tasks))


