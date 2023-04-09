class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        # Initialize instance attributes with default values or given values
        self.item_name = item_name
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        # Calculate total cost and print the item cost information
        total_cost = self.item_price * self.item_quantity
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, total_cost))

    def print_item_description(self):
        # Print the item description information
        print("{}: {}".format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        # Initialize instance attributes with default values or given values
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        # Add the given item to the cart_items list
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        # Remove the item with the given name from the cart_items list if found
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        # Modify the item's quantity with the given item's name if found
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                item.item_quantity = item_to_purchase.item_quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Calculate and return the total quantity of all items in the cart
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    def get_cost_of_cart(self):
        # Calculate and return the total cost of all items in the cart
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        # Print the total cost of objects in the cart
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items: {}\n".format(self.get_num_items_in_cart()))

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print("\nTotal: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        # Print each item's description in the cart
        print("{}'s Shopping Cart - {}\n".format(self.customer_name, self.current_date))
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)

    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


def print_menu(shopping_cart):
    user_choice = ""

    while user_choice != "q":
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")

        while True:
            user_choice = input("Choose an option:\n")

            if user_choice in ["a", "r", "c", "i", "o", "q"]:
                break

        if user_choice == "a":
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))

            item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.add_item(item_to_purchase)

        elif user_choice == "r":
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(item_name)

        elif user_choice == "c":
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            item_quantity = int(input("Enter the new quantity:\n"))

            item_to_purchase = ItemToPurchase(item_name=item_name, item_quantity=item_quantity)
            shopping_cart.modify_item(item_to_purchase)

        elif user_choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()

        elif user_choice == "o":
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()

        elif user_choice == "q":
            continue


if __name__ == "__main__":
    main()