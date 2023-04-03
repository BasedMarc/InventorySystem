# Marco Lopez 1537013
# CIS 2348-17255

class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        # Initialize instance attributes with default values or given values
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        # Print nutritional information per serving
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    # Read input values
    food_name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    num_servings = float(input())

    # Create FoodItem objects: one with default values and one with input values
    food_item_default = FoodItem()
    food_item = FoodItem(food_name, fat, carbs, protein)

    # Print nutritional information and calories per serving for the default FoodItem
    food_item_default.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}\n".format(num_servings, food_item_default.get_calories(num_servings)))

    # Print nutritional information and calories per serving for the input FoodItem
    food_item.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, food_item.get_calories(num_servings)))
