class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        result = [employee for employee in self.employees if employee.age == age]
        return result

    def search_by_name(self, name):
        result = [employee for employee in self.employees if employee.name.lower() == name.lower()]
        return result

    def search_by_salary(self, operator, salary):
        operators = {
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '>=': lambda x, y: x >= y,
            '<=': lambda x, y: x <= y
        }
        result = [employee for employee in self.employees if operators[operator](employee.salary, salary)]
        return result

    def display_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            for employee in results:
                print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

def main():
    database = EmployeeDatabase()

    # Add sample employees to the database
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        age = int(input("Enter the age to search: "))
        results = database.search_by_age(age)
    elif choice == '2':
        name = input("Enter the name to search: ")
        results = database.search_by_name(name)
    elif choice == '3':
        operator = input("Enter the salary operator (> / < / >= / <=): ")
        salary = int(input("Enter the salary to search: "))
        results = database.search_by_salary(operator, salary)
    else:
        print("Invalid choice")
        return

    database.display_results(results)

if __name__ == "__main__":
    main()
