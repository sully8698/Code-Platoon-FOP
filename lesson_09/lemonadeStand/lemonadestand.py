class MenuItems:
    def __init__(self, name, item_wholesale_cost, item_sale_price):
        self._name = name
        self._item_wholesale_cost = item_wholesale_cost
        self._item_sale_price = item_sale_price

        # write get methods for each data embers


class SalesForDay:
    def __init__(self, days_open, dictionary_of_items_sold):
        self._days_open = days_open
        self._dictionary_of_items_sold = dictionary_of_items_sold
    
    # get methods for the data members

class LemonadeStand:
    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu_item_objects = {}
        self._sales_for_today = []

    def get_name(self):
        return self._name
    