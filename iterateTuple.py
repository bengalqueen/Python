# Program to iterate the given tuples

employee1 = ("John Doe",101,"Human Resources",60000)
employee2 = ("Alice Smith",102,"Marketing",55000)
employee3 = ("Bob Johnson",103,"Engineering",75000)

# Store all employee tuples in a list
employees = [employee1, employee2, employee3]

# Iterate through each employee tuple
for emp in employees:
    print("Employee Records:")
    # Access and print each element of the tuple
    print("Name:", emp[0])          
    print("Employee ID:", emp[1])    
    print("Department:", emp[2])     
    print("Salary: $", emp[3])       
    # Blank line for better readability
    print()  