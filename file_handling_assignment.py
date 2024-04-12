try:
    # Step 1: Creating a new text file in write mode and writing to it
    with open("my_file.txt", "w") as file:
        # Writing three lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")  # Including a mix of strings and numbers
        file.write("Python is fun!")

    # Step 2: Reading and displaying the contents of the file
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())

    # Step 3: Appending three additional lines of text to the existing content
    with open("my_file.txt", "a") as file:
        # Appending three more lines of text
        file.write("\nAppending line 1\n")
        file.write("98765\n")  # Including a mix of strings and numbers
        file.write("File handling in Python is awesome!")

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied to access the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Script execution completed.")
