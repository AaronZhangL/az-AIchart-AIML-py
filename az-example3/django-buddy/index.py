import sys
import os

path = os.path.dirname(os.path.abspath(__file__))+'/buddy'
path2 = os.path.dirname(os.path.abspath(__file__))+'/core'
if path not in sys.path:
  sys.path.insert(1, path)
  sys.path.insert(1, path2)

os.environ['DJANGO_SETTINGS_MODULE'] = 'buddy.settings'
from django.core.handlers.wsgi import WSGIHandler
app = WSGIHandler()

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)

