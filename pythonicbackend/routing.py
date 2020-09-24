from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import MessagesConsumer

websocket_urlpatterns = [
    path(r'ws/messages/', MessagesConsumer),
]

application = ProtocolTypeRouter({
    # (http->django views is added by default)
        'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})