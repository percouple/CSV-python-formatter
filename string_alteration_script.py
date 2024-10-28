# Alter the input file as necessary in between the long hash lines 
# The input file is opened as inputFile. Use print() to list to csv

import imaplib
import argparse
import csv

def main(input_file):
    
    # Open input file and read its contents 
    # Read a CSV file
    with open(input_file, mode='r') as fileContent:
        csv_reader = csv.reader(fileContent)

    # Modify fileContent below to manipulate the csv string
    ########################################################################
        # Here you can manipulate each row as needed
        # For example, let's print each row
        for row in csv_reader:
            print(row)
            # for col in range(4): 
            #     # Example manipulation: converting each item to uppercase

            #     print(row[col])
    ########################################################################

# Main function call    
if __name__ == "__main__":
    
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Process an input file.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    
    args = parser.parse_args()
    
    # Call the main function with the provided file path
    main(args.input_file)