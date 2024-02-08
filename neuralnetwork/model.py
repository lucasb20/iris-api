from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from joblib import dump

data_iris = load_iris()

x_features = data_iris.data
y_labels = data_iris.target

x_train, x_test, y_train, y_test = train_test_split(x_features, y_labels, test_size=0.3)

mlp = MLPClassifier()
mlp.fit(x_train, y_train)

print("x_test:")
print(x_test)
print("y_test:")
print(y_test)
print("Acurracy: " + str(mlp.score(x_test, y_test)))

s = dump(mlp, "model.joblib")