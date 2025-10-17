from flask import Flask

app = Flask("__name__")


@app.route("/")
def index():
    return "Salom backend dasturchi"

@app.route("/about")
def about():
    return "Home about"


if __name__ == "__main__":
    app.run(debug=True)
    
