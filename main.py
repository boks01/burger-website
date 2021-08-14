import random
from typing import OrderedDict
from flask import Flask, render_template, request
import time
import requests
from werkzeug.wrappers import response

API = "https://api.npoint.io/57a6a8cdbcc5b6b5094e"
response = requests.get(API)
result = response.json()
with open("order_list.txt", "r") as order_list:
    p = order_list.read()
    full_order = p.split()
num = 0
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', result=result)

@app.route("/home/<order>")
def the_home(order):
    with open("order_list.txt", "a") as order_list:
        order_list.write(f"{order}\n")
    full_order.append(order)
    return render_template('index.html', result=result)

@app.route("/basket")
def basket():
    with open("order_list.txt", "r") as order_list:
        the_orders = order_list.read()
        the_orders_list = the_orders.split()
    return render_template('basket.html', result=result, order=the_orders_list)

@app.route("/login", methods=["POST"])
def login():
    with open("order_list.txt", "w") as order_list:
        order_list.write("")
    return render_template('login.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)