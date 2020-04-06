from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rbac.models import  CR
import json

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print('连接成功')
        user_name = self.scope['user']

        client = CR.objects.get_or_create(user=user_name)[0]
        client.channel = self.channel_name

        # Make a database row with our channel name
        # CR.objects.create(user=user_name,channel=self.channel_name)
        client.save()
        self.accept()

    def disconnect(self, close_code):
        # Note that in some rare cases (power loss, etc) disconnect may fail
        # to run; this naive example would leave zombie channel names around.
        CR.objects.filter(channel=self.channel_name).delete()

    def chat_message(self, event):
        message = event['message']
        # Handles the "chat.message" event when it's sent to us.
        self.send(text_data=json.dumps({
            'message': message
        }))


def SendMsg(user,message):
    channel_layer = get_channel_layer()
    channel_name = CR.objects.get(user=user).channel

    async_to_sync(channel_layer.send)(channel_name, {
        "type": "chat.message",
        "message": message,
    })