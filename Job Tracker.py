import csv
from datetime import datetime

FILENAME = "job_applications.csv"

# Initialize CSV file if it doesn't exist
def initialize_file():
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Company", "Date Applied", "Status"])
    except FileExistsError:
        pass

# Function to add a new job application
def add_application():
    company = input("Enter company name: ")
    date_applied = datetime.today().strftime('%Y-%m-%d')
    status = "Pending"
    
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([company, date_applied, status])
    print("Application added successfully!\n")

# Function to view all applications
def view_applications():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            data = list(reader)
            
            if len(data) <= 1:
                print("No applications found.\n")
                return
            
            for row in data:
                print(" | ".join(row))
            print()
    except FileNotFoundError:
        print("No applications found.\n")

# Function to update application status
def update_status():
    company_name = input("Enter company name to update status: ")
    new_status = input("Enter new status (Accepted/Denied/Pending): ").capitalize()
    
    updated = False
    rows = []
    
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() == company_name.lower():
                row[2] = new_status
                updated = True
            rows.append(row)
    
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    if updated:
        print("Application status updated successfully!\n")
    else:
        print("Company not found.\n")

# Function to delete an application
def delete_application():
    company_name = input("Enter company name to delete: ")
    rows = []
    deleted = False
    
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() == company_name.lower():
                deleted = True
            else:
                rows.append(row)
    
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    if deleted:
        print("Application deleted successfully!\n")
    else:
        print("Company not found.\n")

# Main menu
def main():
    initialize_file()
    
    while True:
        print("Job Tracker Menu:")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Update Application Status")
        print("4. Delete Application")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_application()
        elif choice == "5":
            print("Exiting Job Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()