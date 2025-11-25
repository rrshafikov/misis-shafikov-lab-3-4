from abc import ABC, abstractmethod


# Интерфейс работы с БД
class Database(ABC):
    @abstractmethod
    def query(self, sql: str) -> None:
        pass


# Реальный класс БД
class RealDatabase(Database):
    def query(self, sql: str) -> None:
        print(f"Executing query: {sql}")


# Прокси с проверкой доступа
class DatabaseProxy(Database):
    def __init__(self, has_access: bool):
        self.has_access = has_access
        self.real_db = RealDatabase()

    def query(self, sql: str) -> None:
        if self.has_access:
            self.real_db.query(sql)
        else:
            print("Access denied. Query cannot be executed.")


# Пример использования
if __name__ == "__main__":
    user_db = DatabaseProxy(False)
    admin_db = DatabaseProxy(True)

    user_db.query("SELECT * FROM users")
    admin_db.query("SELECT * FROM users")
