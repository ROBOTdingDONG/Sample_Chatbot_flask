from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(500))
    dialogue = db.Column(db.String(500))
    image_path = db.Column(db.String(200))
