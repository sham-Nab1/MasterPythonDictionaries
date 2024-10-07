# Employee Table
employee_object1 = {
    "ID": 1,
    "Name": "John Doe",
    "Department": "Sales",
    "Age": 30,
    "Email": "john.doe@company.com"
}

employee_object2 = {
    "ID": 2,
    "Name": "Jane Smith",
    "Department": "Human Resources",
    "Age": 25,
    "Email": "jane.smith@company.com"
}

employee_object3 = {
    "ID": 3,
    "Name": "Mark Johnson",
    "Department": "IT",
    "Age": 40,
    "Email": "mark.johnson@company.com"
}

employee_object4 = {
    "ID": 4,
    "Name": "Lisa Wong",
    "Department": "Marketing",
    "Age": 28,
    "Email": "lisa.wong@company.com"
}

employee_object5 = {
    "ID": 5,
    "Name": "Paul McDonald",
    "Department": "Finance",
    "Age": 35,
    "Email": "paul.mcdonald@company.com"
}

# List of employee objects
employee_objects = [employee_object1, employee_object2, employee_object3, employee_object4, employee_object5]

# Print employee details
for employee in employee_objects:
    print(f"ID: {employee['ID']}, Name: {employee['Name']}, Department: {employee['Department']}, Age: {employee['Age']}, Email: {employee['Email']}")
