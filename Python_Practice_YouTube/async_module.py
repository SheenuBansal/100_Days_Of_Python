import asyncio

async def main():
    task=asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")
    return_value = await task
    print(f"Return value is: {return_value}")


async def other_function():
    print("1")
    await asyncio.sleep(1)
    print("2")
    return 10

if __name__ == "__main__":
    asyncio.run(main())