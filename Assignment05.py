# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Arsene Hyacinthe Dina Ngollo, 07/29/2024, <Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of dict(table)
# Extract the data from the file
try:  # Try-Except Error handling to catch any structured error when the file is
    # read into the list of dictionary rows
    file = open(FILE_NAME, "r")
    json_data = json.load(file)
    print(json_data)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
finally:  # checking if the file is still open, if false will be close just in case.
    if not file.closed:
        file.close()
# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:  # Try-Except Error handling to catch any structured error
            # handling when the user enter first and last name.
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers")
            student_last_name = input("Enter the student's last name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers")
            course_name = input("Please enter the name of the course: ")
            student_data = {"student_first_name": student_first_name,
                            "student_last_name": student_last_name,
                            "course_name": course_name}
            students.append(student_data)
        except ValueError as e:
            print(e)
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        print("-" * 50)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'Student {student["student_first_name"]} '
                  f'{student["student_last_name"]} is enrolled in {student["course_name"]}')
        print("-"*50)
        # All data in the list display
        print("Data in the list: \n")
        for row in students:
            print(f'"student_first_name": {row["student_first_name"]}\n'
                  f'"student_last_name": {row["student_last_name"]}\n'
                  f'"course_name": {row["course_name"]}\n')
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:  # Try-Except Error handling to catch any structured error
            # handling when the dictionary rows are written to the file.
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=1)
            file.close()
            print("The following data was stored in the file!")
            # Display what was stored in the file
            for student in students:
                # print(f"Student {student['student_first_name']} "
                #       f"{student['student_last_name']} is enrolled in {student['course_name']}")
                print(f'"student_first_name": {student["student_first_name"]}\n'
                      f'"student_last_name": {student["student_last_name"]}\n'
                      f'"course_name": {student["course_name"]}\n')
            continue
        except TypeError as e:
            print("please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
