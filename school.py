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


class SchoolClass:
    """Représente une salle de classe contenant plusieurs étudiants."""

    def __init__(self):
        self._students: list[Student] = []

    def add_student(self, student: Student):
        self._students.append(student)

    def rank_matter_1(self) -> list:
        """Retourne les étudiants triés du meilleur au moins bon en matière 1."""
        return sorted(self._students, key=lambda s: s.grade1, reverse=True)

    def __repr__(self):
        return f"SchoolClass({self._students!r})"


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("Classement matière 1 :")
    for student in school_class.rank_matter_1():
        print(f"  {student.name} : {student.grade1}")
```

---

### 3. Committer en bas de page

Message :
```
feat: add rank_matter_1 method to SchoolClass
