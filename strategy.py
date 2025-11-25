from abc import ABC, abstractmethod


# Интерфейс стратегии
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array: list[int]) -> None:
        pass


# Конкретные стратегии
class BubbleSortStrategy(SortingStrategy):
    def sort(self, array: list[int]) -> None:
        print("Sorting using Bubble Sort")


class QuickSortStrategy(SortingStrategy):
    def sort(self, array: list[int]) -> None:
        print("Sorting using Quick Sort")


# Контекст
class Sorter:
    def __init__(self) -> None:
        self.strategy: SortingStrategy | None = None

    def set_strategy(self, strategy: SortingStrategy) -> None:
        self.strategy = strategy

    def sort_array(self, array: list[int]) -> None:
        self.strategy.sort(array)


# Пример использования
if __name__ == "__main__":
    sorter = Sorter()

    # Использование стратегии сортировки пузырьком
    sorter.set_strategy(BubbleSortStrategy())
    array1 = [5, 3, 8, 4, 2]
    sorter.sort_array(array1)

    # Использование стратегии быстрой сортировки
    sorter.set_strategy(QuickSortStrategy())
    array2 = [5, 3, 8, 4, 2]
    sorter.sort_array(array2)
