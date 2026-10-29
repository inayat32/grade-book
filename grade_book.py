
# grade_book.py
# A simple command-line grade book.

students = {}  # name -> list of marks


def show_menu():
    print("\n=== Grade Book ===")
    print("1. Add student")
    print("2. Show grades")
    print("0. Exit")


def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 55:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    marks = input("Marks separated by spaces: ").strip()

    try:
        student_marks = [int(m) for m in marks.split()]

        if not student_marks:
            print("Please enter at least one mark.")
            return

        if any(mark < 0 or mark > 100 for mark in student_marks):
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid integer marks.")
        return

    students[name] = student_marks
    print(f"Added {name}.")


def show_grades():
    if not students:
        print("No students yet.")
        return

    for name, marks in students.items():
        average = sum(marks) / len(marks)
        print(
            f"{name}: average {average:.1f}, "
            f"grade {calculate_grade(average)}"
        )


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_grades()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
