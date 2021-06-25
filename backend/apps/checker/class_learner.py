'''
class_learner.py
This is used to train models and analyze them.
We will use class_saver.py script to save the models that gives out the best results.

Usage:
    python <filename>.py
    filename: class_learner

Note:   Remember to give full path to module level script after setting project path.
        DO NOT use auto-formatter like autopep-8 for running this script.
'''

from django.core.wsgi import get_wsgi_application
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import os, sys

proj_path = "."
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
application = get_wsgi_application()

from backend.apps.checker.util import *
from backend.apps.checker.models import *

print("Setting up..")
cDict = loadCanonDict()
qs_Examples = ArticleExample.objects.filter(quality_class__lt=5)

print("Processing examples")
(Y_vector, examplesMatrix) = processExamples(qs_Examples, cDict)

print("ExamplesMatrix Results: ")
print(examplesMatrix.shape)
print("Y values results:")
print(Y_vector.shape)

print("Max/min of Y: ")
ymax = max(Y_vector)
ymin = min(Y_vector)
print(str(ymax) + "/" + str(ymin))

X_train, X_test, y_train, y_test = train_test_split(
    examplesMatrix, Y_vector, test_size=0.2)

print("Training...")

# Uncomment the model that you wish to try out:

# model = MLPClassifier(hidden_layer_sizes=(128,64,32,16,8), max_iter=2500)
model = SVC(gamma='scale', probability = True)
# model = KNeighborsClassifier()
# model = LinearDiscriminantAnalysis()
# model = GaussianNB()
# model = DecisionTreeClassifier()
# model = LogisticRegression()

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Max/min of predictions: ")
ymax = max(predictions)
ymin = min(predictions)
print(str(ymax) + "/" + str(ymin))

print("Max/Min of Y_test")
ymax = max(y_test)
ymin = min(y_test)
print(str(ymax) + "/" + str(ymin))

print("Max/Min of Y_train")
ymax = max(y_train)
ymin = min(y_train)
print(str(ymax) + "/" + str(ymin))

print("Statistical tests...")
print("***************")
print("Accuracy score: " + str(accuracy_score(predictions, y_test)))
print("Confusion Matrix: ")
print(confusion_matrix(predictions, y_test))
print("Classification report: ")
print(classification_report(predictions, y_test))
print("***************")
print("Regression based: ")

rSq = r2_score(y_test, predictions)
expVariance = explained_variance_score(y_test, predictions)
maxErr = max_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print("R^2: " + str(rSq))
print("Explained variance: " + str(expVariance))
print("Max Error: " + str(maxErr))
print("Mean absolute Error: " + str(mae))

exit(0)
