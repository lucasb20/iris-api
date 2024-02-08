from flask.views import MethodView
from flask_smorest import Blueprint
from joblib import load

bp = Blueprint("mlp", __name__, description="Operations on mlp")

@bp.route("/iris")
class Iris(MethodView):
    @bp.arguments(TodoSchema)
    @bp.response(200,TodoSchema(many=True))
    def get(self, features):
        model = load('model.joblib')
        predict = model.predict(**features)
        return {**features, predict: predict}