"""
Now we would like to predict the likelihood of getting a parking ticket.
We will train on the data we generated in the previous steps from 2016 and
test on the one generated from 2017.
"""
import xgboost
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
import pandas as pd
import time
import warnings
import sys
from pathlib import Path

def classification_models(x_train, x_test, y_train, y_test):
    classifiers = []
    model1 = xgboost.XGBClassifier()
    classifiers.append(model1)
    model2 = RandomForestClassifier()
    classifiers.append(model2)
    model3 = tree.DecisionTreeClassifier()
    classifiers.append(model3)

    names = ["XGBClassifier", "RandomForestClassifier", "DecisionTreeClassifier"]
    for i,clf in enumerate(classifiers):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        acc = accuracy_score(y_test, y_pred)
        print("Accuracy of %s is %s" % (names[i], acc))

def main(train_path, test_path):
    #todo - insert the pdf file name
    """
    we will use 3 different classification algorithm. more about then in the
    pdf.
    """
    then = time.time()
    training_data = pd.read_csv(train_path)
    testing_data = pd.read_csv(test_path)
    x_train = training_data[["Day", "Zone", "Latitude", "Longitude"]]
    y_train = training_data['Parking Violation']
    x_test = testing_data[["Day", "Zone", "Latitude", "Longitude"]]
    y_test = testing_data['Parking Violation']
    classification_models(x_train, x_test, y_train, y_test)
    now = time.time()  # Time after it finished
    print("It took for violation round 2: ", now - then, " seconds")

if __name__ == "__main__":
    # geoUnited2016 and 2017 csv files
    train_path = Path(sys.argv[1])
    test_path = Path(sys.argv[2])
    main(train_path, test_path)

