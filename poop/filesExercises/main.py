import os 
import json
import csv
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "files/test.txt")


if os.path.exists(file_path):
    print(f"File exists at location: {os.path.abspath(file_path)}")

    if os.path.isfile(file_path):
        print(f"File is a regular file: {file_path}")
    elif os.path.isdir(file_path):
        print(f"File is a directory: {file_path}")
else:
    print("File does not exist")


# Create a new file and write data to it
txt_data = "This is a test file."
second_file_path=os.path.join(script_dir, "files/output.txt")

with open(second_file_path, "a") as file:
    file.write(txt_data+"\n")
    print(f"Data written to {second_file_path}")


employees = ["John Doe", "Jane Smith", "Alice Johnson"]
second_file_path=os.path.join(script_dir, "files/second_output.txt")

with open(second_file_path, "a") as file:
    for employee in employees:
        file.write(employee+"\n")
    print(f"Data written to {second_file_path} as text")

# Create a dictionary of employees to store as json file
employees_dict = {
    "employees": [
        {"name": "John Doe", "age": 30, "department": "HR"},
        {"name": "Jane Smith", "age": 25, "department": "IT"},
        {"name": "Alice Johnson", "age": 28, "department": "Finance"}
    ]
}

dicitonary_file_path=os.path.join(script_dir, "files/employees.json")

try:
    with open(dicitonary_file_path, "w") as file:
        json.dump(employees_dict, file, indent=4)
        print(f"Data written to {dicitonary_file_path} as json")
except FileExistsError as e:
    print(f"File already exists: {e}")


employess_list = [["Name", "Age", "Department"],
                  ["John Doe", 30, "HR"],
                  ["Jane Smith", 25, "IT"],
                  ["Alice Johnson", 28, "Finance"],
                  ["Bob Brown", 35, "Marketing"],
                  ["Charlie Davis", 40, "Sales"],
                  ["David Wilson", 45, "Operations"],
                  ["Eve Taylor", 50, "Research"],
                  ["Frank Anderson", 55, "Development"],
                  ["Grace Thompson", 60, "Support"],]

list_file_path=os.path.join(script_dir, "files/employees_list.csv")

try:
    with open(list_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employess_list:
            writer.writerow(row)
        print(f"Data written to {list_file_path} as csv")
except FileExistsError as e:
    print(f"File already exists: {e}")