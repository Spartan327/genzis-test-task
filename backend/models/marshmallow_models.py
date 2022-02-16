from flask_marshmallow import Marshmallow

from backend.models.models import ItemModel


ma = Marshmallow()

class ItemModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_instance = True