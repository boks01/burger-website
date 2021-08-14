import random
from flask import Flask, render_template
import time
import requests

API = "https://api.npoint.io/57a6a8cdbcc5b6b5094e"
response = requests.get(API)
result = response.json()
with open("order_list.txt", "r") as order_list:
    p = order_list.read()
    full_order = p.split()
price_count = 0
with open("price.txt", "r") as price_list:
        price = [int(item) for item in price_list]
        for i in price:
            price_count += i
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', result=result)

@app.route("/home/<order><price>")
def the_home(order, price):
    with open("price.txt", "a") as price_list:
        price_list.write(f"{price}\n")
    with open("order_list.txt", "a") as order_list:
        order_list.write(f"{order}\n")
    full_order.append(order)
    return render_template('index.html', result=result)

@app.route("/basket")
def basket():
    num = 0
    with open("order_list.txt", "r") as order_list:
        the_orders = order_list.read()
        the_orders_list = the_orders.split()
    with open("price.txt", "r") as price_list:
        price = [int(item) for item in price_list]
        how_len = len(price)
        num += 1
    return render_template(
        'basket.html', 
        result=result, 
        order=the_orders_list, 
        price=price, 
        num=num, 
        len=how_len, 
        total=sum(price))

@app.route("/login", methods=["POST"])
def login():
    with open("order_list.txt", "w") as order_list:
        order_list.write("")
    with open("price.txt", "w") as price_list:
        price_list.write(f"")
    return render_template('login.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)