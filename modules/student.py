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