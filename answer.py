from flask import Flask, render_template
from flask import render_template, request

app = Flask("__name__")

@app.route("/qa", methods=["GET"])
def qa():
    return render_template("myanswer.html")

if __name__ == "__main__":
    app.run(debug=True)
