class System:
    def __init__(self):
        self.all_students = []

    def check_for_duplicate(self, other_student):
        for student in self.all_students:
            if student.id == other_student.id:
                return True
        return False
    
    def construct_student(self, student_data):
        return Student(*student_data)

    def add_student_record(self, student):
        if student and not self.check_for_duplicate(student):
            self.all_students.append(student)

    def unpack_data(self, matrix):
        for student_data in matrix:
            self.add_student_record(self.construct_student(student_data))

    def access_student(self, target_id):
        for student in self.all_students:
            if student.id == target_id:
                return student
        return None

    def yield_all_students(self):
        yield from self.all_students


class Student():
    def __init__(self, name=None, age=None, id=None, email=None, num=None):
        self.name = name
        self.age = age
        self.id = id
        self.email = email
        self.num = num

    def __str__(self):
        return (
            f"Name:         {self.name}\n"
            f"Age:          {self.age}\n"
            f"ID:           {self.id}\n"
            f"Email:        {self.email}\n"
            f"Phone #:      {self.num}"
        )

    def return_data(self):
        return [self.name, self.age, self.id, self.email, self.num]