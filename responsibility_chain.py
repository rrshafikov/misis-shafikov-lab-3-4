from abc import ABC, abstractmethod
from enum import Enum


# Типы запросов
class RequestType(Enum):
    TYPE_A = 1
    TYPE_B = 2


# Запрос
class Request:
    def __init__(self, type_: RequestType):
        self.type = type_


# Интерфейс обработчика
class Handler(ABC):
    @abstractmethod
    def handle(self, request: Request) -> None:
        pass

    @abstractmethod
    def set_next(self, next_handler: "Handler") -> None:
        pass


# Конкретный обработчик A
class ConcreteHandlerA(Handler):
    def __init__(self):
        self.next_handler: Handler | None = None

    def handle(self, request: Request) -> None:
        if request.type == RequestType.TYPE_A:
            print("ConcreteHandlerA handled the request.")
        elif self.next_handler:
            self.next_handler.handle(request)

    def set_next(self, next_handler: Handler) -> None:
        self.next_handler = next_handler


# Конкретный обработчик B
class ConcreteHandlerB(Handler):
    def __init__(self):
        self.next_handler: Handler | None = None

    def handle(self, request: Request) -> None:
        if request.type == RequestType.TYPE_B:
            print("ConcreteHandlerB handled the request.")
        elif self.next_handler:
            self.next_handler.handle(request)

    def set_next(self, next_handler: Handler) -> None:
        self.next_handler = next_handler


# Пример использования
if __name__ == "__main__":
    handlerA = ConcreteHandlerA()
    handlerB = ConcreteHandlerB()

    handlerA.set_next(handlerB)

    handlerA.handle(Request(RequestType.TYPE_A))
    handlerA.handle(Request(RequestType.TYPE_B))
