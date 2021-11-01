# [START vendor]
import os, sys
from google.appengine.ext import vendor

on_appengine = os.environ.get('SERVER_SOFTWARE','').startswith('Development')
if on_appengine and os.name == 'nt':
    sys.platform = "Not Windows"
# Add any libraries installed in the "lib" folder.
vendor.add('lib')
# [END vendor]