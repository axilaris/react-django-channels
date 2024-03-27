from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print "XXX connect"
        await self.accept()

    async def disconnect(self, close_code):
        print "XXX disconnect"
        pass

    async def receive(self, text_data):
        print "XXX receive"
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))