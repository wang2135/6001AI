from flask import Flask, render_template, redirect, url_for

app = Flask("__name__")

# 根路由，自动跳转到 /qa
@app.route("/", methods=["GET"])
def home():
    return redirect(url_for("qa"))

# /qa 路由，渲染 Q&A.html
@app.route("/qa", methods=["GET"])
def qa():
    return render_template("myanswer.html")

if __name__ == "__main__":
    app.run(debug=True)

