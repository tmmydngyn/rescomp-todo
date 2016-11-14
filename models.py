from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    completed = db.Column(db.Boolean)
    
    def __init__(self, description, completed, priority):
        self.description = description
        self.completed = completed

    def __repr__(self):
        return self.description

