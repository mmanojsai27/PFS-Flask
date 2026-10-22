from flask import Flask,render_template,url_for, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# GET request to fetch name and batch number
@app.route("/get-details", methods=["GET"])
def get_details():
    name = request.args.get("name")
    batchno = request.args.get("batchno")

    return {
        "name": name,
        "batchno": batchno
    }

# POST request to fetch name and skills
@app.route("/post-details", methods=["POST"])
def post_details():
    data = request.get_json()

    name = data.get("name")
    skills = data.get("skills")

    return jsonify({
        "name": name,
        "skills": skills
    })


if __name__ == "__main__":
    app.run(debug=True,port=5002)
