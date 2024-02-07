from flask.views import MethodView
from flask_smorest import Blueprint

bp = Blueprint("mlp", __name__, description="Operations on mlp")

@bp.route("/todo")
class Todo(MethodView):
    @bp.arguments(TodoSchema)
    @bp.response(200,TodoSchema(many=True))
    def get(self):
        todos = TodoModel.query.all()
        return todos