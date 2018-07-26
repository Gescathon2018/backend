from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .utils import create_response
from . import commands

class BlinkMyStickConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, data):
        print(data)
        command = data.get('command')
        if not command:
            await self.send_json(create_response(1, 'No command specified'))
            return


        if command != 'login' and self.scope['user'].is_anonymous:
            await self.send_json(create_response(3, 'You must be logged in '
                'to invoke this command'))
            return            

        cmd = getattr(commands, command, None)

        if not cmd:
            await self.send_json(create_response(2, "Command not found"))
            return

        response = await cmd(self, data.get('data'))
        await self.send_json(response)
   
        

    async def bms_notify(self, event):
        await self.send_json(event['message'])
