# Python Flask API Project — “User Management API”
# 🧠 What You’ll Learn

# How to create real API endpoints (GET, POST)

# How to return JSON responses

# How to handle errors properly

# How to organize code with classes + Flask

from flask import Flask, jsonify, request

# ✅ Initialize Flask App
app = Flask(__name__)

# ✅ Custom Error Class
class APIError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.status_code = status_code


# ✅ User Model
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email
        }


# ✅ API Logic (Class-based)
class UserAPI:
    def __init__(self):
        self.users = [
            User(1, "Alice", "alice@example.com"),
            User(2, "Bob", "bob@example.com"),
            User(3, "Charlie", "charlie@example.com"),
        ]

    def get_all_users(self):
        return [user.to_dict() for user in self.users]

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user.to_dict()
        raise APIError("User not found", 404)

    def add_user(self, name, email):
        if not name or not email:
            raise APIError("Name and Email are required", 400)
        new_id = self.users[-1].user_id + 1 if self.users else 1
        new_user = User(new_id, name, email)
        self.users.append(new_user)
        return new_user.to_dict()


# ✅ Create Instance of API
user_api = UserAPI()


# ------------------------------
# 🌐 Flask Routes
# ------------------------------

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the User API!"})


# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    try:
        users = user_api.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = user_api.get_user_by_id(user_id)
        return jsonify(user), 200
    except APIError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# POST (add) new user
@app.route("/users", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        new_user = user_api.add_user(name, email)
        return jsonify({"message": "User added", "user": new_user}), 201
    except APIError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
