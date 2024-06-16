# neural-network-api
A Flask API consuming a neural network model.

**Description**

  This is an API project in Flask used to communicate with a neural network model to classify types of flowers from the iris dataset, from the scikit-learn library, classifying into Setosa, Versicolor or Virginica.

  NOTE: 'neuralnetwork' folder used to train the model. The model is a Multilayer Perceptron for classification with 100 hidden layer neurons, ReLU activation function, four input neurons and one output neuron.

**Installation instructions**

**System requirements**

* Python 3.x

**Application installation**

1. Enter the backend folder
2. Run `pip install -r requirements.txt` to install the dependencies
3. Run `flask run` to run API

**Screenshots**

- Response on `POST /predict {"features":[5.1, 3.5, 1.4, 0.2]}`

```bash
{
	"predict": "iris-setosa"
}
```

- Response on `POST /predict {"features":[7.0, 3.2, 4.7, 1.4]}`

```bash
{
	"predict": "iris-versicolour"
}
```

- Response on `POST /predict {"features":[6.3, 3.3, 6.0, 2.5]}`

```bash
{
	"predict": "iris-virginica"
}
```