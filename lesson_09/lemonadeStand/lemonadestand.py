class MenuItem:
    def __init__(self, name, item_wholesale_cost, item_sale_price):
        self._name = name
        self._item_wholesale_cost = item_wholesale_cost
        self._item_sale_price = item_sale_price

        # write get methods for each data embers
    def get_name(self):
        return self._name

    def get_item_wholesale_cost(self):
        return self._item_wholesale_cost

    def get_item_sale_cost(self):
        return self._item_wholesale_cost


class SalesForDay:
    def __init__(self, days_open, dictionary_of_items_sold):
        self._days_open = days_open
        self._dictionary_of_items_sold = dictionary_of_items_sold
    
    # get methods for the data members
    def get_days(self):
        return self._days_open
    
    def get_dictionary_of_items_sold(self):
        return self._dictionary_of_items_sold

class InvalideSalesItemError:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return f'{self._name}item sold not currently on menu'

class LemonadeStand:
    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu_item_objects = {}
        self._sales_for_day = []

    def get_name(self):
        return self._name
    
    def add_menu_item(self, menu_Item):
        self._menu_item_objects[menu_Item.get_name()] = menu_Item
    
    def enter_sales_for_today(self, sales_dictionary):
        for val in self._menu_item_objects:
            if val in sales_dictionary:
                self._current_day += 1
                self._sales_for_day.append(sales_dictionary)
        
        # check if the try/except works, except may need some attention
        for val in sales_dictionary:
            try:
                val in self._menu_item_objects
            
            except InvalideSalesItemError():
                return 
                
        



item_1 = MenuItem("sandwhich", 2.50, 5.00)
item_2 = MenuItem("soup", 1.00, 3.00)

stand = LemonadeStand("Sour Bills")

stand.add_menu_item(item_1)
stand.add_menu_item(item_2)