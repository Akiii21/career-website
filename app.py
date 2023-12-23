from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_CareerScoops():
    return render_template("home.html")

@app.route("/post-matricS.html")
def post_matric_scholarship():
    return render_template("post-matricS.html")




if __name__ == "__main__":
 app.run(host="0.0.0.0", debug=True)