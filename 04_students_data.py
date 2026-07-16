students = []

while True:
    print("--- Student Management System ---")
    print("1. Add a Student")
    print("2. View All Students")
    print("3. Search Students")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. Quit")
    choice = int(input("enter your choice 1-6:"))
    if (choice == 1):
        print("Enter student details:")
        s_id = input("Enter the student id:")
        name = input("Enter the name:")
        grade = float(input("Enter Grade:"))
        student = {"id" : s_id, "name" : name , "grade" : grade}
        students.append(student)
        print("Student added successfully.")
    elif (choice == 2):
        print("All Students:")
        for student in students:
            print(f"ID = {student['id']}, Name = {student['name']}, Grade = {student['grade']}")
    elif (choice == 3):
        search_id = input("Enter the student id to search:")
        for student in students:
            if student["id"] == search_id:
                print(f"ID = {student['id']}, Name = {student['name']}, Grade = {student['grade']}")
                break
        else:
            print("Student not found.")
    elif (choice == 4):
        new_id = input("Enter the student id to update grade:")
        for student in students:
            if student["id"] == new_id:
                new_grade = float(input("Enter new grade:"))
                student["grade"] = new_grade
                print("Grade updated successfully.")
                break
        else:
            print("Student not found.")    
    elif (choice == 5):
        del_id = input("Enter student id you want to delete:")  
        for student in students:
            if student['id'] == del_id:
                students.remove(student)
                print("Student deleted successfully.")
                break
        else:
            print("Student not found.")
    else:
        print("Exiting the program.")
        break
