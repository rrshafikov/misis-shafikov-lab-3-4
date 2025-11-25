from abc import ABC, abstractmethod


# Сторонний класс библиотеки
class ExternalLogger:
    def log_message(self, msg: str) -> None:
        print(f"External log: {msg}")


# Целевой интерфейс
class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


# Адаптер для интеграции
class LoggerAdapter(Logger):
    def __init__(self, external_logger: ExternalLogger):
        self.external_logger = external_logger

    def log(self, message: str) -> None:
        self.external_logger.log_message(message)


# Пример использования
if __name__ == "__main__":
    external = ExternalLogger()
    logger = LoggerAdapter(external)

    logger.log("This is a test message.")
