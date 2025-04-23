def modify_content(content):
    # example: Title case conversion and line numbers
    lines = content.splitlines()
    modified = [f"{i+1}: {line.title()}" for i, line in enumerate(lines)]
    return "\n".join(modified)

def read_and_write_file():
    filename = input("Enter the name of the file to read: ")
    file = None

    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except IOError:
        print(" Error: Could not read the file due to an I/O issue.")
    else:
        modified_content = modify_content(content)
        new_filename = "modified_" + filename

        try:
            with open(new_filename, 'w') as new_file:
                new_file.write(modified_content)
            print(f" Success: Modified content written to '{new_filename}'.")
        except IOError:
            print(" Error: Could not write to the new file.")
    finally:
        if file:
            file.close()
            print("File closed.")
        print("Process complete.")

# Run the function
read_and_write_file()
