from flask import Flask

app = Flask("__name__")


@app.route("/")
def index():
    return "Salom backend dasturchi"

@app.route("/about")
def about():
    return "Home about"

@app.route("/file")
def about():
    return "file page"


if __name__ == "__main__":
    app.run(debug=True)
    
