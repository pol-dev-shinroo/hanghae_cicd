from flask import Flask, render_template

application = Flask(__name__)


@application.route("/test")
def hello():
    return "Hello World!"

@application.route("/")
def main():
    return render_template("index.html")

# run the app.
if __name__ == "__main__":
    application.run()
