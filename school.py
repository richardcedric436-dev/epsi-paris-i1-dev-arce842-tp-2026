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

    def __repr__(self):
        return f"SchoolClass({self._students!r})"
```

---

### 5. Committer le fichier

Descendez en bas de la page jusqu'à la section **"Commit new file"** :

- Dans le premier champ, tapez le message :
```
feat: declare Student and SchoolClass base classes
```
- Laissez **"Commit directly to the main branch"** coché
- Cliquez sur le bouton vert **"Commit new file"**

---

### 6. Récupérer le lien vers ce commit précis

Une fois le commit créé :

1. Cliquez sur l'**historique des commits** (icône 🕐 ou lien **"X commits"** en haut à droite du dépôt)
2. Cliquez sur le commit que vous venez de faire
3. Vous êtes sur une URL de ce type :
```
https://github.com/richardcedric436-dev/epsi-paris-i1-dev-arce842-tp-2026/commit/abc1234
```
4. Pour avoir le lien vers **le fichier à ce commit précis**, modifiez l'URL ainsi :
```
https://github.com/richardcedric436-dev/epsi-paris-i1-dev-arce842-tp-2026/blob/abc1234/school.py

if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print(school_class)
