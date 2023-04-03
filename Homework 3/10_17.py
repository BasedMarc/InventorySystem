# Marco Lopez 1537013
# CIS 2348-17255

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        # Initialize instance attributes with default values or given values
        self.item_name = item_name
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        # Calculate total cost and print the item cost information
        total_cost = self.item_price * self.item_quantity
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, total_cost))


if __name__ == "__main__":
    items = []

    # Prompt the user for two items
    for i in range(1, 3):
        print("Item {}".format(i))
        item_name = input("Enter the item name:\n")
        item_price = int(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        print()

        # Create ItemToPurchase objects and add them to the items list
        items.append(ItemToPurchase(item_name, item_price, item_quantity))

    # Print the total cost header
    print("TOTAL COST")

    total_cost = 0
    # Iterate through items, print the cost information, and update the total cost
    for item in items:
        item.print_item_cost()
        total_cost += item.item_price * item.item_quantity

    # Print the total cost
    print("\nTotal: ${}".format(total_cost))
