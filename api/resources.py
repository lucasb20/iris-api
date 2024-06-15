from flask import Blueprint, request, jsonify
import onnxruntime as rt
import numpy as np

bp = Blueprint("Predict", __name__, url_prefix="/predict")

sess = rt.InferenceSession("model.onnx", providers=["CPUExecutionProvider"])
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

@bp.route("/", methods=['POST'])
def predict():
    data = request.get_json()
    if 'features' not in data or not isinstance(data['features'], list) or len(data['features']) != 4:
        return jsonify({'message': 'invalid features field'}), 404

    data = np.array([data['features']], dtype=np.float32)

    pred_onx = sess.run([label_name], {input_name: data})[0]
    predict_str = ["setosa", "versicolor", "virginica"][pred_onx[0]]

    return {'predict': predict_str}