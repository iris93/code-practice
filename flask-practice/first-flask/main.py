from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"


class User(db.Model):
    """docstring fo User."""
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        super(User, self).__init__()
        self.username = username
    def __repr__(self):
        return "<User `{}`>".format(self.username)



@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()
