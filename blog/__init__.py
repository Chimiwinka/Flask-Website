# Main core for the code (app and the db)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Creates an application
app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = "####################################"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "blog.db").
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://"####################"  # Combining that directory with file name for diff systems

# Use library for the database
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


from blog import routes
