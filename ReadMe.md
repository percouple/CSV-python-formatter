# CSV Formatter PowerShell Script

## Overview
This PowerShell script takes an input CSV file, processes it through a Python script for formatting, and then opens the formatted CSV in Microsoft Excel. This allows for easy viewing and further manipulation of the data.

## Features
- Accepts a CSV file as input.
- Executes a specified Python script to format the CSV.
- Opens the newly formatted CSV in Excel.
- Provides error handling and user prompts for a smooth user experience.

## Prerequisites
- **PowerShell**: Ensure you have PowerShell installed on your system.
- **Python**: Python must be installed, and the script `string_alteration_script.py` should be accessible.
- **Excel**: Microsoft Excel must be installed on your machine.

## Installation
1. Clone or download the repository containing this script and the Python script.
2. Ensure the Python script (`string_alteration_script.py`) is in the same directory as the PowerShell script.
3. Place the input CSV file in an accessible location.

## Usage
1. Open PowerShell.
2. Navigate to the directory where the script is located.
3. Run the script with the following command:

   ```powershell
   .\excelFormatterRunScript.ps1 "C:\path\to\your\input.csv"