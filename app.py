import os
from flask import (
    Flask, flash, render_template,
    redirect, session, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId #MongoDB stores its data BSON, we need to render the ObjectId in order to find documents from MongoDB
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_products")
def get_products():
    products = mongo.db.products.find()
    return render_template("products.html", products=products)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
