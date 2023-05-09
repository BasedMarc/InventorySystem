# Marco Lopez
# 1537013

import csv
from datetime import datetime


# Helper method to extract price from an item
def item_price(item):
    return float(item[3])


# Helper method to calculate the absolute difference between two prices
def price_difference(item, target_price):
    return abs(float(item[3]) - float(target_price))


# Helper method to find the closest item based on price difference
def find_closest_item(item_list, target_price):
    closest_item = None
    min_difference = None

    for item in item_list:
        diff = price_difference(item, target_price)

        if min_difference is None or diff < min_difference:
            min_difference = diff
            closest_item = item

    return closest_item


class InventoryManager:
    def __init__(self, manufacturer_list, price_list, service_dates_list) -> object:
        self.manufacturer_list = manufacturer_list
        self.price_list = price_list
        self.service_dates_list = service_dates_list
        self.inventory_data = self.process_inventory()

    def read_csv(self, filename):
        data = []
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                data.append(row)
        return data

    def process_inventory(self):
        manufacturers = self.read_csv(self.manufacturer_list)
        prices = self.read_csv(self.price_list)
        service_dates = self.read_csv(self.service_dates_list)

        id_price = {row[0]: row[1] for row in prices}
        id_service_date = {row[0]: row[1] for row in service_dates}

        inventory_data = []

        for item in manufacturers:
            item_id, manufacturer, item_type, *damaged = item
            damaged = "Yes" if damaged == "damaged" else "No"
            price = id_price[item_id]
            service_date = id_service_date[item_id]

            inventory_data.append([item_id, manufacturer.strip(), item_type.strip(), price, service_date, damaged])

        return inventory_data

    def find_item(self, manufacturer, item_type):
        available_items = [item for item in self.inventory_data if
                           item[1].lower() == manufacturer.lower() and
                           item[2].lower() == item_type.lower() and
                           item[5] == "No" and
                           datetime.strptime(item[4], "%m/%d/%Y") > datetime.now()]
        if available_items:
            most_expensive_item = max(available_items, key=item_price)
            return most_expensive_item
        else:
            return None

    def find_alternative(self, item_type, price):
        alternative_items = [item for item in self.inventory_data if
                             item[2] == item_type and item[5] == "No" and datetime.strptime(item[4],
                                                                                            "%m/%d/%Y") > datetime.now() and float(
                                 item[3]) != float(price)]
        if alternative_items:
            closest_item = find_closest_item(alternative_items, price)
            return closest_item
        else:
            return None

    def query_item(self):
        global price
        while True:
            user_input = input("Please enter the manufacturer and item type (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break

            user_input_split = user_input.split()

            if len(user_input_split) < 2:
                print("Please provide both manufacturer and item type.")
                continue

            manufacturer, item_type = user_input.split()[:2]
            result = self.find_item(manufacturer, item_type)

            if result:
                item_id, manufacturer, item_type, price, service_date, damaged = result
                print(f"Your item is: {item_id}, {manufacturer}, {item_type}, {price}")

            alternative = self.find_alternative(item_type, price)
            if alternative:
                alt_id, alt_manufacturer, alt_item_type, alt_price, alt_service_date, alt_damaged = alternative
                print(f"You may, also, consider: {alt_id}, {alt_manufacturer}, {alt_item_type}, {alt_price}")
            else:
                print("No such item in inventory")


if __name__ == "__main__":
    inventory_manager = InventoryManager(
        "ManufacturerList.csv",
        "PriceList.csv",
        "ServiceDatesList.csv"
    )
    inventory_manager.query_item()
