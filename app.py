import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, json)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    """
    Display three random recipes on home page
    """
    recipes = mongo.db.recipes.aggregate([{'$sample': {'size': 3}}])
    return render_template("pages/index.html", recipes=recipes)


@app.route("/recipe/<recipe_id>", methods=["GET", "POST"])
def recipe(recipe_id):
    """
    Display the recipe on-page for each recipe id that was requested
    """
    # Update the rating if it's an AJAX call
    if request.method == "POST":
        print("ajax request")
        rating = request.form.get("stars")
        return json.dumps({'status': 'OK', 'rating': rating})

    page = "recipe"
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("pages/recipe.html", recipe=recipe, page=page)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Display the login page and check for authentofication
    """
    if request.method == "POST":
        return redirect("/home")

    page = "form"
    return render_template("pages/login.html", page=page)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
