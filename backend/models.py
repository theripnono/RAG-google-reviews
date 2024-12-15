from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(400))

    def __init__(self, title, description):
        self.title = title
        self.description = description

class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')
