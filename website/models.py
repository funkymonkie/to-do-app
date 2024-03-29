from . import db
from sqlalchemy import func


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300), unique=True)
    complete = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, server_default=func.now())
    date_completed = db.Column(db.DateTime, nullable=True)
