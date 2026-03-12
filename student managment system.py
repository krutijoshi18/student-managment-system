students = {}

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    students[name] = marks
    print("Student added successfully")

def view_students():
    for name, marks in students.items():
        print(name, "-", marks)

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted")
    else:
        print("Student not found")

while True:
    print("\n1.Add Student\n2.View Students\n3.Delete Student\n4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break