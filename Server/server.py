import asyncio
import websockets
import threading
import time
import os
 
async def handler(websocket, path):
    data = await websocket.recv()
    await websocket.send(data)
    if data == "open kivy interface":
        os.system("sudo python /home/pi/upwork_demo/kivy_interface_main.py")
    elif data == "open web interface":
        os.system("sudo su -l pi -c startx")

 
start_server = websockets.serve(handler, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

