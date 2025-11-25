from typing import Generic, TypeVar, Iterator as PyIterator


T = TypeVar("T")


# Конкретный итератор
class ArrayIterator(Generic[T]):
    def __init__(self, items: list[T]):
        self.items = items
        self.position = 0

    def __iter__(self) -> PyIterator[T]:
        return self

    def __next__(self) -> T:
        if self.position < len(self.items):
            value = self.items[self.position]
            self.position += 1
            return value
        raise StopIteration


# Пример использования
if __name__ == "__main__":
    iterator = ArrayIterator([1, 2, 3, 4])
    for elem in iterator:
        print(elem)
