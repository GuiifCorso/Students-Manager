class Student():
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        self.info = {
            "Nome": name,
            "Idade": age,
            "Notas": grades
        }

    def student_info(self):
        print(f"Student: {self.name} / Age: {self.age} / Grades: {self.grades}")

    def update_student(self):
        self.age = int(input(f"Enter the new age for {self.name}: "))
        self.grades = list(map(float, input(f"Enter the new grades for {self.name} separated by space: ").split()))

    @classmethod
    def from_dict(cls, data):
        return cls(name=data['Nome'], age=data["Idade"], grades=data['Notas'])