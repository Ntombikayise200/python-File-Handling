# File handling assignment script

# File Creation, Writing, Reading, Appending and Error Handling

def create_and_write_file():
    """Creates a file and writes three lines of text to it."""
    try:
        # Step 1: Create and write to the file
        with open("my_file.txt", 'w') as file:  # Removed directory path
            file.write("This is the first line of text.\n")
            file.write("The second line includes a number: 12345.\n")
            file.write("Here's another line of text with a float: 3.14\n")
        print("File 'my_file.txt' created and written successfully.")
    
    except PermissionError:
        print("Error: You don't have permission to write to this file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
def read_file():
    """Reads the content of the file and displays it."""
    try:
        # Step 2: Read and display the file content
        with open("my_file.txt", 'r') as file:  # Removed directory path
            content = file.read()
            print("\nReading file 'my_file.txt':\n")
            print(content)
    
    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    """Appends three more lines of text to the file."""
    try:
        # Step 3: Open the file in append mode and write more lines
        with open("my_file.txt", 'a') as file:  # Removed directory path
            file.write("This is an appended line: adding more content.\n")
            file.write("Appending another number: 67890.\n")
            file.write("Final appended line with a float: 2.71\n")
        print("Successfully appended to 'my_file.txt'.")
    
    except PermissionError:
        print("Error: You don't have permission to append to this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the file operations."""
    try:
        create_and_write_file()   # Create and write to the file
        read_file()               # Read and display the file content
        
        append_to_file()          # Append new lines to the file
        read_file()               # Read and display the updated content
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operations complete.")

if __name__ == "__main__":
    main()
