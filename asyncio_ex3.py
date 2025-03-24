import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a network request
    print("Data fetched!")
    return {"data": 123}

async def process_data():
    print("Processing data...")
    await asyncio.sleep(1)  # Simulate processing time
    print("Data processed!")

async def main():
    # Create a task for fetch_data
    fetch_task = asyncio.create_task(fetch_data())

    # Run process_data concurrently
    await process_data()

    # Wait for fetch_task to complete and get the result
    result = await fetch_task
    print("Result:", result)

# Run the event loop
asyncio.run(main())