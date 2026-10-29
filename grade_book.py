
# grade_book.py
# A simple command-line grade book.

# students = {}  # name -> list of marks
students = {
    "Ali": [78, 91, 66]
}

def show_menu():
    print("\n=== Grade Book ===")
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

        if choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
show_grades()

if __name__ == "__main__":
    main()
