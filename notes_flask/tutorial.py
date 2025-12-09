#EG 7th flask notes
from flask import Flask, render_template, request, redirect, url_for

app=Flask (__name__)

@app.route("/" methods=["POST", "GET"])
def home():
    if request.method=="POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")


@app.route("/contact")
def contact():
    return "<p> you can find behind the dumpster</p>"

@app.route("/<name>")
def user(name):
    return f"<p> Hello {name}!</p>"

if __name__ == "__main__":
    app.run(debug=True)