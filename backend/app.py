from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()



app = Flask(__name__, static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY")
CORS(app)

# ---------------- MONGODB ----------------

client = MongoClient(
      os.environ.get("MONGO_URI")
)

db = client["novels_project"]

users = db["users"]
stories = db["stories"]

# ---------------- WEB PAGES ----------------

@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/register-page")
def register_page():
    return render_template("register.html")


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/horror")
def horror_page():
    return render_template("Horror.html")


@app.route("/fantasy")
def fantasy_page():
    return render_template("Fantasy.html")


@app.route("/history")
def history_page():
    return render_template("History.html")


@app.route("/adventure")
def adventure_page():
    return render_template("Adventure.html")


@app.route("/comedy")
def comedy_page():
    return render_template("Comedy.html")


@app.route("/mystery")
def mystery_page():
    return render_template("Mystery.html")


@app.route("/educational")
def educational_page():
    return render_template("Educational.html")


@app.route("/ecofiction")
def ecofiction_page():
    return render_template("ecofiction.html")


# ---------------- STORY PAGE ----------------

@app.route("/story")
def story_page():

    title = request.args.get("title")

    return render_template("story.html", title=title)


# ---------------- REGISTER ----------------

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if users.find_one({"username": username}):

        return jsonify({"message": "User already exists"})

    hashed_pw = generate_password_hash(password)

    users.insert_one({

        "username": username,
        "password": hashed_pw

    })

    return jsonify({"message": "User registered successfully"})


# ---------------- LOGIN ----------------

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = users.find_one({"username": username})

    if user and check_password_hash(user["password"], password):

        return jsonify({"message": "Login successful"})

    return jsonify({"message": "Invalid credentials"})


# ---------------- GET STORIES BY THEME ----------------

@app.route("/stories/<theme>", methods=["GET"])
def get_stories(theme):

    stories_list = list(
        stories.find(
            {"theme": theme},
            {"_id": 0}
        )
    )

    return jsonify(stories_list)


# ---------------- GET SINGLE STORY ----------------

@app.route("/story/<title>", methods=["GET"])
def get_story(title):

    story = stories.find_one(

        {"title": title},

        {"_id": 0}

    )

    if story:

        return jsonify(story)

    return jsonify({"error": "Story not found"}), 404


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)