import secrets, string
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation)
                                   for _ in range(32))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# weird import structure to avoid bad importing
from DFWeb_app import routes
