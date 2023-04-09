#Marco Lopez 1537013

# Import necessary modules
import csv
from datetime import datetime


# Define the InventoryManager class to manage the store inventory
class InventoryManager:
    # Initialize the class with three input files
    def __init__(self, manufacturer_list, price_list, service_dates_list):
        self.manufacturer_list = manufacturer_list
        self.price_list = price_list
        self.service_dates_list = service_dates_list

    # Function to read a CSV file and return its data as a list of rows
    def read_csv(self, filename):
        data = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data

    # Function to write a list of rows to a CSV file
    def write_csv(self, filename, data):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    # Functions to return specific elements from a list
    # These functions are used for sorting the lists
    def manufacturer_key(self, item):
        return item[1]

    def item_id_key(self, item):
        return item[0]

    def service_date_key(self, item):
        return item[4]

    def price_key(self, item):
        return item[3]

    # Main function to process the inventory data
    def process_inventory(self):
        # Read the input CSV files
        manufacturers = self.read_csv(self.manufacturer_list)
        prices = self.read_csv(self.price_list)
        service_dates = self.read_csv(self.service_dates_list)

        # Create dictionaries to map item ID to price and service date
        id_price = {row[0]: row[1] for row in prices}
        id_service_date = {row[0]: row[1] for row in service_dates}

        # Initialize lists to store the output data
        full_inventory = []
        type_inventory = {}
        past_service_inventory = []
        damaged_inventory = []

        # Process each item in the manufacturers list
        for item in manufacturers:
            item_id, manufacturer, item_type, *damaged = item
            damaged = "Yes" if damaged else "No"
            price = id_price[item_id]
            service_date = id_service_date[item_id]

            # Add the item to the full inventory list
            full_inventory.append([item_id, manufacturer, item_type, price, service_date, damaged])

            # Add the item to the type-specific inventory list
            if item_type not in type_inventory:
                type_inventory[item_type] = []
            type_inventory[item_type].append([item_id, manufacturer, price, service_date, damaged])

            # Check if the item is past its service date and add it to the list if it is
            if datetime.strptime(service_date, "%m/%d/%Y") < datetime.now():
                past_service_inventory.append([item_id, manufacturer, item_type, price, service_date, damaged])

            # Check if the item is damaged and add it to the list if it is
            if damaged == "Yes":
                damaged_inventory.append([item_id, manufacturer, item_type, price, service_date])

        # Sort the lists and write them to CSV files
        full_inventory.sort(key=self.manufacturer_key)
        self.write_csv("FullInventory.csv", full_inventory)

        # Write the type-specific inventory lists to separate CSV files
        for item_type, items in type_inventory.items():
            items.sort(key=self.item_id_key)
            self.write_csv(f"{item_type}Inventory.csv", items)

        # Write the past service inventory items to CSV
        past_service_inventory.sort(key=self.service_date_key)
        self.write_csv("PastServiceDateInventory.csv", past_service_inventory)

        # Sort the damaged inventory items by price (descending) and write to CSV
        damaged_inventory.sort(key=self.price_key, reverse=True)
        self.write_csv("DamagedInventory.csv", damaged_inventory)


# This is the main entry point of the script
if __name__ == "__main__":
    # Create an instance of the InventoryManager class with the input file names
    inventory_manager = InventoryManager(
        "ManufacturerList.csv",
        "PriceList.csv",
        "ServiceDatesList.csv"
    )
    # Call the process_inventory method to process the data and generate the output files
    inventory_manager.process_inventory()
