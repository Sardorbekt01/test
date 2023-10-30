import time
import asyncio

print('--->',time.time())
async def work (msg):
    print(f'{msg}start')
    await asyncio.sleep(1)
    print(f'{msg} end')

    async def main():
        await asyncio.gather(work('work1'), work('work2'),work('work3'))

if __name__ == '__main__':
    asyncio.run(main())

print(time.time)
