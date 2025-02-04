import os

def display_menu():
    print("\n===== Annem Saad Hotel Project UI =====")
    print("1) Login to Main Code")
    print("2) Login to Enhancement Code")
    print("3) Exit Code")
    
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("\nLaunching Main Code...")
            os.system("python main.py")  # Runs main.py
        elif choice == '2':
            print("\nLaunching Enhancement Code...")
            os.system("python Project_File_Enhancement5_db.py")  # Runs enhancement 5.py
        elif choice == '3':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
