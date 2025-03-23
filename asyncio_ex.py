import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate an I/O operation
    print("World")

async def main():
    # Run the coroutine
    await say_hello()

# Run the event loop
asyncio.run(main())