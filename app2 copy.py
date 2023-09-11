from flask import Flask, request, render_template

app = Flask(__name__)

users = [
    {"username": "dor", "password": "123456"},
    {"username": "nir", "password": "123"},
]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        for user in users:
            if user["username"] == username and user["password"] == password:
                return render_template("welcome.html", username=username)
        
        error_message = "Login failed. Please check your credentials."
        return render_template("login.html", error=error_message)

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
