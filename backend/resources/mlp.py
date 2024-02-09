from flask.views import MethodView
from flask_smorest import Blueprint
from joblib import load
from backend.schemas import IrisFeatures, IrisPredict

bp = Blueprint("mlp", __name__, description="Operations on mlp")

@bp.route("/iris")
class Iris(MethodView):
    @bp.arguments(IrisFeatures)
    @bp.response(200, IrisPredict)
    def post(self, features):
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