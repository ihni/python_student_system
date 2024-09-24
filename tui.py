import os

class TUI:
    ATTEMPTS = 5
    MENU_OPTIONS = {
        1: "View your information",
        2: "View other students' information",
        3: "Register a new student",
        4: "View all students in record",
        5: "End program"
    }

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_input(prompt):
        return input(prompt).strip()
    
    @staticmethod
    def print_menu(user):
        TUI.clear_screen()
        print(f"Welcome, {user.name.title()}!")
        for key, value in TUI.MENU_OPTIONS.items():
            print(f"{key}: {value}")
    
    @staticmethod
    def is_valid_choice(user_input):
        return (user_input.isdigit() and 5 >= int(user_input) >= 1)
    
    @staticmethod
    def confirm_action(message):
        return TUI.get_input(f"{message} (Y/N): ").lower() == 'y'
    
    @staticmethod
    def register_student(system):
        TUI.clear_screen()
        attributes = ["name", "age", "ID", "email","phone number"]
        student_data, display_string = [], []
        for attr in attributes:
            print(f"REGISTER STUDENT TO RECORD")
            print(f"{display_string}")
            user_input = TUI.get_input(f"Enter {attr}: ")
            student_data.append(user_input)
            display_string.append(f"{attr}: {user_input}")
            TUI.clear_screen()

        if TUI.confirm_action(f"REGISTER STUDENT TO RECORD\n{display_string}\n\n"):
            new_student = Student(*student_data)
            if not system.check_for_duplicate(new_student):
                system.add_student_record(new_student)
                print(f"Added '{new_student.name}' to the records.\n")
            else:
                print(f"Student ID '{new_student.id}' already exists.\n")
        else:
            print("Process Cancelled.\n")
    
    @staticmethod
    def view_student(system):
        TUI.clear_screen()
        target_id = TUI.get_input(f"Enter Student ID: ")
        student = system.access_student(target_id)

        TUI.clear_screen()
        if student:
                print(f"=== Student Record ===\n\n{student}\n\n======================\n")
        else:
            print(f"No Student Record of '{target_id}' found.\n")
    
    @staticmethod
    def view_all_students(system):
        TUI.clear_screen()
        print("=== ALL STUDENT RECORDS ===\n")
        for student in system.yield_all_students():
            print(student, end='\n\n')
        print("=============================\n")
    
    @staticmethod
    def main_menu(system,  user):
        while True:
            TUI.clear_screen()
            TUI.print_menu(user)
            choice = TUI.get_input(f"\nEnter your choice: ")
            if not TUI.is_valid_choice(choice):
                print("\nInvalid Choice.")
                input("\nPress enter to continue...")
                continue

            choice = int(choice)
            if choice == 5:
                TUI.clear_screen()
                print("Ending Program...")
                break
            if choice == 1:
                TUI.clear_screen()
                print(f"=== Your Information ===\n\n{user}\n\n=======================\n")
            elif choice == 2:
                TUI.view_student(system)
            elif choice == 3:
                TUI.register_student(system)
            elif choice == 4:
                TUI.view_all_students(system)
            
            input('Press enter to continue...')
            
    @staticmethod
    def log_in(system):
        attempts = TUI.ATTEMPTS
        user = None
        while attempts > 0:
            TUI.clear_screen()
            print("Welcome to the Student Information System!")
            print("\nPlease Log In: ")
            id = TUI.get_input("Enter your ID: ")
            for student in system.all_students:
                if student.id == id:
                    user = student

            if user:
                return user
            
            attempts -= 1
            print(f"\nInvalid ID, you have {attempts} attempts left." if attempts <= 3 else
                  f"\nInvalid ID, please try again.\n")
            input("Press enter to continue...")
            
        TUI.clear_screen()
        print("You have run out of attempts.\n\nPlease contact 123-304-502")
        quit()

    @staticmethod
    def deploy(system):
        user = TUI.log_in(system)
        TUI.main_menu(system, user)