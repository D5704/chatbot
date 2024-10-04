import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
print("Chemins de recherche des templates :", app.template_folder)

# Configurer la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chatbot_user:57046943@localhost/chatbot_saoudibank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialiser SQLAlchemy
db = SQLAlchemy(app)

# Initialiser Flask-Migrate pour la gestion des migrations
migrate = Migrate(app, db)

from app import routes, models
