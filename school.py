def add_subject(subject_name, default_grade=0):
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, name, grades):
            original_init(self, name, grades)
            self.grades[subject_name] = default_grade

        cls.__init__ = new_init
        return cls

    return decorator
