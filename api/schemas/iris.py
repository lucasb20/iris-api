from marshmallow import Schema, fields

class IrisFeatures(Schema):
    Sepal_Length = fields.Float(required=True)
    Sepal_Width = fields.Float(required=True)
    Petal_Length = fields.Float(required=True)
    Petal_Width = fields.Float(required=True)

class IrisPredict(IrisFeatures):
    Specie = fields.String()