from flask import *

app = Flask(__name__)

@app.route("/get-users/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Mihir Bhadauria",
        "email": "mihirbhadauria@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-users", methods=["POST"])
def create_users():
    data = request.get_json()

    return jsonify(data), 201

def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=False)