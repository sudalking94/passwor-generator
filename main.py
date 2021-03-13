import os
import math
import random
from flask import Flask, flash, render_template, redirect, url_for, request


app = Flask(__name__)

sign = "!@#$%^&*()"
number = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def make_password(length, args):
    total_string = ""
    for k in args:
        if k == "sign":
            total_string += sign
        elif k == "number":
            total_string += number
        elif k == "lower_case":
            total_string += lower_case
        elif k == "upper_case":
            total_string += upper_case

    total_string_list = list(total_string)
    random.shuffle(total_string_list)
    total_string = ''.join(total_string_list)
    if length == "10":
        total_string = total_string[0:10]
        return total_string
    else:
        if len(total_string) < 20:
            temp = total_string[0:10]
            total_string_list = list(total_string)
            random.shuffle(total_string_list)
            total_string = temp + ''.join(total_string_list[0:10])
            total_string = ''.join(total_string)
            return total_string
        else:
            total_string = total_string[0:20]
            return total_string


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<result>")
def result(result):
    total_string = ""
    if result == "result":
        length = request.args["length"]
        args = request.args
        total_string = make_password(length, args)
        return render_template(f"{result}.html", result=total_string)
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
