# Alter the input file as necessary in between the long hash lines 
# The input file is opened as inputFile. Use print() to list to csv

import imaplib
import argparse

def main(input_file):
    
    # Open input file and read its contents 
    with open(input_file, 'r') as inputFile:
        fileContent = inputFile.read()

    # Modify fileContent below to change the file in python
    ########################################################
    curWord = ''
    for i in range(len(fileContent)):
        curWord += fileContent[i]
        if fileContent[i+1] == ',': 
            print(curWord)
            curWord = ''
    
    
    # Print stuff to make sure things are running correctly
    # print(fileContent)
    # print("running - you're doing a right swell job my guy")
    
    #########################################################

# Main function call    
if __name__ == "__main__":
    
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Process an input file.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    
    args = parser.parse_args()
    
    # Call the main function with the provided file path
    main(args.input_file)