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
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        acc = accuracy_score(y_test, y_pred)
        print("Accuracy of %s is %s" % (names[i], acc))

def main():
    #todo - insert the pdf file name
    """
    we will use 3 different classification algorithm. more about then in the
    pdf.
    """
    training_data = pd.read_csv(
        r"filtered_csv_files\geoFull2016.csv")
    testing_data = pd.read_csv(
        r"filtered_csv_files\geoUnited2017.csv")
    x_train = training_data[["Day", "Zone", "Latitude", "Longitude"]]
    y_train = training_data['Parking Violation']
    x_test = testing_data[["Day", "Zone", "Latitude", "Longitude"]]
    y_test = testing_data['Parking Violation']
    classification_models(x_train, x_test, y_train, y_test)

if __name__ == "__main__":
    main()
