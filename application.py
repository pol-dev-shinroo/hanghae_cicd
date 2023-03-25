from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def hello():
    return render_template("index.html")


# run the app.
if __name__ == "__main__":
    application.run()
