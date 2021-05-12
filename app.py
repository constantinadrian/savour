import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, json)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import login_required
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
    categories = mongo.db.recipes.distinct("categoryName")
    recipes = mongo.db.recipes.aggregate([{'$sample': {'size': 3}}])
    return render_template("pages/index.html",
                           recipes=recipes,
                           categories=categories)


@app.route("/recipe/<recipe_id>", methods=["GET", "POST"])
def recipe(recipe_id):
    """
    Display the recipe on-page for each recipe id that was requested
    """
    # Update the rating if it's an AJAX call
    if request.method == "POST":
        rating = request.form.get("stars")
        return json.dumps({'status': 'OK', 'rating': rating})

    page = "recipe"
    categories = mongo.db.recipes.distinct("categoryName")
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("pages/recipe.html",
                           recipe=recipe,
                           page=page,
                           categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Display the login page and check for authentofication
    """
    if request.method == "POST":
        # make check on server side before sending data on database
        username = request.form.get("username").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()
        password_confirmation = request.form.get(
            "passwordConfirmation").strip()

        if not username:
            flash("You must provide a username", category="alert-danger")
            return redirect("/register")

        if not email:
            flash("You must provide a email", category="alert-danger")
            return redirect("/register")

        if password != password_confirmation:
            flash("Password does not match", category="alert-danger")
            return redirect("/register")

        exist_user = mongo.db.users.find_one({"username": username.lower()})
        exist_email = mongo.db.users.find_one({"email": email.lower()})

        if exist_user and exist_email:
            flash("Username and email already in use", category="alert-danger")
            return redirect("/register")

        if exist_user:
            flash("Username already in use", category="alert-danger")
            return redirect("/register")

        if exist_email:
            flash("Email already in use", category="alert-danger")
            return redirect("/register")

        new_user = {
            "username": username.lower(),
            "email": email,
            "password": generate_password_hash(password)
        }

        mongo.db.users.insert_one(new_user)

        session["user"] = username.lower()
        flash("Registration Successful!", category="alert-success")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.recipes.distinct("categoryName")
    page = "form"
    return render_template("pages/register.html",
                           page=page,
                           categories=categories)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Display the login page and check for authentofication
    """
    if request.method == "POST":
        if not request.form.get("email"):
            flash("You must provide a email", category="alert-danger")
            return redirect("/login")

        if not request.form.get("password"):
            flash("You must provide a password", category="alert-danger")
            return redirect("/login")

        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")})
        if not existing_user or not check_password_hash(
                existing_user["password"], request.form.get("password")):
            flash("Incorrect Email and/or Password", category="alert-danger")
            return redirect("/login")

        session["user"] = existing_user["username"]
        return redirect(url_for(
                    "profile", username=session["user"]))

    categories = mongo.db.recipes.distinct("categoryName")
    page = "form"
    return render_template("pages/login.html",
                           page=page,
                           categories=categories)


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    """
    Display the profile page
    """
    # Denied user access to other profile pages
    if username != session["user"]:
        return redirect(url_for('permission', code=403))

    categories = mongo.db.recipes.distinct("categoryName")
    recipes = mongo.db.recipes.find({"createdBy": username.lower()})
    return render_template("pages/profile.html",
                           username=username,
                           recipes=recipes,
                           categories=categories)


@app.route("/logout")
def logout():
    """
    Log out the user
    """
    # Remove user from session cookies
    session.pop("user")
    flash("You have been logged out", category="alert-info")
    return redirect("/login")


@app.errorhandler(401)
def http_unauthorized(e):
    return redirect(url_for('permission', code=401))


@app.errorhandler(403)
def http_forbidden(e):
    return redirect(url_for('permission', code=403))


@app.route("/permission/<code>")
def permission(code):
    """
    Show user permission to the page
    """
    categories = mongo.db.recipes.distinct("categoryName")
    return render_template("pages/permission.html", 
                           code=code, 
                           categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
