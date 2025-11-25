from abc import ABC, abstractmethod


# Интерфейс для продукта A
class Button(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


# Конкретный продукт A1
class WindowsButton(Button):
    def paint(self) -> None:
        print("You have created a Windows button.")


# Конкретный продукт A2
class MacButton(Button):
    def paint(self) -> None:
        print("You have created a Mac button.")


# Интерфейс для продукта B
class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


# Конкретный продукт B1
class WindowsCheckbox(Checkbox):
    def paint(self) -> None:
        print("You have created a Windows checkbox.")


# Конкретный продукт B2
class MacCheckbox(Checkbox):
    def paint(self) -> None:
        print("You have created a Mac checkbox.")


# Интерфейс абстрактной фабрики
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Конкретная фабрика 1
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


# Конкретная фабрика 2
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# Клиентский код
class Application:
    def __init__(self, factory: GUIFactory) -> None:
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self) -> None:
        self.button.paint()
        self.checkbox.paint()


# Пример использования
if __name__ == "__main__":
    app1 = Application(WindowsFactory())
    app1.paint()

    app2 = Application(MacFactory())
    app2.paint()
