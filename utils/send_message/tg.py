import aiohttp
import asyncio

import config


async def send_message(msg: str) -> None:
    url = f"https://api.telegram.org/bot{config.TG['access_token']}/sendMessage?chat_id={config.TG['chat_id']}&text={msg}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                print("ERROR (send_message)")
