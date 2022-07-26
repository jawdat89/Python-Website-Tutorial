from flask import Flask, render_template

app = Flask(__name__, static_url_path="", static_folder="static")  # Flask("main.py)


@app.route("/")  # Create a page on the first url
def homePage():
    items = [
     "1234",
      "2345",
      "5678"
    ];
    return render_template("homepage.html", todolist = items)


app.run(host="0.0.0.0")
