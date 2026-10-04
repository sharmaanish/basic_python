# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "hello world"

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)

from flask import Flask, request

app = Flask(__name__)

users = {
    1: {
        "name":"anish",
        "age":29
    }
}

@app.route("/users/<int:user_id>",methods=["GET"]):
def get_user(user_id):
    if len(users) == 0:
        return "no user exists", 404
    user = users[user_id]
    return user

@app.route("/users", methods =[POST]):
def create_user():
    data = request.get_json()
    id = max(users.keys()) + 1  else 1

    users[id] = {
        "name":data['name'],
        "age" : data['age']
    }

   return{"message":"user create", "user":users[id], 201 }

@app.route(users/<"user_id"> , methods=[PUT]):
def update_user(user_id):
    if user_id not in users:
        return {"message":"user not found", 404}
    data = request.get_json()
    users[user_id] = {
        "name" = data["name"]
        "age" = data['age']
    }
    return {"message":"user updated", users[user_id]}

@app.route(users/<"user_id"> , methods=[PATCH]):
def update_user(user_id):
    if user_id not in users:
        return {"message":"user not found", 404}
    data = request.get_json()
    user = users[user_id]
    if "name" in data:
        user['name']= data['name']
    elif "age" in data:
        user['age']= data['age']
    return {"message":"user updated", users[user_id]}

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return {"error": "User not found"}, 404

    del users[user_id]

    return {"message": "User deleted"}

# HEAD → Same response headers as GET, but no body
@app.route("/users/<int:user_id>", methods=["HEAD"])
def head_user(user_id):
    if user_id not in users:
        return "", 404

    return ""


# OPTIONS → Tell client which methods are supported
@app.route("/users/<int:user_id>", methods=["OPTIONS"])
def options_user(user_id):
    return "", 204, {
        "Allow": "GET, PUT, PATCH, DELETE, HEAD, OPTIONS"
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
