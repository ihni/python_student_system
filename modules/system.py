from .student import *

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