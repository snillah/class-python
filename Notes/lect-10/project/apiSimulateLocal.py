# Mini Project: “Simple API Simulation”

# We’ll simulate an API that:

# Lists all users

# Adds a new user

# Gets user by ID

# Handles errors (like invalid ID)

# Uses class-based design

import json

# ✅ Custom Error Class
class APIError(Exception):
    """Custom error for API operations"""
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.status_code = status_code

# ✅ User Data Model
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email
        }

# ✅ API Class
class UserAPI:
    def __init__(self):
        # Dummy data
        self.users = [
            User(1, "Alice", "alice@example.com"),
            User(2, "Bob", "bob@example.com"),
            User(3, "Charlie", "charlie@example.com")
        ]

    # Get all users
    def get_all_users(self):
        try:
            data = [user.to_dict() for user in self.users]
            return self.make_response(data, 200)
        except Exception as e:
            return self.make_response(str(e), 500)

    # Get single user by ID
    def get_user_by_id(self, user_id):
        try:
            for user in self.users:
                if user.user_id == user_id:
                    return self.make_response(user.to_dict(), 200)
            raise APIError("User not found", 404)
        except APIError as e:
            return self.make_response({"error": str(e)}, e.status_code)

    # Add a new user
    def add_user(self, name, email):
        try:
            if not name or not email:
                raise APIError("Name and email required", 400)

            new_id = self.users[-1].user_id + 1 if self.users else 1
            new_user = User(new_id, name, email)
            self.users.append(new_user)
            return self.make_response({"message": "User added", "user": new_user.to_dict()}, 201)
        except APIError as e:
            return self.make_response({"error": str(e)}, e.status_code)
        except Exception as e:
            return self.make_response({"error": str(e)}, 500)

    # Common JSON-like response
    def make_response(self, data, status):
        return {
            "status_code": status,
            "data": data
        }

# ✅ Testing the API Simulation
api = UserAPI()

# List all users
print("📜 GET ALL USERS")
print(json.dumps(api.get_all_users(), indent=4))

# Get user by valid ID
print("\n🔍 GET USER BY ID = 2")
print(json.dumps(api.get_user_by_id(2), indent=4))

# Get user by invalid ID
print("\n❌ GET USER BY ID = 10 (invalid)")
print(json.dumps(api.get_user_by_id(10), indent=4))

# Add new user
print("\n➕ ADD NEW USER")
print(json.dumps(api.add_user("David", "david@example.com"), indent=4))

# Add user with missing info (error)
print("\n⚠️ ADD USER WITHOUT NAME (Error Example)")
print(json.dumps(api.add_user("", "no_name@example.com"), indent=4))
