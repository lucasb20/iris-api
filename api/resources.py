from flask import Blueprint

bp = Blueprint("Predict", __name__, url_prefix="/predict")

@bp.route("/", methods=['POST'])
def post():
    model = load('resources/model.joblib')
    predict = model.predict([[features['Sepal_Length'], features['Sepal_Width'], features['Petal_Length'], features['Petal_Width']],])[0].item()
    predict_str = ""
    if(predict == 0):
        predict_str = "setosa" 
    elif(predict == 1):
        predict_str = "versicolor"
    else:
        predict_str = "virginica"

    return {**features, 'Specie': predict_str}