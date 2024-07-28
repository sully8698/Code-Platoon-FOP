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
        return self._item_sale_price

class SalesForDay:
    def __init__(self, days_open, dictionary_of_items_sold):
        self._days_open = days_open
        self._dictionary_of_items_sold = dictionary_of_items_sold
    
    # get methods for the data members
    def get_days(self):
        return self._days_open
    
    def get_dictionary_of_items_sold(self):
        return self._dictionary_of_items_sold

class InvalidSalesItemError(Exception):
    pass
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return f'{self._name}item sold not currently on menu'

class LemonadeStand:
    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu_item_objects = {}
        self._sales_history = []

    def get_name(self):
        return self._name
    
    def add_menu_item(self, menu_Item):
        self._menu_item_objects[menu_Item.get_name()] = menu_Item
    
    def enter_sales_for_today(self, sales_dictionary):
        sales = SalesForDay(0, {})  
        
        for val in sales_dictionary:
            if val not in self._menu_item_objects:
                raise InvalidSalesItemError(val)
        
        sales.get_days = self._current_day
        sales.get_dictionary_of_items_sold = sales_dictionary
        self._sales_history.append(sales)
        self._current_day += 1
    
    def sales_of_menu_item_for_day(self, day_num, menu_item_name):
        if day_num > len(self._sales_history):
            return 'No information found for that day'
        
        for i in self._sales_history:
            if i.get_days == day_num:
                if menu_item_name in i.get_dictionary_of_items_sold:
                    return i.get_dictionary_of_items_sold[menu_item_name]
                elif menu_item_name in self._menu_item_objects:
                    
                    i.get_dictionary_of_items_sold[menu_item_name] = 0
                    
                    return i.get_dictionary_of_items_sold[menu_item_name]
    
    def total_sales_for_menu_item(self, menu_item_name):
        total = 0
        for i in range(len(self._sales_history)):
            total += self.sales_of_menu_item_for_day(i, menu_item_name)
            
        
        return total
    
    def total_profit_for_menu_item(self, menu_item_name):
        total_sold = self.total_sales_for_menu_item(menu_item_name)
        profit = total_sold * (self._menu_item_objects[menu_item_name].get_item_sale_cost() - self._menu_item_objects[menu_item_name].get_item_wholesale_cost())
        
        return profit
    
    def total_profit_for_stand(self):
        total = 0
        for i in range(len(self._sales_history)):
            
            for j in self._sales_history[i].get_dictionary_of_items_sold.keys():
                total += self.total_profit_for_menu_item(j)
        
        return total

def main():
    stand = LemonadeStand("Sour Bills")

    item_1 = MenuItem("sandwhich", 2.50, 6.00)
    item_2 = MenuItem("soup", 1.00, 3.00)
    item_3 = MenuItem("lemonade", .50, 1.25)

    stand.add_menu_item(item_1)
    stand.add_menu_item(item_2)
    stand.add_menu_item(item_3)

    day_0_sales = {
        'lemonade' : 5,
        'sandwhich' : 2,
        # 'cookie' : 3
    }

    day_1_sales = {
        'soup' : 6,
        'sandwhich' : 2,
        'lemonade' : 3
    }

    day_2_sales = {
        'sandwhich' : 5,
        'lemonade' : 10
    }
    


    stand.enter_sales_for_today(day_0_sales)
    stand.enter_sales_for_today(day_1_sales)
    stand.enter_sales_for_today(day_2_sales)

    print(stand.total_profit_for_stand())

if __name__ == '__main__':
    main()
        









