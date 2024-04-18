
# Dorlens Janvier Chapter 4 Question 8

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
            with open(destination_file, 'w') as destination:
                destination.write(content)
        print("File copied successfully!")
    except FileNotFoundError:
        print("One of the files does not exist.")

def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()