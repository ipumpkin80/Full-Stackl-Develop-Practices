def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example usage
try:
    score = float(input("Enter the student's score: "))
    if 0 <= score <= 100:
        grade = determine_grade(score)
        print(f"The student's grade is: {grade}")
    else:
        print("Please enter a valid score between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
