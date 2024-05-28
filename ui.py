import os
from colorama import Fore

import json

def generate_test_file():
    # Get user inputs
    doc_name = input("Enter document name: ")
    path = input("Enter file path: ")

    # Get files priority
    files_priority = []
    while True:
        file_name = input("Enter file name (or type 'done' to finish): ")
        if file_name.lower() == 'done':
            break
        files_priority.append(file_name)

    # Get extended files names
    extended_files_names = {}
    for file_name in files_priority:
        extended_name = input(f"Enter extended name for {file_name} (or press Enter for None): ")
        extended_files_names[file_name] = extended_name if extended_name != '' else None

    # Get excluded files names
    excluded_files_names = []
    while True:
        excluded_file_name = input("Enter excluded file name (or type 'done' to finish): ")
        if excluded_file_name.lower() == 'done':
            break
        excluded_files_names.append(excluded_file_name)

    # Get test scheme
    test_scheme = []
    while True:
        test_type = input("Enter test type (or type 'done' to finish): ")
        if test_type.lower() == 'done':
            break
        test_function = input("Enter test function: ")
        test_scheme.append([test_type, test_function])

    # Get test titles
    test_titles = {}
    for test_type in test_scheme:
        title = input(f"Enter title for {test_type[0]} test: ")
        test_titles[test_type[0]] = title

    # Get marginalia
    marginalia = {}
    while True:
        unit_name = input("Enter unit name (or type 'done' to finish): ")
        if unit_name.lower() == 'done':
            break
        header_image = input(f"Enter header image path for {unit_name}: ")
        footer_image = input(f"Enter footer image path for {unit_name}: ")
        marginalia[unit_name] = {
            "header": {"content": {"background_image": header_image}},
            "footer": {"content": {"background_image": footer_image}}
        }

    # Create dictionary
    generated_data = {
        "doc_name": doc_name,
        "path": path,
        "files_periority": files_priority,
        "extended_files_names": extended_files_names,
        "excluded_files_names": excluded_files_names,
        "test_scheme": test_scheme,
        "test_titles": test_titles,
        "marginalia": marginalia
    }

    # Convert to JSON and save to file
    with open("generated_file.json", "w") as json_file:
        json.dump(generated_data, json_file, indent=4)

if __name__ == "__main__":
    generate_test_file()

class BookScheme:
    def __init__(self):
        self.scheme = {}

    def create_book_scheme(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        self.scheme = {'Title': title, 'Author': author, 'Genre': genre}
        print("Book scheme created successfully!")

    def use_book_scheme(self):
        if not self.scheme:
            print("Please create a book scheme first.")
        else:
            print("Current Book Scheme:")
            for key, value in self.scheme.items():
                print(f"{key}: {value}")

    def create_quiz(self):
        print("Quiz creation feature coming soon!")

# Main menu
def main_menu():
    book_scheme = BookScheme()

    while True:
        print("\nMain Menu:")
        print("1. Create Book Scheme")
        print("2. Use Book Scheme")
        print("3. Create Quiz")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            book_scheme.create_book_scheme()
        elif choice == '2':
            book_scheme.use_book_scheme()
        elif choice == '3':
            book_scheme.create_quiz()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()

