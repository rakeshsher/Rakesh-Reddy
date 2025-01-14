# -*- coding: utf-8 -*-
"""Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z876K6rPQEh1l4hvtWkLJ5H6n9SAYYfP
"""

def calculate_grade(marks1, marks2, marks3):
    """
    Calculates the grade based on the average of three subject marks.

    Args:
        marks1: Marks in the first subject.
        marks2: Marks in the second subject.
        marks3: Marks in the third subject.

    Returns:
        str: The calculated grade.
    """
    average = (marks1 + marks2 + marks3) / 3

    if average >= 90:
        return "Grade: A"
    elif 80 <= average < 90:
        return "Grade: B"
    elif 70 <= average < 80:
        return "Grade: C"
    else:
        return "Grade: Fail"


# Get input from the user
try:
    marks1 = float(input("Enter marks in subject 1: "))
    marks2 = float(input("Enter marks in subject 2: "))
    marks3 = float(input("Enter marks in subject 3: "))

    # Ensure the marks are valid
    if 0 <= marks1 <= 100 and 0 <= marks2 <= 100 and 0 <= marks3 <= 100:
        # Calculate and print the grade
        grade = calculate_grade(marks1, marks2, marks3)
        print(grade)
    else:
        print("Error: Marks should be between 0 and 100.")
except ValueError:
    print("Error: Please enter valid numerical marks.")