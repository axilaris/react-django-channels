"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
#import backend.routing
import user_api.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter(
#         user_api.routing.websocket_urlpatterns
#         #backend.routing.websocket_urlpatterns
#     ),
# })

application = ProtocolTypeRouter({     
            "websocket": URLRouter([         
                path("/ws/notifications/", consumers.NotificationConsumer.as_asgi()),     
                ]), 
            }) 