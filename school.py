def add_subject_with_iterator(subject_name, default_grade=0):
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, name, grades):
            original_init(self, name, grades)
            self.grades[subject_name] = default_grade

        # Ajout d'une méthode pour récupérer un itérateur sur la matière
        def get_subject_iterator(self):
            return iter([self.grades[subject_name]])

        cls.__init__ = new_init
        cls.get_subject_iterator = get_subject_iterator

        return cls

    return decorator
