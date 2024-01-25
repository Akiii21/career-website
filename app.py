from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_CareerScoops():
    return render_template("home.html")

@app.route("/Assessment.html")
def Assessment():
    return render_template("Assessment.html")

@app.route("/quiz.html")
def quiz():
    return render_template("quiz.html")

@app.route("/post-matricS.html")
def post_matric_scholarship():
    return render_template("post-matricS.html")

@app.route("/AICTE – SWANATH-SCHOLARSHIP.html")
def AICTE_SWANATHSCHOLARSHIP():
    return render_template("AICTE – SWANATH-SCHOLARSHIP.html")

@app.route("/pre-matricS.html")
def pre_matric_scholarship():
    return render_template("pre-matricS.html")

@app.route("/Young- artists.html")
def Young_artists():
    return render_template("Young- artists.html")

@app.route("/central-sector.html")
def central_sector():
    return render_template("central-sector.html")

@app.route("/Prime-minister.html")
def Prime_minister():
    return render_template("Prime-minister.html")

@app.route("/army.html")
def army():
    return render_template("army.html")

@app.route("/Doctor.html")
def Doctor():
    return render_template("Doctor.html")

@app.route("/Banking.html")
def Banking():
    return render_template("Banking.html")

@app.route("/lawyer.html")
def lawyer():
    return render_template("lawyer.html")

@app.route("/Engineer.html")
def Engineer():
    return render_template("Engineer.html")

@app.route("/pilot.html")
def pilot():
    return render_template("pilot.html")




           

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
