import asyncio 
import aiohttp


async def _get_file(IP: str, legacy: bool):
    
    if legacy: 
        path = "http://192.168." + IP + ":8085/api/storage/file?args=%2Fstorage%2Femulated%2F0%2FAlReaderXPro%2FSync%2Fcites.txt&sender=web"
    else:
        path = "http://192.168." + IP + ":8085/api/storage/file?args=%2Fstorage%2Femulated%2F0%2FOReaderX%2FSync%2Fcites.txt&sender=web"
    async with aiohttp.ClientSession() as session:
        async with session.get(path) as resp:
            data = await resp.read()
            with open("temp/cites.txt", "wb") as f:
                f.write(data)


def get_file(IP: str, legacy: bool=True):
    asyncio.run(_get_file(IP, legacy))