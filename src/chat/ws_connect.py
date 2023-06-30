import aiohttp
import time
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        client_id = int(time.time() * 1000)
        #TODO switch to second session if deploying

        # async with session.ws_connect(f'http://localhost:8000/chat/ws/{client_id}') as ws:
        async with session.ws_connect(f'https://global-messenger.onrender.com/chat/ws/{client_id}') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    with open("ws_messages.txt", "a") as file:
                        file.write(f"{msg.data}\n")

asyncio.run(main())
