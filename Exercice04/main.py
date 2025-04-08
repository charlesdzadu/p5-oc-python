"""Module containing student management classes and functions."""


class Student:
    """Class representing a student with name and grades."""

    def __init__(self, name, grades=None):
        """Initialize a student with name and grades.

        Args:
            name (str): The student's name
            grades (list, optional): List of student's grades. Defaults to None.
        """
        self.name = name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        """Add a new grade to the student's record.

        Args:
            grade (float): The grade to add
        """
        self.grades.append(grade)

    def calculate_average(self):
        """Calculate the student's average grade.

        Returns:
            float: The average grade, or 0 if no grades exist
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


def format_student_info(student):
    """Format student information into a string.

    Args:
        student (Student): The student object to format

    Returns:
        str: Formatted string with student information
    """
    average = student.calculate_average()
    return f"Student {student.name} has an average of {average:.2f}"


def main():
    """Main function to demonstrate the usage of Student class."""
    # Create a student instance
    student = Student("Alice", [85, 92, 78])
    
    # Add a new grade
    student.add_grade(90)
    
    # Print formatted student information
    print(format_student_info(student))


if __name__ == "__main__":
    main()
