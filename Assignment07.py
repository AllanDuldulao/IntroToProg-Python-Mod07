# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: Classes and Objects
# Change Log: (Who, When, What)
# ADuldulao, 5/29/2025, Created Script
# ADuldulao, 5/30/2025, Created Person class and Student class
# ADuldulao, 5/31/2025, Worked on editing and cleaning the script.

# ------------------------------------------------------------------------------------------ #
import json


#---Data-------------------------------------------------------------------------------------#
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program -------------
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------------
'''
# Define Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

#  Create a Person Class
class Person:
    """
      A base class representing student first name and last name.
      ChangLog: (Who, When, What)
      ADuldulao: 5/30/2025, Created person class
    """

# Add first_name and last_name properties to the constructor
    def __init__(self, student_first_name: str = '', student_last_name: str = ''):
        """
        Initialize a Person object with first and last name
        ChangeLog: ADuldulao, 5/31/2025, Created Method docstrings
        """
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

# Create a getter and setter for the first_name property
    @property
    def student_first_name(self):
        return self.__student_first_name.title()

    @student_first_name.setter
    def student_first_name(self, value: str):
        if value.replace(" ", "").isalpha() or value == "":
            self.__student_first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

# Create a getter and setter for the last_name property
    @property
    def student_last_name(self):
        return self.__student_last_name.title()

    @student_last_name.setter
    def student_last_name(self, value: str):
        if value.replace(" ", "").isalpha() or value == "":
            self.__student_last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")
    # Override the __str__() method to return Person data
    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name}'

#  Create a Student class the inherits from the Person class
class Student(Person):
    """
      A class representing student data, inheriting from Person.

      Properties:
          first_name (str): The student's first name.
          last_name (str): The student's last name.
          course_name (str): The course_name of the student.

      ChangeLog: (Who, When, What)
      ADuldulao: 5/30/2025, Created student class
      """
    #  call to the Person constructor and pass it the first_name and last_name data
    def __init__(self, student_first_name: str = '', student_last_name: str = '', course_name: str = ''):
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name)
    #  add a assignment to the course_name property using the course_name parameter
        self.__course_name = course_name

    # add the getter for course_name
    @property
    def course_name(self):
        return self.__course_name.title()

    # add the setter for course_name
    @course_name.setter
    def course_name(self, value: str):
        self.__course_name = value

    # Override the __str__() method to return the Student data
    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name},{self.course_name}'

#---Processing------------------------------------------------------------------------------#
class FileProcessor:
    """
    A class for reading and writing student data to/from a JSON file.
    This class provides static method to read student data from JSON file into a list
    of Student objects, and to write a list of
    Student objects to a JSON file as a list of dictionaries.

    ChangeLog: (Who, When, What)
    ADuldulao, 5/30/2025, Created class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function attempts to open and read a JSON file, parse its contents into a list,
        and return the list. It handles errors such as missing files or invalid JSON file format
        and print appropriate error message.
        :param file_name: string data with name of file to read from
        :return: list: The updated student_data  list containing Student objects
         ChangeLog: (Who, When, What)
    ADuldulao, 5/30/2025, Created function
        """
        file = None
        try:
            file = open(file_name, 'r')
            list_of_dictionary_data = json.load(file)
            # this line of code to convert dictionary data to Student data
            for student_dict in list_of_dictionary_data:
                student_object: Student = Student(student_first_name=student_dict["FirstName"],
                                                  student_last_name=student_dict["LastName"],
                                                  course_name=student_dict["CourseName"])
                students.append(student_object)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
            print("To prevent confusion. PRESS 4 TO EXIT IMMEDIATELY!!!")
        except Exception as e:
            IO.output_error_messages("Please check that the data is a valid JSON format!", e)
            print(e)
            print("To prevent confusion. PRESS 4 TO EXIT IMMEDIATELY!!!")
        finally:
            if file is not None and not file.closed:
                file.close()
        return students
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This functions writes a list to specified file in JSON format.
        It handles errors such as invalid JSON data or other issues.
        It will show the current student is being saved in the list.
        :param file_name: string data with name of file to read from
         ChangeLog: (Who, When, What)
    ADuldulao, 5/30/2025, Created Function
        """
        file = None
        try:
            #  code to convert Student objects into dictionaries (Done)
            list_of_dictionary_data: list = []
            for student in students:
                student_json: dict \
                    = {"FirstName": student.student_first_name,
                       "LastName": student.student_last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file, indent=1)  # Added the indent so that my datas are easily readable.
            file.close()
            if students:
               current_student = students[-1] # To show only the last student registered and not the whole registration
               print("The following student was added to list!")
               print(f'Student {current_student.student_first_name} '
                        f'{current_student.student_last_name} is enrolled in {current_student.course_name}')
        except TypeError as e:
            IO.output_error_messages("Please make sure that the data is a valid JSON format!\n", e)
        except Exception as e:
            IO.output_error_messages("\nThere was a non-specific error!\n", e)
        finally:
            if file is not None and not file.closed:
                file.close()
#---Presentation----------------------------------------------------------------------------------------------#
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog:(Who, When, What)
    ADuldulao, 5/30/2025, Created Clas
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This Function displays that a custom error messages to the user
        :param message: spring with message data to display
        :param error: Exception object with technical message to display
        :return: None
         ChangLog: (Who,When,What)
        ADuldulao, 5/30/2025
        """
        print(message, end="\n\n")
        if error is not None:
            print("-----Technical Error Message------")
            print(error, error.__doc__, type(error), sep='\n')
    @staticmethod
    def output_menu(menu: str):
        """
        This function displays a menu of choices to the user
        :return: None
        """
        print()
        print(menu)
        print()
    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user
        :return: string with the user choice
         ChangeLog: (Who, When, What)
         ADuldulao, 5/30/2025, Created Function
        """
        choice = "0"
        try:
            choice = input("What would you like to do: \n")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice
    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets the User first name, last name, and course name.
        The input data is used to create Student object
        :param student_data: list of dictionary rows to be filled with input data
        :return: list: The updated student_data list containing Student objects
         ChangeLog: (Who, When, What)
         ADuldulao, 5/30/2025, Created Function
        """
        try:
            #  this code to use a Student objects instead of a dictionary objects
            student = Student()
            student.student_first_name = input("What is the student's first name? \n")
            student.student_last_name = input("What is the student's last name? \n")
            student.course_name = input("Please enter the name of the course: \n")
            print(f"You have registered {student.student_first_name} {student.student_last_name}"
                  f" for {student.course_name}.")
            students.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return students
    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the list of registered students and courses. It will display a string
        of comma-separated values for each row collected in the students variable
        :return: None
         ChangeLog: (Who, When, What)
         ADuldulao, 5/30/2025, Created Function
        """
        print("The current registration data: ")
        print("-" * 47)
        for student in students:
            #  code to access Student object data instead of dictionary data
            message = "{},{},{}"
            print(message.format(student.student_first_name,
                                 student.student_last_name,
                                 student.course_name))
        print("-" * 47)
        print()
#---Beginning of the main body of the script-----------------------------------------------------------#
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
#---Present and Process the Data-----------------------------------------------------------------------#
while (True):
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()
    # Present the menu of choices    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue
        # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        # Process the data to create and display a custom message
        continue
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please select only 1,2, and 3. Select 4 to exit")
        continue
print("Program Ended")
