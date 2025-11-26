from flask import Flask, render_template

from src.config import Config, csrf, bcrypt, login_manager
from src.models import db, init_create_table
from src.routes import main

app = Flask(__name__)

app.config.from_object(Config)

login_manager.init_app(app)
login_manager.login_view = "main.signin"

csrf.init_app(app)

db.init_app(app)
init_create_table(app)

bcrypt.init_app(app)

app.register_blueprint(main)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8181, debug=True)
