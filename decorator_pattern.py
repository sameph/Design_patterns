class Coffee:
    def get_cost(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def get_ingredients(self):
        raise NotImplementedError("Subclasses must implement this method.")


class SimpleCoffee(Coffee):
    def get_cost(self):
        return 5.0

    def get_ingredients(self):
        return "Simple Coffee"


class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self._decorated_coffee = decorated_coffee

    def get_cost(self):
        return self._decorated_coffee.get_cost()

    def get_ingredients(self):
        return self._decorated_coffee.get_ingredients()


class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._decorated_coffee.get_cost() + 1.5

    def get_ingredients(self):
        return self._decorated_coffee.get_ingredients() + ", with Milk"


class SugarDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._decorated_coffee.get_cost() + 0.5

    def get_ingredients(self):
        return self._decorated_coffee.get_ingredients() + ", with Sugar"


class CaramelDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._decorated_coffee.get_cost() + 2.0

    def get_ingredients(self):
        return self._decorated_coffee.get_ingredients() + ", with Caramel"


if __name__ == "__main__":
    print("Demonstrating the Decorator Pattern:")

    coffee = SimpleCoffee()
    print(f"Order 1: {coffee.get_ingredients()} - Cost: ${coffee.get_cost():.2f}")

    coffee_with_milk = MilkDecorator(SimpleCoffee())
    print(f"Order 2: {coffee_with_milk.get_ingredients()} - Cost: ${coffee_with_milk.get_cost():.2f}")

    coffee_with_milk_sugar = SugarDecorator(MilkDecorator(SimpleCoffee()))
    print(f"Order 3: {coffee_with_milk_sugar.get_ingredients()} - Cost: ${coffee_with_milk_sugar.get_cost():.2f}")

    fancy_coffee = SugarDecorator(MilkDecorator(CaramelDecorator(SimpleCoffee())))
    print(f"Order 4: {fancy_coffee.get_ingredients()} - Cost: ${fancy_coffee.get_cost():.2f}")

    caramel_coffee = CaramelDecorator(SimpleCoffee())
    print(f"Order 5: {caramel_coffee.get_ingredients()} - Cost: ${caramel_coffee.get_cost():.2f}")

    print("\nThe Decorator pattern allows adding new responsibilities to objects dynamically.")
