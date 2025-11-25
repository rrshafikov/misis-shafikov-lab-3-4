from abc import ABC, abstractmethod


# Интерфейс устройства
class Device(ABC):
    @abstractmethod
    def print_data(self, data: str) -> None:
        pass


# Конкретные устройства
class Monitor(Device):
    def print_data(self, data: str) -> None:
        print(f"Displaying on monitor: {data}")


class Printer(Device):
    def print_data(self, data: str) -> None:
        print(f"Printing to paper: {data}")


# Абстракция вывода
class Output(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def render(self, data: str) -> None:
        pass


# Расширенная абстракция
class TextOutput(Output):
    def render(self, data: str) -> None:
        self.device.print_data(f"Text: {data}")


class ImageOutput(Output):
    def render(self, data: str) -> None:
        self.device.print_data(f"Image: [Binary data: {data}]")


# Пример использования
if __name__ == "__main__":
    monitor = Monitor()
    printer = Printer()

    t1 = TextOutput(monitor)
    t2 = TextOutput(printer)

    t1.render("Hello, world!")
    t2.render("Hello, world!")

    img = ImageOutput(monitor)
    img.render("101010101")
