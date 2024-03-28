from channels.generic.websocket import AsyncWebsocketConsumer
import json

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print("XXX connect")
#         await self.accept()

#     async def disconnect(self, close_code):
#         print("XXX disconnect")
#         pass

#     async def receive(self, text_data):
#         print("XXX receive")
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))



class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'notifications'
        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def notification_message(self, event):
        # Send a message to the WebSocket
        await self.send(text_data=json.dumps(event["text"]))        