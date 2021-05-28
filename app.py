import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, json, abort)
from flask_pymongo import PyMongo
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import login_required, update_recipe_rating, is_valid, check_form
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Pagination for recipes was inspired from this two website
# and modified and adapted to my understanding on my project
# Credit code
#    https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
# Credit code https://harishvc.com/2015/04/15/pagination-flask-mongodb/
PER_PAGE = 6


def get_page_items():
    # get the page number
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        abort(404)

    # get the per_page items
    per_page = request.args.get('per_page')
    if not per_page:
        per_page = PER_PAGE
    else:
        try:
            per_page = int(per_page)
        except ValueError:
            abort(404)

    # calculate the offset
    offset = (page - 1) * per_page

    return page, per_page, offset


def get_css_framework():
    return 'bootstrap4'


def get_link_size():
    return 'sm'


def paginated(recipes):
    page, per_page, offset = get_page_items()
    return recipes[offset: offset + per_page]


def get_pagination(recipes):
    page, per_page, offset = get_page_items()
    total = len(recipes)
    return Pagination(css_framework=get_css_framework(),
                      link_size=get_link_size(),
                      page=page,
                      per_page=per_page,
                      offset=offset,
                      total=total
                      )
# End Credit code


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    """
    Display three random recipes on home page and
    three kitchen tools
    """
    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # get three sample recipe to display on home page
    recipes = mongo.db.recipes.aggregate([{'$sample': {'size': 3}}])

    # get three sample kitchen tools to display on home page
    products = mongo.db.shop.aggregate([{'$sample': {'size': 3}}])

    page_set = {
        "type": "form"
    }
    return render_template("pages/index.html",
                           recipes=recipes,
                           products=products,
                           nav_categories=nav_categories,
                           page_set=page_set)


@app.route("/all_recipes", methods=["GET", "POST"])
def all_recipes():
    """
    Display all recipes
    """
    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # show one recipe as suggest recipe for users when access
    # the recipes page
    sugestion_recipe = mongo.db.recipes.aggregate([{'$sample': {'size': 1}}])

    # the query for existing recipes on the database
    recipes = list(mongo.db.recipes.find())

    # call the paginated function to display only the
    # specific number of recipes per page
    paginated_recipes = paginated(recipes)

    # get the page pagination
    pagination = get_pagination(recipes)

    # total number of recipes found
    total = len(recipes)

    # set up the page_set object
    page_set = {
        "title": "Recipes",
        "type": "form"
    }
    return render_template("pages/all_recipes.html",
                           nav_categories=nav_categories,
                           sugestion_recipe=sugestion_recipe,
                           recipes=paginated_recipes,
                           pagination=pagination,
                           total=total,
                           page_set=page_set)


@app.route("/category/<category>", methods=["GET", "POST"])
def category(category):
    """
    Display recipes from requested category
    """
    # see if there are any recipes for specific
    # category on the database
    check_category = mongo.db.recipes.count_documents(
        {"category_name": category})

    # return page not found if no recipes found
    # for the specific category
    if not check_category:
        return redirect(url_for('error', code=404))

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # the query for existing recipes on the database for specific category
    recipes = list(mongo.db.recipes.find({"category_name": category}))

    # call the paginated function to display only the
    # specific number of recipes per page
    paginated_recipes = paginated(recipes)

    # get the page pagination
    pagination = get_pagination(recipes)
    total = len(recipes)

    # set up the page_set object
    page_set = {
        "title": category.title(),
        "type": "form"
    }
    return render_template("pages/category.html",
                           recipes=paginated_recipes,
                           pagination=pagination,
                           total=total,
                           nav_categories=nav_categories,
                           page_set=page_set,
                           category=category)


@app.route("/category/<category>/search", methods=["GET", "POST"])
def category_search(category):
    """
    Display the search recipes from requested category only
    """
    # get the search query
    query = request.args.get('query')

    # if no query return page not found
    if not query:
        return redirect(url_for('error', code=404))

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # the query for existing recipes on the database for specific search query
    recipes = list(mongo.db.recipes.find(
        {"category_name": category, "$text": {"$search": query}}))

    # call the paginated function to display only the
    # specific number of recipes per page
    paginated_recipes = paginated(recipes)

    # get the page pagination
    pagination = get_pagination(recipes)

    # total number of recipes found
    total = len(recipes)

    # set up the page_set object
    page_set = {
        "title": "Search",
        "type": "form"
    }
    return render_template("pages/category.html",
                           recipes=paginated_recipes,
                           pagination=pagination,
                           total=total,
                           nav_categories=nav_categories,
                           page_set=page_set,
                           category=category)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Display the search query that was requested
    """
    # get the search query
    query = request.args.get('query')

    # if no query return page not found
    if not query:
        return redirect(url_for('error', code=404))

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # the query for existing recipes on the database for specific search query
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    # call the paginated function to display only the
    # specific number of recipes per page
    paginated_recipes = paginated(recipes)

    # get the page pagination
    pagination = get_pagination(recipes)

    # total number of recipes found
    total = len(recipes)

    # set up the page_set object
    page_set = {
        "title": "Search",
        "type": "form"
    }
    return render_template("pages/search.html",
                           recipes=paginated_recipes,
                           pagination=pagination,
                           total=total,
                           page_set=page_set,
                           nav_categories=nav_categories)


@app.route("/users/<username>", methods=["GET", "POST"])
def users(username):
    """
    Display the user page that was requested
    """
    # check if user exists on the database
    user_found = mongo.db.users.find_one({"username": username.lower()})

    # return page not found if invalid user
    if not user_found:
        return redirect(url_for('error', code=404))

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # the query to show the recipes from specific user on the database
    recipes = list(mongo.db.recipes.find({"created_by": username.lower()}))

    # call the paginated function to display only the
    # specific number of recipes per page
    paginated_recipes = paginated(recipes)

    # get the page pagination
    pagination = get_pagination(recipes)

    # total number of recipes found
    total = len(recipes)

    # set up the page_set object
    page_set = {
        "title": username.title()
    }
    return render_template("pages/search.html",
                           recipes=paginated_recipes,
                           pagination=pagination,
                           total=total,
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

        # the query for the specific recipe that has to be rated
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

        # if user want to rate it's own recipe return denied
        if recipe["created_by"] == session["user"]:
            return json.dumps({'status': 'denied'})

        # check if user didn't altered the form value
        new_rating = request.form.get("stars")
        if int(new_rating) > 0 and int(new_rating) <= 5:
            # update the recipe rating
            rating = update_recipe_rating(mongo, new_rating, recipe)
            return json.dumps({'status': 'success', 'rating': rating})

        return json.dumps({'status': 'error'})

    # check if the recipe id hasn't been change
    if not is_valid(recipe_id):
        return redirect(url_for('error', code=404))

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # the query for the specific recipe that the user wants to access
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # added in case the owner decide to delete the recipe while
    # other users might by on this recipe page and cause an error
    # after refresh the page as we access the recipe["recipe_name"] on page_set
    # due to access None["recipe_name"]
    if not recipe:
        return redirect(url_for('error', code=404))

    # set up the page_set object
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
        # make a check on the server-side before sending data to the database
        # remove any trail of white spaces from
        # the beginning or end of each string
        username = request.form.get("username").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()
        password_confirmation = request.form.get(
            "passwordConfirmation").strip()

        # if no username provided alert the user
        if not username:
            flash("You must provide a username", category="alert-danger")
            return redirect("/register")

        # if no emali provided alert the user
        if not email:
            flash("You must provide a email", category="alert-danger")
            return redirect("/register")

        # if password does match confirmation password alert the user
        if password != password_confirmation:
            flash("Password does not match", category="alert-danger")
            return redirect("/register")

        # check if the username/email is not already reqister
        # this is because the username and email have to be unique to each user
        exist_user = mongo.db.users.find_one({"username": username.lower()})
        exist_email = mongo.db.users.find_one({"email": email.lower()})

        # alert the user if username and email is already in use
        if exist_user and exist_email:
            flash("Username and email already in use", category="alert-danger")
            return redirect("/register")

        # if we found that username already exist alert the user
        if exist_user:
            flash("Username already in use", category="alert-danger")
            return redirect("/register")

        # if we found that email already exist alert the user
        if exist_email:
            flash("Email already in use", category="alert-danger")
            return redirect("/register")

        # create obj to the new user
        new_user = {
            "username": username.lower(),
            "email": email.lower(),
            "password": generate_password_hash(password)
        }

        # insert the new user into database
        mongo.db.users.insert_one(new_user)

        # login the user and redirect to his profile page
        session["user"] = username.lower()
        flash("Registration Successful!", category="alert-success")
        return redirect(url_for("profile", username=session["user"]))

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # set up the page_set object
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
        # check if user provided an email
        if not request.form.get("email"):
            flash("You must provide a email", category="alert-danger")
            return redirect("/login")

        # check if user provided an password
        if not request.form.get("password"):
            flash("You must provide a password", category="alert-danger")
            return redirect("/login")

        # query the users database for the specific email
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        # check if there is any user with that email address and
        # that the provided password matches the existed password
        if not existing_user or not check_password_hash(
                existing_user["password"], request.form.get("password")):
            flash("Incorrect Email and/or Password", category="alert-danger")
            return redirect("/login")

        # login the user and redirect to his profile page
        session["user"] = existing_user["username"]
        return redirect(url_for(
                    "profile", username=session["user"]))

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # set up the page_set object
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

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # the query to show the recipes from specific user on the database
    recipes = list(mongo.db.recipes.find({"created_by": username.lower()}))

    # call the paginated function to display only the
    # specific number of recipes per page
    paginated_recipes = paginated(recipes)

    # get the page pagination
    pagination = get_pagination(recipes)

    # total number of recipes found
    total = len(recipes)

    # set up the page_set object
    page_set = {
        "title": "Profile"
    }
    return render_template("pages/profile.html",
                           username=username,
                           page_set=page_set,
                           recipes=paginated_recipes,
                           pagination=pagination,
                           total=total,
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

        # create new recipe obj
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

        # insert the new recipe into database and return
        # the new ObjectId for that recipe
        recipe_id = mongo.db.recipes.insert_one(new_recipe).inserted_id

        # redirect the user to the new recipe page and show the success message
        flash("Recipe Added Successfully", category="alert-success")
        return redirect(url_for('recipe', recipe_id=recipe_id))

    # get all the categories that the admin has added in database
    # the user can select from these categories and add his
    # recipe accordingly to his selection
    categories_recipes = mongo.db.categories.find().sort("category_name", 1)

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # set up the page_set object
    page_set = {
        "title": "Add Recipe",
        "type": "form",
        "route": "add_recipe"
    }
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

        # update the recipe with the new changes
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

    # get all the categories that the admin has added in database
    # the user can select from these categories and add his
    # recipe accordingly to his selection
    categories_recipes = mongo.db.categories.find().sort("category_name", 1)

    # the query for the specific recipe that the user wants to access
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # set up the page_set object
    page_set = {
        "title": "Edit Recipe",
        "type": "form",
        "route": "edit_recipe"
    }
    return render_template("pages/add_recipe.html",
                           page_set=page_set,
                           recipe=recipe,
                           categories_recipes=categories_recipes,
                           nav_categories=nav_categories)


@app.route("/delete", methods=["POST"])
@login_required
def delete():
    """
    Delete the recipe/category
    """
    # get the id for the item that has to be deleted
    delete_item_id = request.form.get("delete-item-id")

    # take the type of item (recipe or category) that
    # the user/admin wants to delete
    delete_item = request.form.get("delete-item")

    # check if the id hasn't been change
    if not is_valid(delete_item_id):
        return redirect(url_for('error', code=404))

    # check if we have any type of item (recipe or category)
    if not delete_item:
        return redirect(url_for('error', code=404))

    # if the item is a recipe proceeds in deleting
    # the specific recipe base on the item id
    if delete_item == "recipe":

        # delete the recipe from recipes collection
        mongo.db.recipes.delete_one({"_id": ObjectId(delete_item_id)})

        # delete all the recipe ratings from userRatings collection
        mongo.db.userRatings.delete_many(
            {"recipe_id": ObjectId(delete_item_id)})

        # alert the user that recipe was successfully deleted
        flash("Recipe Deleted Successfully", category="alert-success")
        return redirect(url_for(
                "profile", username=session["user"]))

    # if the item is a category proceeds in deleting
    # the specific category base on the item id
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
            return redirect("/manage_categories")

        # delete the category from categories collection
        mongo.db.categories.delete_one({"_id": ObjectId(delete_item_id)})
        flash("Category Deleted Successfully", category="alert-success")
        return redirect("/manage_categories")

    return redirect(url_for('error', code=404))


@app.route("/manage_categories", methods=["GET", "POST"])
@login_required
def manage_categories():
    """
    Display all categories to manage categories page (admin only)
    """
    # Denied user access to manage_categories page
    if session["user"] != "admin":
        return redirect(url_for('error', code=403))

    # query for all categories from categories collection
    manage_categories = mongo.db.categories.find().sort("category_name", 1)

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # set up the page_set object
    page_set = {
        "title": "Manage Categories",
        "type": "form"
    }
    return render_template("pages/manage_categories.html",
                           page_set=page_set,
                           nav_categories=nav_categories,
                           manage_categories=manage_categories)


@app.route("/add_categories", methods=["POST"])
@login_required
def add_categories():
    """
    Add categories or edit categories (admin only)
    """
    # Denied user access to manage_categories page
    if session["user"] != "admin":
        return redirect(url_for('error', code=403))

    # get all the information in order to know
    # what type of request the admin wants
    category_id = request.form.get("category-id")
    category_type = request.form.get("category-type")
    category_name = request.form.get("category-name").strip()

    # if no category name provided return error
    if not category_name:
        return redirect(url_for('error', code=404))

    # check if admin wants to add or edit category
    if category_type == "Add":

        # check if the category exists in our database
        category_exists = mongo.db.categories.count_documents(
            {"category_name": category_name.lower()})

        if category_exists:
            flash("Category Already Exists", category="alert-warning")
            return redirect(url_for('manage_categories'))

        # add new category in database
        new_category = {
            "category_name": category_name.lower()
        }
        mongo.db.categories.insert_one(new_category)

        # alert the admin that the category was successfully added
        flash("Category Added Successfully", category="alert-success")
        return redirect(url_for('manage_categories'))

    elif category_type == "Edit":
        # check if the category id hasn't been change
        if not is_valid(category_id):
            return redirect(url_for('error', code=404))

        # check if the admin edit category is not submitted with the same name
        check_category = mongo.db.categories.count_documents(
            {"category_name": category_name.lower()})

        if check_category:
            flash("You have submited the same category",
                  category="alert-warning")
            return redirect(url_for('manage_categories'))

        # update category name in category collection
        # and return the old document in order to update the
        # recipe collection the old category with the new name
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

        # alert the admin that the category was successfully edited
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
    # query all products from shop collection
    products = list(mongo.db.shop.find())

    # call the paginated function to display only the
    # specific number of product per page
    paginated_products = paginated(products)

    # get the page pagination
    pagination = get_pagination(products)

    # total number of products found
    total = len(products)

    # set up the page_set object
    page_set = {
        "title": "Kitchen Tools"
    }

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # get the recomanded products
    recommended_products = mongo.db.shop.aggregate([{'$sample': {'size': 3}}])
    return render_template("pages/shop.html",
                           page_set=page_set,
                           nav_categories=nav_categories,
                           products=paginated_products,
                           pagination=pagination,
                           total=total,
                           recommended_products=recommended_products)


@app.route("/shop/search", methods=["GET", "POST"])
def shop_search():
    """
    Display the search items from shop page
    """
    # get the query search
    query = request.args.get('query')

    # if no query return page not found
    if not query:
        return redirect(url_for('error', code=404))

    # get the requested product(s)
    products = list(mongo.db.shop.find({"$text": {"$search": query}}))

    # call the paginated function to display only the
    # specific number of product per page
    paginated_products = paginated(products)

    # get the page pagination
    pagination = get_pagination(products)

    # total number of products found
    total = len(products)

    # set up the page_set object
    page_set = {
        "title": "Kitchen Tools"
    }

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # get the recomanded products
    # get the recomanded products
    recommended_products = mongo.db.shop.aggregate([{'$sample': {'size': 3}}])
    return render_template("pages/shop.html",
                           page_set=page_set,
                           nav_categories=nav_categories,
                           products=paginated_products,
                           pagination=pagination,
                           total=total,
                           recommended_products=recommended_products)


@app.route("/contact", methods=["GET"])
def contact():
    """
    Display the contact page
    """
    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # set up the page_set object
    page_set = {
        "title": "Contact",
        "type": "form"
    }
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

    # if email already exists return status to user
    if email_exists:
        return json.dumps({'status': 'already subscribed'})

    # insert new email in our database in subscriptions collection
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
    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # set up the page_set object
    page_set = {
        "title": "Terms and Conditions"
    }
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
    Show user error to the erro page
    """
    # check which type of error needs to be display
    if code == "401":
        title = "Authorization Required"
    elif code == "403":
        title = "Access Forbidden"
    elif code == "404":
        title = "Page Not Found"

    # get the categories that are in use for navigation menu
    nav_categories = mongo.db.recipes.distinct("category_name")

    # set up the page_set object
    page_set = {
        "title": title,
        "code": code
    }
    return render_template("pages/error.html",
                           page_set=page_set,
                           nav_categories=nav_categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
