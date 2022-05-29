#
# import time
# from threading import Thread
#
# # class MyThread(Thread):
# #     def start(self):
# #         print('start')
#
# def start_rocket(id):
#     time.sleep(3)
#     print(f'Rocket with id {id} is ready\n')
#
# threads_list = []
#
# for i in range(5):
#     thread = Thread(target=start_rocket,args=(i,), daemon=True)
#     threads_list.append(thread)
#
# for i in threads_list:
#     i.start()
#
# for i in threads_list:
#     i.join()
#
# # for i in range(5):
# #     start_rocket(i)

#
# from multiprocessing import Process
#
# from time import sleep
#
# def func(start, end,timeout):
#     while start < end:
#         print(f'Process {id}: {start}')
#         start += 1
#         sleep(timeout)
# if __name__ == '__main__':
#     process1 = Process(target=func, args=(3,10,1))
#     process2 = Process(target=func, args=(5,20,1))
#     process1.start()
#     process2.start()
#
#     print('END')



# from threading import Lock, Thread
#
# counter = 0
#
# lock = Lock()
#
# def func():
#     lock.acquire()
#     global counter
#     f = counter
#     counter += 1
#     lock.release()
#

import requests
import asyncio
import aiohttp
from datetime import datetime
import requests


resource_list = ['https://github.com/','https://www.youtube.com/']
st1 = datetime.now()
for resource in resource_list:
    r = requests.get(resource)
    print(len(r.text))
st2= datetime.now()
data1= st2 -st2
print(f'TIME {data1.microseconds} ')
async def get_data(url):
    print(f'Start {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(len(data))


t1 = datetime.now()

jobs = [get_data(url) for url in resource_list]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(jobs))
t2 = datetime.now()

data = t2 - t1
print(f'TIME {data.microseconds} ')