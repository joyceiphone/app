from flask import Flask, request, Response
from sklearn.model_selection import train_test_split
from sklearn import tree
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/train', methods=["POST"])
def train():
    try:
        df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
            names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"])
        X = df.iloc[:,:-1]
        y = df.iloc[:,-1]

        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)
        classifier = tree.DecisionTreeClassifier()
        classifier.fit(X_train, y_train)
        with open('model_pkl', 'wb') as files:
            pickle.dump(classifier, files)
        return Response('', status=200)
    except:
        return Response(status=201)

@app.route('/get-result', methods=["GET"])
def get_result():
    try:
        with open('model_pkl', 'rb') as f:
            classifier = pickle.load(f)
            args = request.args
            
            sepal_length = args.get('sepal_length', default='0')
            sepal_width=args.get('sepal_width', default='0')
            petal_length= args.get('petal_length', default='0')
            petal_width=args.get('petal_width', default='0')

            predictions = classifier.predict([[sepal_length,sepal_width,petal_length,petal_width]])
            return Response(response=predictions[0], status=200, mimetype='application/json')
    except:
        return Response(response="", status=201, mimetype='application/json')

if __name__ == '__main__':
    app.run("0.0.0.0")
