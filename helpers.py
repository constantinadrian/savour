from flask import redirect, session, url_for
from functools import wraps
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId
from bson.errors import InvalidId


def login_required(f):
    """
    Decorate routes to require login

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return redirect(url_for('error', code=401))
        return f(*args, **kwargs)
    return decorated_function


# Credit Function
#   https://www.programcreek.com/python/example/87925/bson.errors.InvalidId
# Project: vnpy_crypto   Author: birforce
# File: objectid.py    License: MIT License
def is_valid(oid):
    """Checks if a `oid` string is valid or not.

    :Parameters:
        - `oid`: the object id to validate

    .. versionadded:: 2.3
    """
    if not oid:
        return False

    try:
        ObjectId(oid)
        return True
    except (InvalidId, TypeError):
        return False


def check_form(form_data):
    """
    Function that perform a small check on submited form data
    """
    # check if there are any empty fields
    for key, value in form_data:
        if value == "":
            return None
    return form_data


def user_ratings(mongo, rating, recipe):
    """
    Function that updates the user rating for each recipe
    """
    # check if user already rated this recipe
    user_rating = mongo.db.userRatings.find_one(
        {"user": (session["user"]), "recipe_id": ObjectId(recipe["_id"])})

    # if user didn't vote insert new rating in userRatings collection
    if not user_rating:
        user_rated_recipe = {
            "user": session["user"],
            "recipe_id": recipe["_id"],
            "rating": int(rating)
        }
        mongo.db.userRatings.insert_one(user_rated_recipe)
        return None

    # get the user old rating before updating with new rating
    old_user_rating = user_rating["rating"]
    mongo.db.userRatings.update_one(
        {"_id": ObjectId(user_rating["_id"])},
        {"$set": {"rating": int(rating)}})

    return old_user_rating


def calculate_weighted_average(rated_stars):
    """
    Function that calculates the recipe weighted average rating
    """
    numerator = 0
    denominator = 0
    for key, value in rated_stars.items():
        numerator += int(key) * value
        denominator += value

    return numerator/denominator


def update_recipe_rating(mongo, rating, recipe):
    """
    Function that updates the recipe rating
    """
    # update user rating and return old rating if any
    old_user_rating = user_ratings(mongo, rating, recipe)

    # define path for new rating field
    new_rated_field = "ratings.rated_stars." + rating

    # update recipe rating if it's first time rating
    if not recipe["ratings"]["status"]:
        mongo.db.recipes.find_one_and_update(
            {"_id": ObjectId(recipe["_id"])},
            {
                "$set": {
                    "ratings.status": True,
                    "ratings.number_of_ratings": 1,
                    "ratings.weighted_average": round(float(rating), 1),
                    new_rated_field: 1
                }
            }
        )
        return round(float(rating), 1)
    # if user rated for first time update the recipe rating with new rate
    elif not old_user_rating:
        new_recipe_ratings = mongo.db.recipes.find_one_and_update(
            {"_id": ObjectId(recipe["_id"])},
            {
                "$inc": {
                    "ratings.number_of_ratings": 1,
                    new_rated_field: 1
                }
            },
            return_document=ReturnDocument.AFTER
        )

        weighted_average = calculate_weighted_average(
            new_recipe_ratings["ratings"]["rated_stars"])

        mongo.db.recipes.update_one(
            {"_id": ObjectId(new_recipe_ratings["_id"])},
            {
                "$set": {
                    "ratings.weighted_average": round(
                        float(weighted_average), 1
                    )
                }
            }
        )

        return round(weighted_average, 1)

    # if user vote for second time updated the old rate with new rate
    # define path for old rating path
    old_rated_field = "ratings.rated_stars." + str(old_user_rating)

    mongo.db.recipes.update_one(
        {"_id": ObjectId(recipe["_id"])},
        {
            "$inc": {
                old_rated_field: -1
            }
        }
    )

    new_recipe_ratings = mongo.db.recipes.find_one_and_update(
        {"_id": ObjectId(recipe["_id"])},
        {
            "$inc": {
                new_rated_field: 1
            }
        },
        return_document=ReturnDocument.AFTER
    )
    # calculate the new weighted average
    new_weighted_average = calculate_weighted_average(
        new_recipe_ratings["ratings"]["rated_stars"])

    # set the new weighted average to mongo for future display
    mongo.db.recipes.update_one(
        {"_id": ObjectId(new_recipe_ratings["_id"])},
        {
            "$set": {
                "ratings.weighted_average": round(
                    float(new_weighted_average), 1
                )
            }
        }
    )
    return round(new_weighted_average, 1)
