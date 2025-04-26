from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hello/<name>")
def hello(name):
    return f'Hello, {name}!'

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)