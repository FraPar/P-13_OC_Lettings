import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_oc_lettings_site.settings')

application = get_asgi_application()
