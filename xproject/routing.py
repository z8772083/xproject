from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from rbac.consumers import RbacConsumer
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url(r"^ws/chat/(?P<room_name>[^/]+)/$", ChatConsumer),
            url(r"^ws/rbac/chat/$", RbacConsumer),
        ])
    ),
})