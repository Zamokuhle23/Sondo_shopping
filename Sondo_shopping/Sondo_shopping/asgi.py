import os

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import store.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sondo_shopping.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            store.routing.websocket_urlpatterns
        )
    )
})
