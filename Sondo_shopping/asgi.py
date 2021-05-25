import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import store.routing

django_asgi_app = get_asgi_application()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sondo_shopping.settings')
django.setup()
# application = get_default_application()
#
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            store.routing.websocket_urlpatterns
        )
    )
})
