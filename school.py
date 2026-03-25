from collections.abc import Iterable, Iterator


class Student:
    """Représente un étudiant avec 3 notes dans 3 matières."""

    def __init__(self, name: str, grade1: float, grade2: float, grade3: float):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    @property
    def average(self) -> float:
        return (self.grade1 + self.grade2 + self.grade3) / 3

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"grade1={self.grade1}, grade2={self.grade2}, grade3={self.grade3}, "
            f"average={self.average:.2f})"
        )


class Matter1Iterator(Iterator):
    """Itérateur qui parcourt les étudiants du meilleur au moins bon en matière 1."""

    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grade1, reverse=True)
        self._index = 0

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

    def __iter__(self):
        return self


class Matter2Iterator(Iterator):
    """Itérateur qui parcourt les étudiants du meilleur au moins bon en matière 2."""

    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grade2, reverse=True)
        self._index = 0

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

    def __iter__(self):
        return self


class Matter3Iterator(Iterator):
    """Itérateur qui parcourt les étudiants du meilleur au moins bon en matière 3."""

    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grade3, reverse=True)
        self._index = 0

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

    def __iter__(self):
        retu
