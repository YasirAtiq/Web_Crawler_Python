import flask

app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/a")
def page_a():
    return flask.render_template("a.html")


@app.route("/b")
def page_b():
    return flask.render_template("b.html")


@app.route("/c")
def page_c():
    return flask.render_template("c.html")


if __name__ == "__main__":
    app.run("localhost", 8000, debug=True)
