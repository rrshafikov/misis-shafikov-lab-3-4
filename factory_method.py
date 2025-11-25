from abc import ABC, abstractmethod


# Интерфейс для продукта (логгера)
class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


# Конкретный продукт: Файловый логгер
class FileLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Logging to file: {message}")


# Конкретный продукт: Консольный логгер
class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Logging to console: {message}")


# Создатель (фабрика)
class LoggerFactory(ABC):
    # Фабричный метод
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    # Метод, использующий фабричный метод
    def log_message(self, message: str) -> None:
        logger = self.create_logger()
        logger.log(message)


# Конкретный создатель: Фабрика для файлового логгера
class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


# Конкретный создатель: Фабрика для консольного логгера
class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


# Пример использования
if __name__ == "__main__":
    file_factory = FileLoggerFactory()
    console_factory = ConsoleLoggerFactory()

    file_factory.log_message("file message")
    console_factory.log_message("console message")
