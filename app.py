import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, json)
from flask_pymongo import PyMongo
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import login_required, update_recipe_rating, is_valid, check_form
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
    nav_categories = mongo.db.recipes.distinct("category_name")
    recipes = mongo.db.recipes.aggregate([{'$sample': {'size': 3}}])
    products = mongo.db.shop.aggregate([{'$sample': {'size': 3}}])
    return render_template("pages/index.html",
                           recipes=recipes,
                           products=products,
                           nav_categories=nav_categories)


@app.route("/all_recipes", methods=["GET", "POST"])
def all_recipes():
    """
    Display all recipes
    """
    nav_categories = mongo.db.recipes.distinct("category_name")
    sugestion_recipe = mongo.db.recipes.aggregate([{'$sample': {'size': 1}}])
    recipes = mongo.db.recipes.find()
    page_set = {
        "title": "Recipes"
    }
    return render_template("pages/all_recipes.html",
                           nav_categories=nav_categories,
                           sugestion_recipe=sugestion_recipe,
                           recipes=recipes,
                           page_set=page_set)


@app.route("/category/<category>", methods=["GET", "POST"])
def category(category):
    """
    Display recipes from requested category
    """
    check_category = mongo.db.recipes.count_documents(
        {"category_name": category})
    if not check_category:
        return redirect(url_for('error', code=404))

    nav_categories = mongo.db.recipes.distinct("category_name")
    recipes = mongo.db.recipes.find({"category_name": category})

    page_set = {
        "title": category.title()
    }
    return render_template("pages/category.html",
                           recipes=recipes,
                           nav_categories=nav_categories,
                           page_set=page_set,
                           category=category)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Display the search query that was requested
    """
    if request.method == "POST":
        query = request.form.get("query")
        nav_categories = mongo.db.recipes.distinct("category_name")
        recipes = mongo.db.recipes.find({"$text": {"$search": query}})

        page_set = {
            "title": "Search"
        }
        return render_template("pages/search.html",
                               recipes=recipes,
                               page_set=page_set,
                               nav_categories=nav_categories)
    return redirect(url_for("home"))


@app.route("/users/<username>", methods=["GET", "POST"])
def users(username):
    """
    Display the search query that was requested
    """
    user_found = mongo.db.users.find_one({"username": username.lower()})
    if not user_found:
        return redirect(url_for('error', code=404))

    nav_categories = mongo.db.recipes.distinct("category_name")
    recipes = mongo.db.recipes.find({"created_by": username.lower()})

    page_set = {
        "title": username.title()
    }
    return render_template("pages/search.html",
                           recipes=recipes,
                           page_set=page_set,
                           nav_categories=nav_categories)


@app.route("/recipe/<recipe_id>", methods=["GET", "POST"])
def recipe(recipe_id):
    """
    Display the recipe on-page for each recipe id that was requested
    """
    # Update the rating if it's an AJAX call
    if request.method == "POST":
        # check if user is login in order to proceed with rating
        if not session:
            return json.dumps({'status': 'not logged in'})

        # check if the recipe id hasn't been change
        if not is_valid(recipe_id):
            return json.dumps({'status': 'error'})

        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

        # if user want to rate it's own recipe return denied
        if recipe["created_by"] == session["user"]:
            return json.dumps({'status': 'denied'})

        # check if user didn't altered the form value
        new_rating = request.form.get("stars")
        if int(new_rating) > 0 and int(new_rating) <= 5:
            rating = update_recipe_rating(mongo, new_rating, recipe)
            return json.dumps({'status': 'success', 'rating': rating})

        return json.dumps({'status': 'error'})

    # check if the recipe id hasn't been change
    if not is_valid(recipe_id):
        return redirect(url_for('error', code=404))

    nav_categories = mongo.db.recipes.distinct("category_name")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # added in case the owner decide to delete the recipe while
    # other users might by on this recipe page and cause an error
    # after refresh the page as we access the recipe["recipe_name"] on page_set
    # due to access None["recipe_name"]
    if not recipe:
        return redirect(url_for('error', code=404))

    page_set = {
        "title": recipe["recipe_name"].title(),
        "type": "recipe"
    }
    return render_template("pages/recipe.html",
                           recipe=recipe,
                           page_set=page_set,
                           nav_categories=nav_categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Display the login page and check for authentication
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
            "email": email.lower(),
            "password": generate_password_hash(password)
        }

        mongo.db.users.insert_one(new_user)

        session["user"] = username.lower()
        flash("Registration Successful!", category="alert-success")
        return redirect(url_for("profile", username=session["user"]))

    nav_categories = mongo.db.recipes.distinct("category_name")
    page_set = {
        "title": "Register",
        "type": "form"
    }
    return render_template("pages/register.html",
                           page_set=page_set,
                           nav_categories=nav_categories)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Display the login page and check for authentication
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

    nav_categories = mongo.db.recipes.distinct("category_name")
    page_set = {
        "title": "Login",
        "type": "form"
    }
    return render_template("pages/login.html",
                           page_set=page_set,
                           nav_categories=nav_categories)


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    """
    Display the profile page
    """
    # Denied user access to other profile pages
    if username != session["user"]:
        return redirect(url_for('error', code=403))

    nav_categories = mongo.db.recipes.distinct("category_name")
    recipes = mongo.db.recipes.find({"created_by": username.lower()})

    page_set = {
        "title": "Profile"
    }
    return render_template("pages/profile.html",
                           username=username,
                           page_set=page_set,
                           recipes=recipes,
                           nav_categories=nav_categories)


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    """
    Display the form for add recipe
    """
    if request.method == "POST":
        # check if all fields has been completed
        # for the ingredient and methods we can only check for the first item
        # as request.form.items() does not take the
        # array of same key but only the first value
        form_data = check_form(list(request.form.items()))

        if not form_data:
            flash("All Recipe Fields Must be Completed",
                  category="alert-warning")
            return redirect('/add_recipe')

        new_recipe = {
            "category_name": request.form.get("recipe-category").strip(),
            "recipe_name": request.form.get("recipe-title").strip(),
            "description": request.form.get("recipe-description").strip(),
            "image_url": request.form.get("recipe-image-url").strip(),
            "ingredients": request.form.getlist("recipe-ingredient"),
            "methods": request.form.getlist("recipe-methods"),
            "tips": request.form.get("recipe-tips").strip(),
            "time": request.form.get("recipe-cook-time"),
            "serve": request.form.get("recipe-serve"),
            "ratings": {
                "status": False,
                "number_of_ratings": 0,
                "weighted_average": 0.0,
                "rated_stars": {
                    "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 0,
                    "5": 0}},
            "created_by": session["user"]
        }
        recipe_id = mongo.db.recipes.insert_one(new_recipe).inserted_id
        flash("Recipe Added Successfully", category="alert-success")
        return redirect(url_for('recipe', recipe_id=recipe_id))

    page_set = {
        "title": "Add Recipe",
        "type": "form",
        "route": "add_recipe"
    }
    nav_categories = mongo.db.recipes.distinct("category_name")
    categories_recipes = mongo.db.categories.find().sort("category_name", 1)
    return render_template("pages/add_recipe.html",
                           page_set=page_set,
                           categories_recipes=categories_recipes,
                           nav_categories=nav_categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """
    Display the form for edit recipe
    """
    if request.method == "POST":
        # check if the recipe id hasn't been change
        if not is_valid(recipe_id):
            return redirect(url_for('error', code=404))

        # check if all fields has been completed
        # for the ingredient and methods we can only check for the first item
        # as request.form.items() does not take the
        # array of same key but only the first value
        form_data = check_form(list(request.form.items()))

        if not form_data:
            flash("All Recipe Fields Must be Completed",
                  category="alert-warning")
            return redirect(url_for('edit_recipe', recipe_id=recipe_id))

        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)},
            {
                "$set": {
                    "category_name": request.form.get(
                        "recipe-category").strip(),
                    "recipe_name": request.form.get("recipe-title").strip(),
                    "description": request.form.get(
                        "recipe-description").strip(),
                    "image_url": request.form.get("recipe-image-url").strip(),
                    "ingredients": request.form.getlist("recipe-ingredient"),
                    "methods": request.form.getlist("recipe-methods"),
                    "tips": request.form.get("recipe-tips").strip(),
                    "time": request.form.get("recipe-cook-time"),
                    "serve": request.form.get("recipe-serve")
                }
            }
        )
        flash("Recipe Edited Successfully", category="alert-success")
        return redirect(url_for('recipe', recipe_id=recipe_id))

    # check if the recipe id hasn't been change
    if not is_valid(recipe_id):
        return redirect(url_for('error', code=404))

    page_set = {
        "title": "Edit Recipe",
        "type": "form",
        "route": "edit_recipe"
    }
    nav_categories = mongo.db.recipes.distinct("category_name")
    categories_recipes = mongo.db.categories.find().sort("category_name", 1)
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("pages/add_recipe.html",
                           page_set=page_set,
                           recipe=recipe,
                           categories_recipes=categories_recipes,
                           nav_categories=nav_categories)


@app.route("/delete", methods=["POST"])
@login_required
def delete():
    """
    Display the form for edit recipe
    """
    delete_item_id = request.form.get("delete-item-id")
    delete_item = request.form.get("delete-item")

    # check if the recipe id hasn't been change
    if not is_valid(delete_item_id):
        return redirect(url_for('error', code=404))

    if not delete_item:
        return redirect(url_for('error', code=404))

    if delete_item == "recipe":
        mongo.db.recipes.delete_one({"_id": ObjectId(delete_item_id)})
        mongo.db.userRatings.delete_many(
            {"recipe_id": ObjectId(delete_item_id)})
        flash("Recipe Deleted Successfully", category="alert-success")
        return redirect(url_for(
                "profile", username=session["user"]))

    elif delete_item == "category":
        # Denied user access from delete categories
        if session["user"] != "admin":
            return redirect(url_for('error', code=403))

        # revoke delete category if category already has one or more recipes
        category = mongo.db.categories.find_one(
            {"_id": ObjectId(delete_item_id)})
        check_category = mongo.db.recipes.count_documents(
            {"category_name": category["category_name"]})
        if check_category:
            flash("Cannot Delete Category", category="alert-danger")
            flash("Category Already in Use", category="alert-danger")
            return redirect(url_for(
                "profile", username=session["user"]))

        mongo.db.categories.delete_one({"_id": ObjectId(delete_item_id)})
        flash("Category Deleted Successfully", category="alert-success")
        return redirect(url_for(
                "profile", username=session["user"]))

    return redirect(url_for('error', code=404))


@app.route("/manage_categories", methods=["GET", "POST"])
@login_required
def manage_categories():
    """
    Display the all categories
    """

    # Denied user access to manage_categories page
    if session["user"] != "admin":
        return redirect(url_for('error', code=403))

    page_set = {
        "title": "Manage Categories",
        "type": "form"
    }
    manage_categories = mongo.db.categories.find().sort("category_name", 1)
    nav_categories = mongo.db.recipes.distinct("category_name")
    return render_template("pages/manage_categories.html",
                           page_set=page_set,
                           nav_categories=nav_categories,
                           manage_categories=manage_categories)


@app.route("/add_categories", methods=["POST"])
@login_required
def add_categories():
    """
    Add categories or edit categories
    """

    # Denied user access to manage_categories page
    if session["user"] != "admin":
        return redirect(url_for('error', code=403))

    category_id = request.form.get("category-id")
    category_type = request.form.get("category-type")
    category_name = request.form.get("category-name").strip()

    # if no category name provided return error
    if not category_name:
        return redirect(url_for('error', code=404))

    # check if user wants to add or edit category
    if category_type == "Add Category":

        check_category = mongo.db.categories.count_documents(
            {"category_name": category_name.lower()})

        if check_category:
            flash("Category Already Exists", category="alert-warning")
            return redirect(url_for('manage_categories'))

        new_category = {
            "category_name": category_name.lower()
        }
        mongo.db.categories.insert_one(new_category)

        flash("Category Added Successfully", category="alert-success")
        return redirect(url_for('manage_categories'))

    elif category_type == "Edit Category":
        # check if the category id hasn't been change
        if not is_valid(category_id):
            return redirect(url_for('error', code=404))

        # update category name in category collection
        old_category = mongo.db.categories.find_one_and_update(
            {"_id": ObjectId(category_id)},
            {
                "$set": {
                    "category_name": category_name.lower()
                }
            },
            return_document=ReturnDocument.BEFORE
        )
        # update category name in recipe collection
        mongo.db.recipes.update_many(
            {"category_name": old_category["category_name"]},
            {
                "$set": {
                    "category_name": category_name.lower()
                }
            }
        )

        flash("Category Edited Successfully", category="alert-success")
        return redirect(url_for('manage_categories'))

    return redirect(url_for('error', code=404))


@app.route("/logout")
@login_required
def logout():
    """
    Log out the user
    """
    # Remove user from session cookies
    session.pop("user")
    flash("You have been logged out", category="alert-info")
    return redirect("/login")


@app.route("/shop", methods=["GET", "POST"])
def shop():
    """
    Display the shop page
    """
    if request.method == "POST":
        # get the query search
        query = request.form.get("query")

        # get the requested product(s)
        products = mongo.db.shop.find({"$text": {"$search": query}})

        page_set = {
            "title": "Kitchen Tools"
        }

        # get the nav categories
        nav_categories = mongo.db.recipes.distinct("category_name")

        # get the recomanded products
        recommended_products = mongo.db.shop.find({
            "$or": [
                {"_id": ObjectId("60a51442da1161837d99ef35")},
                {"_id": ObjectId("60a514f3da1161837d99ef36")},
                {"_id": ObjectId("60a51a00da1161837d99ef3c")}
            ]
        })
        return render_template("pages/shop.html",
                               page_set=page_set,
                               nav_categories=nav_categories,
                               products=products,
                               recommended_products=recommended_products)

    products = mongo.db.shop.find()

    page_set = {
        "title": "Kitchen Tools"
    }

    nav_categories = mongo.db.recipes.distinct("category_name")

    recommended_products = mongo.db.shop.find({
        "$or": [
            {"_id": ObjectId("60a51442da1161837d99ef35")},
            {"_id": ObjectId("60a514f3da1161837d99ef36")},
            {"_id": ObjectId("60a51a00da1161837d99ef3c")}
        ]
    })
    return render_template("pages/shop.html",
                           page_set=page_set,
                           nav_categories=nav_categories,
                           products=products,
                           recommended_products=recommended_products)


@app.route("/contact", methods=["GET"])
def contact():
    """
    Display the contact page
    """
    page_set = {
        "title": "Contact",
        "type": "form"
    }
    nav_categories = mongo.db.recipes.distinct("category_name")

    return render_template("pages/contact.html",
                           page_set=page_set,
                           nav_categories=nav_categories)


@app.route("/subscribe_ajax", methods=["POST"])
def subscribe_ajax():
    """
    Display the message after the user subscribe to out newsletter
    """
    # check if user sent the 'email address' and not an empty form
    if not request.form.get("email"):
        return json.dumps({'status': 'error'})

    # check if the email is already in our subscriptions
    email_exists = mongo.db.subscriptions.count_documents(
        {"email": request.form.get("email").strip().lower()})

    # if user want to rate it's own recipe return denied
    if email_exists:
        return json.dumps({'status': 'already subscribed'})

    # insert new email in out database
    subscribed_email = mongo.db.subscriptions.insert_one(
        {"email": request.form.get("email").strip().lower()}).inserted_id
    if subscribed_email:
        return json.dumps({'status': 'success'})

    return json.dumps({'status': 'error'})


@app.route("/terms_and_conditions", methods=["GET"])
def terms_and_conditions():
    """
    Display the terms and conditions page
    """
    page_set = {
        "title": "Terms and Conditions"
    }
    nav_categories = mongo.db.recipes.distinct("category_name")
    return render_template("pages/terms_conditions.html",
                           page_set=page_set,
                           nav_categories=nav_categories)


@app.errorhandler(401)
def http_unauthorized(e):
    return redirect(url_for('error', code=401))


@app.errorhandler(403)
def http_forbidden(e):
    return redirect(url_for('error', code=403))


@app.errorhandler(404)
def http_not_found(e):
    return redirect(url_for('error', code=404))


@app.route("/error/<code>")
def error(code):
    """
    Show user error to the page
    """
    if code == "401":
        title = "Authorization Required"
    elif code == "403":
        title = "Access Forbidden"
    elif code == "404":
        title = "Page Not Found"

    page_set = {
        "title": title,
        "code": code
    }
    nav_categories = mongo.db.recipes.distinct("category_name")
    return render_template("pages/error.html",
                           page_set=page_set,
                           nav_categories=nav_categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
