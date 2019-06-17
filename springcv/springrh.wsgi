"""
WSGI config for cadi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "springcv.settings")
sys.path.append("/home/djangospring/env35spring/lib/python3.5/site-packages")
sys.path.append("/home/djangospring/env35spring/springrh")
sys.path.append("/home/djangospring/env35spring/springrh/springcv")

#os.environ("DJANGO_SETTINGS_MODULE", "springcv.settings")

application = get_wsgi_application()
