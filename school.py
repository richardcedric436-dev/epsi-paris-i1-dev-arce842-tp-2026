class Classroom:
    _instance = None  # Stocke l'unique instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Classroom, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Évite de réinitialiser à chaque appel
        if not hasattr(self, "students"):
            self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for s in self.students:
            print(s)
