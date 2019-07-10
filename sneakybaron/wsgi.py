"""
WSGI config for sneakybaron project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/home/ubuntu/sneakybaron-back')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/ubuntu/sneakybaron-back/venv/Lib/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sneakybaron.settings.production')

application = get_wsgi_application()
