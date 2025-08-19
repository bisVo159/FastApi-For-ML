import asyncio
from timeit import default_timer as timer

async def run_task(name,seconds):
    print(f"{name} task started at {timer()}")
    await asyncio.sleep(seconds)
    print(f"{name} task ended at {timer()}")

async def main():
    start = timer()
    await asyncio.gather(
        run_task('Task 1', 2),
        run_task('Task 2', 1),
        run_task('Task 3', 3)
    )
    print(f'\nTotal time taken: {timer() - start:.2f} s')

asyncio.run(main())