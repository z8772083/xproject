from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rbac.models import  CR
import json

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('连接成功')
        user_name = self.scope['user']
        path = self.scope['path'].replace('/','_')

        self.user_group = str(self.scope['user']) + path
        print(self.user_group)
        await self.channel_layer.group_add(
            self.user_group,
            self.channel_name
        )
        # client = CR.objects.get_or_create(user=user_name)[0]
        # client.channel = self.channel_name

        # Make a database row with our channel name
        # CR.objects.create(user=user_name,channel=self.channel_name)
        # client.save()
        await self.accept()

    async def disconnect(self, close_code):
        # Note that in some rare cases (power loss, etc) disconnect may fail
        # to run; this naive example would leave zombie channel names around.
        # CR.objects.filter(channel=self.channel_name).delete()
        await self.channel_layer.group_discard(
            self.user_group,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('3333333333')
        # 信息群发
        await self.channel_layer.group_send(
            self.user_group,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        print('222222')
        message = event['message']
        # Handles the "chat.message" event when it's sent to us.
        await self.send(text_data=json.dumps({
            'message': message
        }))


def SendMsg(user_group,message):

    channel_layer = get_channel_layer()
    # channel_name = CR.objects.get(user=user).channel
    print('1111111')
    async_to_sync(channel_layer.group_send)(
        user_group,
        {
        "type": "chat.message",
        "message": message,
    })