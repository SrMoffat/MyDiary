from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.secret_key = "4fr0c0d3th1ng5"

from app import views