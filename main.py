import sys
from tabulate import tabulate

def load_csv_data(filename, delimiter=','):
    lines = []
    try:
        with open(filename) as file: #using filename instead of "filName"
            for line in file:
                line = line.strip()
                if line:
                    lines.append(line.split(delimiter))  #using delimiter variable instead of 'delimiter'
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    return lines

def sort_data(data, column):
    if column >= len(data[0]):
        print("Invalid column index for sorting")
        return data
    sorted_data = [data[0]] + sorted(data[1:], key=lambda x: x[column])
    return sorted_data

def filter_data(data, column, value):
    if column >= len(data[0]):
        print("Invalid column index for filtering")
        return data
    filtered = [data[0]] + [row for row in data[1:] if row[column].strip() == value]
    return filtered

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python script.py filename.csv")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        print("File is not a csv file")
        sys.exit()  #correcting the indentation

    delimiter = input("Enter the delimiter (default is comma): ")
    if not delimiter:
        delimiter = ','

    lines = load_csv_data(filename, delimiter)
    original_lines = lines[:]  # Make a copy of the original data

    headings = lines[0]

    while True:
        print(tabulate(lines, headers="firstrow", tablefmt="grid"))

        choice = input("\nDo you want to:\n"
                       "1. Sort data\n"
                       "2. Filter data\n"
                       "3. Exit\n"
                       "Enter your choice: ")

        if choice == '1': #changed from integer to string for comparison
            column = int(input("Enter the column index to sort by: "))
            lines = sort_data(original_lines[:], column)  # Using a copy of the original data

        elif choice == '2':
            column = int(input("Enter the column index to filter by: "))
            value = input("Enter the value to filter for: ")
            lines = filter_data(original_lines[:], column, value)  # Use a copy of the original data

        elif choice == '3':
            sys.exit("Exiting the program")

        else:
            print("Invalid choice. Please choose again.")
