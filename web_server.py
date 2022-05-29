import json


from flask import Flask, render_template, abort, request
from bs4 import BeautifulSoup
import requests
import menu as menu

from pizza import pizzeria

app = Flask(__name__)


#
# @app.route('/')
# def hello():
#     return render_template('index.html')


@app.route('/')
def hello():
    return 'WELCOME TO PIZZERIA'


@app.route('/pizzeria/menu', methods=['GET'])
def get_menu():
    menu = pizzeria.load_menu()
    pizza_name = request.args.get('pizza_name')
    if pizza_name:
        if pizza_name in menu.keys():
            return json.dumps({pizza_name: menu[pizza_name]})
        else:
            abort(404)
    else:
        result = json.dumps(menu)
        return result

@app.route('/pizzeria/menu/pizza', methods=['POST'])
def add_pizza():
    data = request.form
    name = data.get('name')
    cost = data.get('cost')
    pizzeria.add_pizza(name, cost)
    return '', 201

@app.route('/pizzeria/menu/pizza', methods=['DELETE'])
def delete_pizza():
    pizza_name = request.args.get('pizza_name')
    pizzeria.remove_pizza(pizza_name)
    return '', 204

@app.route('/pizzeria/order', methods=['POST'])
def order_pizza():
    data = request.form
    print(data)
    order = data.getlist('order')
    print(order)
    result = pizzeria.order_pizza_api(order)
    print(result)
    if result:
        return json.dumps({'cost': result})
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)

    # '<p>hello <p>'+ '<a href="http://127.0.0.1:5000/weather">Weather</a>'+  '<p><p>'+'<a href="http://127.0.0.1:5000/weather/add_info">Add</a>'

#
# @app.route('/weather')
# def weather():
#     page = requests.get("https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD"
#                         "%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5")
#
#     soup = BeautifulSoup(page.text, 'html.parser')
#
#     result = soup.find('div', {"class": "ArchiveTemp"}).find('span', {'class': 't_0'})
#
#     return "current weather" + result.text
#
# @app.route('/weather/info')
# def add():
#     page = requests.get('https://www.tripadvisor.ru/LocationPhotos-g298507-St_Petersburg_Northwestern_District.html')
#     soup2 = BeautifulSoup(page.text, 'html.parser')
#     result = soup2.find('div', {"class": "imgBx"}).find('img', {'class': 'taLnk big_photo'})
#
#     return "add" + result.img
#
#
#
#
#
# @app.route('/weather_api')
# def weather_api():
#     return json.dumps{'weather':15}
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
