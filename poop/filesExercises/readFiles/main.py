import json
import csv
file_path = 'pythonExercise/poop/filesExercises/files/output.txt'
second_file_path = 'pythonExercise/poop/filesExercises/files/employees.json'
third_file_path = 'pythonExercise/poop/filesExercises/files/employees_list.csv'

def read(file_path):
    try:
        with open(file_path, 'r') as file:
            if(file_path.endswith('.json')):
                content = json.load(file)
            elif(file_path.endswith('.csv')):
                content = csv.reader(file)
                content = [line for line in content]
            else:
                content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

print("TEXT")
print("======================================")
print(read(file_path))
print("======================================")
print("JSON")
print("======================================")
print(read(second_file_path))
print("======================================")
print("CSV")
print("======================================")
print(read(third_file_path))