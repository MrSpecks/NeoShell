import aiohttp
from tqdm import tqdm
import asyncio

async def fetch(session, url):
 async with session.get(url) as response:
  return response.status

async def main():
 urls = ["https://httpbin.org/get" for _ in range(5)]
 async with aiohttp.ClientSession() as session:
  for f in tqdm(asyncio.as_completed([fetch(session, url) for url in urls]), total=len(urls)):
    status = await f 
    print(f"Status: {status}")


if __name__ == "__main__":
 asyncio.run(main())