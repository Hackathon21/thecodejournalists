import pandas as pd
from django.core.wsgi import get_wsgi_application
import os
import sys
import time

proj_path = "."
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
application = get_wsgi_application()

from strainer import *
from backend.apps.checker.models import *

ss = SoupStrainer()
print("Initializing dictionary...")
ss.init()

record_count = 1

def harvest_Politifact_data():
    global record_count
    print("Ready to harvest Politifact data.")
    print("Reading URLs file")
    df_csv = pd.read_csv("backend/apps/checker/politifact_data.csv", error_bad_lines=False,
                         quotechar='"', thousands=',', low_memory=False)
    for _, row in df_csv.iterrows():
        try:
            if(ss.loadAddress(row['news_url'])):
                #  ignoring those pages with < 500 words to ignore 404 error pages.
                if(len(ss.extractText) > 500):
                    ae = ArticleExample()
                    ae.body_text = ss.extractText
                    ae.origin_url = row['news_url']
                    ae.origin_source = 'politifact data'
                    ae.bias_score = 0 
                    ae.bias_class = 5  #  5 means 'no data'
                    ae.quality_score = row['score']
                    ae.quality_class = row['class']
                    ae.save()
                    print(record_count)
                    record_count += 1
                    time.sleep(0.1)
                else:
                    print("**** This URL produced insufficient data.")
            else:
                print("**** Error on that URL ^^^^^")
        except:
            pass


def harvest_MBC_data():
    global record_count
    print("Ready to harvest Media Bias Chart data.")
    print("Reading URLs file")
    df_csv = pd.read_csv("backend/apps/checker/MediaBiasChartData.csv",
                         error_bad_lines=False, quotechar='"', thousands=',', low_memory=False)
    for _, row in df_csv.iterrows():
        try:
            if(ss.loadAddress(row['Url'])):
                ae = ArticleExample()
                ae.body_text = ss.extractText
                ae.origin_url = row['Url']
                ae.origin_source = row['Source']
                ae.bias_score = row['Bias']
                ae.quality_score = row['Quality']
                ae.bias_class = 5
                if(ae.quality_score <= 16.25):
                    ae.quality_class = 1
                elif(ae.quality_score <= 32.50):
                    ae.quality_class = 2
                elif(ae.quality_score <= 48.75):
                    ae.quality_class = 3
                else:
                    ae.quality_class = 4
                ae.save()
                print(record_count)
                record_count += 1
                time.sleep(0.1)
            else:
                print("Error on that URL ^^^^^")
        except:
            pass


harvest_MBC_data()
harvest_Politifact_data()
