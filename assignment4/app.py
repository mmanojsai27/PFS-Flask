from flask import Flask,render_template,url_for, request, jsonify

app = Flask(__name__)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        address = request.form.get("address")
        password = request.form.get("password")

        return {
            "username": username,
            "email": email,
            "address": address,
            "message": "Signup data has collected successfully"
        }

    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True,port=5002)
