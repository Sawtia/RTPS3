import json

import menu as menu


class Pizzeria:

    @staticmethod
    def load_menu():
        with open('menu.json', 'r') as f:
            menu = json.load(f)
            return menu
    @staticmethod
    def __save_menu(menu):
        with open('menu.json', 'w') as f:
            json.dump(menu, f)

    def add_pizza(self, name, price):
        menu = self.load_menu()
        if name in menu.keys():
            print('already there is')
        else:
            menu[name] = price
        self.__save_menu(menu)

    def remove_pizza(self, name):
        menu = self.load_menu()
        if name in menu.keys():
            print('delete')
            del menu[name]
        else:
            print('no pizza')
        self.__save_menu(menu)


    def order_pizza_api(self, order):
        menu = self.load_menu()
        cost = 0
        for name in order:
            if name in menu.keys():
                cost += menu[name]
            else:
                return None
        return cost


    def order_pizza(self):
            menu = self.load_menu()
            order = []
            cost = 0
            while True:
                q1 = input('continue?')
                if q1 == 'no':
                    break
                else:
                    print('Our menu:')
                    print(menu)
                    pizza_name = input('Witch pizza?')
                    if pizza_name in menu.keys():
                        order.append(pizza_name)
                        cost = cost + int(menu[pizza_name])
                        print('Pizza added')
                        print(cost)
            return order, cost

pizzeria = Pizzeria()





if __name__ == "__main__":
    while True:
        q3 = input('continue?')
        if q3 == 'yes':
            role = input('choose role:')
            if role == 'admin':
                q2 = input('add or delete?')
                if q2 == 'add':
                    name_pizza = input('name pizza:')
                    price_pizza = int(input('price:'))
                    pizzeria.add_pizza(name_pizza, price_pizza)
                elif q2 == 'delete':
                    name_pizza = input('for deleting:')
                    pizzeria.remove_pizza(name_pizza)
            elif role == 'user':
                pizzeria.order_pizza()
            else:
                print('wrong')
        elif q3 == 'no':
            break
        else:
            print('mistake')

