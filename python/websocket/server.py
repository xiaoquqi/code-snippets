#!/usr/bin/python3

import asyncio
import websockets
import time


async def echo(websocket, path):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        await websocket.send(message)

        while True:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #if str(t).endswith("0"):
            #    await websocket.send(t)
            #    break
            await websocket.send("[%s]Send client task" % str(t))
            time.sleep(10)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
