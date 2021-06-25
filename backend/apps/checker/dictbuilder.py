'''
dictbuilder.py
Here we run through the examples downloaded and build out a table with a dictionary of all of the words.

Usage:
    python <filename>.py
    filename: dictbuilder

Note:   Remember to give full path to module level script after setting project path.
        DO NOT use auto-formatter like autopep-8 for running this script.

'''

from django.core.wsgi import get_wsgi_application
import os
import sys

proj_path = "."
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
application = get_wsgi_application()

from backend.apps.checker.util import *
from backend.apps.checker.models import *

print("Loading dictionary...")
cDict = loadCanonDict()

qs_Examples = ArticleExample.objects.all()
print("Examples: " + str(qs_Examples.count()))

for ex in qs_Examples:
    try:
        cwords = ex.body_text.split()
        print('.')
        for cwrd in cwords:
            if not (cwrd in cDict.keys()):
                nde = DictEntry(canonWord=cwrd)
                nde.save()
                cDict[cwrd] = nde.pk
    except:
        pass