from student_app import *

predefined_data = [
    ["Nadia", "99", "2023-2-00001", "2023-2-00001@school.edu.gov", "N/A"],
    ["Akkin", "99", "2023-2-00002", "N/A", "N/A"],
    ["Egroeg", "50", "2023-2-00003", "2023-2-00003@school.edu.gov", "N/A"]
]

if __name__ == "__main__":
    sys = System()
    sys.unpack_data(predefined_data)

    TUI.deploy(sys)