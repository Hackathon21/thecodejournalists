'''
class_saver.py
This file is used to save the train models and save them if needed after analyzing them.
Models are saved in checker app with .sav extension.

Usage:
    python <filename>.py
    filename: class_saver

Note:   Remember to give full path to module level script after setting project path.
        DO NOT use auto-formatter like autopep-8 for running this script.
'''

from sklearn.metrics import *
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
import pickle
import os, sys

proj_path = "."
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from backend.apps.checker.util import *
from backend.apps.checker.models import *

# Load datasets and dictionaries for the ML models
print("Setting up..")
cDict = loadCanonDict()
qs_Examples = ArticleExample.objects.filter(quality_class__lt = 5)
print("Processing examples")
(Y_vector, examplesMatrix) = processExamples(qs_Examples, cDict)
X_train, X_test, y_train, y_test = train_test_split(examplesMatrix, Y_vector, test_size=0.2)
chosen_models = {}

# Add models here to run, analyze and save.
chosen_models['backend/apps/checker/MLPC_model.sav'] = MLPClassifier(hidden_layer_sizes=(128,64,32,16,8), max_iter=2500)
chosen_models['backend/apps/checker/svc_model.sav'] = SVC(gamma='scale', probability = True)
chosen_models['backend/apps/checker/log_model.sav'] = LogisticRegression(max_iter=1000)

for fname, model in chosen_models.items():
    print("Working on " + fname)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Classification report: ")
    print(classification_report(predictions, y_test))
    print("Accuracy score: " + str(accuracy_score(predictions, y_test)))
    print("***************")
    dosave = input("Save " + fname + "? ")
    if(dosave == 'y' or dosave == 'Y'):
        print("Saving...")
        pickle.dump(model, open(fname, 'wb'))
        print("Saved!")
    else:
        print("Not saved!")