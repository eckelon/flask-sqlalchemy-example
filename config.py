import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_username = os.environ.get("DB_USERNAME", "root")
db_password = os.environ.get("DB_PASSWORD", "mysql")
db_host = os.environ.get("DB_HOST", "0.0.0.0")
db_port = os.environ.get("DB_PORT", "3808")
db_name = os.environ.get("DB_NAME", "todoapp")

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
