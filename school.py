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

    def rank_matter_2(self) -> list:
        """Retourne les étudiants triés du meilleur au moins bon en matière 2."""
        return sorted(self._students, key=lambda s: s.grade2, reverse=True)

    def rank_matter_3(self) -> list:
        """Retourne les étudiants triés du meilleur au moins bon en matière 3."""
        return sorted(self._students, key=lambda s: s.grade3, reverse=True)

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

    print("Classement matière 2 :")
    for student in school_class.rank_matter_2():
        print(f"  {student.name} : {student.grade2}")

    print("Classement matière 3 :")
    for student in school_class.rank_matter_3():
        print(f"  {student.name} : {student.grade3}")
```

---

### 2. Résultat attendu à l'exécution
```
Classement matière 1 :
  J : 10
  V : 9
  A : 8
Classement matière 2 :
  V : 14
  J : 12
  A : 2
Classement matière 3 :
  A : 17
  V : 14
  J : 13
```

---

### 3. Committer sur GitHub

Message du commit :
```
feat: add rank_matter_2 and rank_matter_3 methods to SchoolClass
```
→ **"Commit changes"** ✅

---

### 4. Récupérer votre lien

Dans l'historique 🕐 → cliquez sur ce commit → copiez le hash :
```
https://github.com/richardcedric436-dev/epsi-paris-i1-dev-arce842-tp-2026/blob/<HASH>/school.py
