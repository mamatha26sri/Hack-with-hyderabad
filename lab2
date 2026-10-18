def calculate_grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'E'

def main():
    print("Enter marks for 3 subjects (out of 100):")
    subject1 = float(input("Subject 1: "))
    subject2 = float(input("Subject 2: "))
    subject3 = float(input("Subject 3: "))

    total_marks = subject1 + subject2 + subject3
    percentage = total_marks / 3
    grade = calculate_grade(percentage)

    print(f"\nTotal Marks: {total_marks:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == '__main__':
    main()
