import asyncio

async def task_one():
    print("Task 1: Start")
    await asyncio.sleep(2)  # Simulate a delay
    print("Task 1: End")

async def task_two():
    print("Task 2: Start")
    await asyncio.sleep(1)  # Simulate a delay
    print("Task 2: End")

async def main():
    # Run both tasks concurrently
    await asyncio.gather(task_one(), task_two())

# Run the event loop
asyncio.run(main())