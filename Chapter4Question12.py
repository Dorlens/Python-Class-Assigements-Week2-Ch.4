
#Dorlens Janvier Chapter 4 Question 12 





def calculate_wages(hourly_wage, hours_worked):
    # Calculate wages based on hourly wage and hours worked
    return hourly_wage * hours_worked

def generate_report(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Print table headers
            print("Employee Name\tHours Worked\tWages Paid")
            print("-------------------------------------------")
            
            # Read each line of the file
            for line in file:
                # Split the line into parts
                parts = line.strip().split()
                # Check if the line has valid data
                if len(parts) == 3:
                    # Extract employee information
                    last_name, hourly_wage, hours_worked = parts
                    # Convert hourly wage and hours worked to numbers
                    hourly_wage = float(hourly_wage)
                    hours_worked = float(hours_worked)
                    # Calculate wages paid
                    wages_paid = calculate_wages(hourly_wage, hours_worked)
                    # Print employee details in tabular format
                    print(f"{last_name}\t\t{hours_worked}\t\t{wages_paid:.2f}")
                else:
                    # Print a warning for invalid data format
                    print("Invalid data format in line:", line.strip())
    except FileNotFoundError:
        # Print an error message if the file is not found
        print("File not found.")

def main():
    # Prompt the user to enter the filename
    filename = input("Enter the filename: ")
    # Generate and print the report
    generate_report(filename)

if __name__ == "__main__":
    # Call the main function when the script is run
    main()