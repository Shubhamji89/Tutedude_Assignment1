def main_menu(employees):
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            
# function for add add employee 
def add_employee(employees):
    while True:
        try:
            emp_id = int(input("Enter Employee ID (integer): ").strip())
            if emp_id in employees:
                print("Employee ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for Employee ID.")

    name = input("Enter Employee Name: ").strip()
    while True:
        try:
            age = int(input("Enter Employee Age: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for Age.")

    department = input("Enter Employee Department: ").strip()
    while True:
        try:
            salary = float(input("Enter Employee Salary: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Salary.")

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"Employee {name} added successfully.")

# function for view employee
def view_employees(employees):
    if not employees:
        print("No employees available.")
        return

    print("\n{:<10} {:<20} {:<5} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)
    for emp_id, details in employees.items():
        print("{:<10} {:<20} {:<5} {:<15} {:<10.2f}".format(
            emp_id,
            details['name'],
            details['age'],
            details['department'],
            details['salary']
        ))

# function for search employee

def search_employee(employees):
    try:
        emp_id = int(input("Enter Employee ID to search: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid integer for Employee ID.")
        return

    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nDetails of Employee ID {emp_id}:")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']:.2f}")
    else:
        print("Employee not found.")


if __name__ == "__main__":
    # Initialize with sample data
    employees = {
        101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
        102: {'name': 'Anita', 'age': 30, 'department': 'IT', 'salary': 60000},
        103: {'name': 'Ravi', 'age': 25, 'department': 'Finance', 'salary': 55000},
    }
    main_menu(employees)