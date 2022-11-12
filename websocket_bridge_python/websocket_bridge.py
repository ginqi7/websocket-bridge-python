import asyncio
import websockets
import sys
import json
import threading


class WebsocketBridge:
    def __init__(self, app_name, server_port, on_message):
        self.app_name = app_name
        self.server_port = server_port
        self.on_message = on_message
        
    async def on_open(self, ws):
        self.client = ws 
        print("WebSocket Client [{app_name}] connected, the server port is {port}".format(app_name = self.app_name, port = self.server_port))
        await ws.send(json.dumps({"type": "client-app-name", "content": self.app_name}))

    async def start(self):
        async for websocket in websockets.connect("ws://localhost:" + self.server_port):
            try:
                await self.on_open(websocket)
                async for message in websocket:
                    await self.on_message(message)
            except websockets.ConnectionClosed:
                continue
        

    async def message_to_emacs(self, message):
        await self.client.send(json.dumps({"type": "show-message", "content": message}))

    async def eval_in_emacs(self, code):
        await self.client.send(json.dumps({"type": "eval-code", "content": code}))
        
    async def get_emacs_var(self, varName):
        # get Emascs variable using a new websocket short connect to communicate.
        async with websockets.connect("ws://localhost:" + self.server_port) as websocket:
            await websocket.send(json.dumps({"type": "fetch-var", "content": varName}))
            return await websocket.recv()
        
        

def bridge_app_regist(on_message):
    bridge = WebsocketBridge(sys.argv[1], sys.argv[2], on_message)
    return bridge
    
