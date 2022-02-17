from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_restful import Resource, Api
from flask_migrate import Migrate

from backend.forms.forms import AddForm, SearchForm
from backend.src.tools.parser import parse_input
from backend.models.models import db, ItemModel
from backend.models.marshmallow_models import ma, ItemModelSchema
from config import config, config_name


def create_app():
    app = Flask(__name__, template_folder=config[config_name].TEMPLATES_DIR)
    app.config.from_object(config[config_name])
    db.init_app(app)
    ma.init_app(app)
    api = Api(app)
    migrate = Migrate(app, db)

    item_schema = ItemModelSchema()
    items_schema = ItemModelSchema(many=True)

    @app.route("/", methods=['POST', 'GET'])
    def index():
        add_form = AddForm()
        search_form = SearchForm()
        items=ItemModel.query.all()
        if request.method == 'POST' and add_form.validate_on_submit():
            try:
                data = parse_input(add_form.input_item.data, request.method)
                item = item_schema.load(data)
                db.session.add(item)
                db.session.commit()
            except Exception as e:
                return(str(e))
            return redirect(url_for('index'))
        if request.method == 'GET' and request.args.get('input_search'):
            input_search = parse_input(request.args.get('input_search'))
            item_index = []
            for count, item in enumerate(items):
                if item.filter_item(input_search) == False:
                    item_index.append(count)
            for index in item_index[::-1]:
                del items[index]
        return render_template(
            'index.html',
            forms={'add_form':add_form, 'search_form':search_form},
            items=items[::-1]
            )

    class Item(Resource):
        def get(self, id):
            try:
                item = ItemModel.query.get(id)
                return item_schema.jsonify(item)
            except Exception as e:
                return {'message': 'can not get item', 'error': str(e)}, 500

        def delete(self, id):
            try:
                item = ItemModel.query.get(id)
                db.session.delete(item)
                db.session.commit()
                return item_schema.jsonify(item)
            except Exception as e:
                return {'message': 'can not delete item', 'error': str(e)}, 500

        def put(self, id):
            data = request.get_json()
            try:
                item = ItemModel.query.get(id)
                item.name = data['name']
                item.type = data.get('type', None)
                item.count = data.get('count', None)
                db.session.commit()
                return item_schema.jsonify(item)
            except Exception as e:
                return {'message': 'can not change item', 'error': str(e)}, 400

    class Items(Resource):
        def get(self):
            try:
                items=ItemModel.query.all()
                return jsonify(items_schema.dump(items))
            except Exception as e:
                return {'message': 'can not get items', 'error': str(e)}, 500

        def post(self):
            data = request.get_json()
            try:
                name = data['name']
                type = data.get('type', None)
                count = data.get('count', None)
                new_item = ItemModel(name, type, count)
                db.session.add(new_item)
                db.session.commit()
                return item_schema.jsonify(new_item)
            except Exception as e:
                return {'message': 'can not add item', 'error': str(e)}, 400

    api.add_resource(Items, '/api/v1/items')
    api.add_resource(Item, '/api/v1/items/<int:id>')

    return app
