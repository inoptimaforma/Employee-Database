import sqlite3
from datetime import datetime

if __name__ == "__main__":
    dao = EmployeeDAO()

    print("\n=== Inserting Employees ===")
    emp1 = Employee(name="Matthew Mcconaughey", position="Actor", salary=2500000, hire_date="1990-07-22")
    emp2 = Employee(name="Natalie Portman", position="Actress", salary=4000000, hire_date="1994-04-13")
    
    dao.insert(emp1)
    dao.insert(emp2)
    print(f"Inserted: {emp1}")
    print(f"Inserted: {emp2}")

    print("\n=== Getting Employee by ID ===")
    found_emp = dao.get_by_id(emp1.id)
    print(f"Found employee by ID {emp1.id}: {found_emp}")

    print("\n=== Getting All Employees ===")
    all_employees = dao.get_all()
    for emp in all_employees:
        print(emp)

    print("\n=== Updating Employee ===")
    emp1.name = "Matthew David Mcconaughey"
    emp1.salary = 3500000
    dao.update(emp1)
    updated_emp = dao.get_by_id(emp1.id)
    print(f"Updated employee: {updated_emp}")

    print("\n=== Deleting Employee ===")
    delete_id = emp2.id
    dao.delete(delete_id)
    print(f"Deleted employee with ID: {delete_id}")

        print("\n=== Final Employee List ===")
    remaining_employees = dao.get_all()
    for emp in remaining_employees:
        print(emp)