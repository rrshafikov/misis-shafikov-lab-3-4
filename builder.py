from abc import ABC, abstractmethod


# Продукт
class Pizza:
    def __init__(self) -> None:
        self.dough: str | None = None
        self.sauce: str | None = None
        self.topping: str | None = None

    def set_dough(self, dough: str) -> None:
        self.dough = dough

    def set_sauce(self, sauce: str) -> None:
        self.sauce = sauce

    def set_topping(self, topping: str) -> None:
        self.topping = topping

    def __str__(self) -> str:
        return (
            f"Pizza(dough='{self.dough}', "
            f"sauce='{self.sauce}', "
            f"topping='{self.topping}')"
        )


# Интерфейс строителя
class PizzaBuilder(ABC):
    @abstractmethod
    def build_dough(self) -> None:
        pass

    @abstractmethod
    def build_sauce(self) -> None:
        pass

    @abstractmethod
    def build_topping(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> Pizza:
        pass


# Конкретный строитель
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self) -> None:
        self.pizza = Pizza()

    def build_dough(self) -> None:
        self.pizza.set_dough("cross")

    def build_sauce(self) -> None:
        self.pizza.set_sauce("mild")

    def build_topping(self) -> None:
        self.pizza.set_topping("ham+pineapple")

    def get_result(self) -> Pizza:
        return self.pizza


# Директор
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder) -> None:
        self.builder = builder

    def construct_pizza(self) -> None:
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()


# Пример использования
if __name__ == "__main__":
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)

    director.construct_pizza()
    pizza = builder.get_result()

    print(pizza)
