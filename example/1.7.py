import asyncio
async def holacoro ():    
	print ("Hello% d"% 1)    
	await asyncio.sleep (1)    

def renew (* args):    
	task = loop.create_task (holacoro ())    
	x = task.add_done_callback (renew)
	print(x)

loop = asyncio.get_event_loop ()
task = loop.create_task (holacoro ())
task.add_done_callback (renew)

try:     
	loop.run_until_complete(task)
except KeyboardInterrupt:     
	print ('Loop stopped') 
