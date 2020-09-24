from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
import socket

class MessagesConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('in connection: ', self)
         # Join room group

        await self.accept()

    async def disconnect(self, close_code):
        print('in disconnect: ', close_code)

    async def receive(self, text_data):
        print('in recieve')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
