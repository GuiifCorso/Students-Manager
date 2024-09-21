from student import Student
import json

students = []

def add_student():
    global students
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grades = list(map(float, input("Enter the student's grades separated by space: ").split()))
    students.append(Student(name, age, grades))

def update_student(name):
    for student in students:
        if student.name == name:
            student.update_student()
            print(f"Updated {name}'s data successfully.")
            return
    print(f"Student with name {name} not found.")

def delete_student(name):
    global students
    students = [student for student in students if student.name != name]
    print(f"Deleted student with name {name} if existed.")

def view_students():
    global students
    if not students:
        print("No students available.")
        return
    for student in students:
        student.student_info()

def search_student(name):
    global students
    for student in students:
        if student.name == name:
            print(student.info)
            return
    print(f"Student {name} not found.")

def average_grades():
    global students
    all_grades = []
    for student in students:
        grades = [grade for grade in student.grades]
        all_grades += grades
    print(sum(all_grades)/len(all_grades))

def find_highest_and_lowest_average_grades():
    global students
    if not students:
        print("No students available.")
        return
        
    highest_avg = float('-inf')
    lowest_avg = float('inf')
    highest_student = None
    lowest_student = None
        
    for student in students:
        avg_grade = sum(student.grades) / len(student.grades)
        if avg_grade > highest_avg:
            highest_avg = avg_grade
            highest_student = student
        if avg_grade < lowest_avg:
            lowest_avg = avg_grade
            lowest_student = student
        
    if highest_student:
        print(f"Highest average grade: {highest_avg} by {highest_student.name}")
    if lowest_student:
        print(f"Lowest average grade: {lowest_avg} by {lowest_student.name}")

def save_data(filename):
    global students
    data = [student.info for student in students]
    with open(f"{filename}.json", 'w') as f:
        json.dump(data, f)
    print(f"Data saved to {filename} successfully.")

def load_data(filename):
    global students
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            students = [Student.from_dict(student_data) for student_data in data]
        print(f"Data loaded from {filename} successfully.")
    except FileNotFoundError:
        print(f"No data file found with the name {filename}.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {filename}.")

def main():
    commands = {
        '1': add_student,
        '2': lambda: update_student(input("Enter the student's name to update: ")),
        '3': lambda: delete_student(input("Enter the student's name to delete: ")),
        '4': view_students,
        # Add placeholders for the other commands
        '5': lambda: search_student(input("Enter the student's name to search: ")),
        '6': average_grades,
        '7': find_highest_and_lowest_average_grades,
        '8': lambda: save_data(input("Enter the filename to save: ")),
        '9': lambda: load_data(input("Enter the filename to load: ")),
        '0': lambda: exit()
    }
    while True:
        print("1. Add a student\n2. Update a student\n3. Delete a student\n4. View all students\n5. Search for student\n6. Calculate average grades\n7. Find highest and lowest average grades\n8. Save data\n9. Load data\n0. Exit")
        order = input("Choose an option: ")
        try:
            commands[order]()
        except KeyError: 
            print("Select a valid option, please.")
                
main()