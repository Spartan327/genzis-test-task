from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=True)
    count = db.Column(db.Integer, nullable=True)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, type=None, count=None):
        self.name = name
        self.type = type
        self. count = count

    def __repr__(self):
        return f"<Item({self.name})>"

    def filter_item(self, input_search):
        for search_word in input_search:
            if self.name == search_word: return True
            if self.type == search_word: return True
            if str(self.count) == search_word: return True
        return False
