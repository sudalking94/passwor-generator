import os
import math
from flask import Flask, flash, render_template, redirect, url_for, request


app = Flask(__name__)

sign = "@#$%"
number = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def make_password(length):

    return pass


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<result>")
def result(result):
    if result == "result":
        length = request.args["length"]
        if length == 10:
            result = make_password(length)
        else:
            result = make_password(length)
        return render_template(f"{result}.html", result=result)
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
