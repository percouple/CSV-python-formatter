# Take in an input csv file
# Run it through python script for formatting purposes
# Open the new csv in excel on the user's computer


# Enables advanced functions in Powershell
[CmdletBinding()]

# Defines parameter for 
param (
    [string]$dataFilePath
)

Write-Output "
    Formatting CSV input from $($dataFilePath)"

# Check if the data file path was provided
if (-not $dataFilePath) {
    # Prompt the user to input the data file path if not provided
    $dataFilePath = Read-Host -Prompt "     Please enter the path to the data file"
}

# Try/Catch for python formatting script execution to provide for errors
Try {
    # Execute Python script and redirect output to a CSV
    python ".\string_alteration_script.py" $dataFilePath > ".\testOutput.csv";
    Write-Output "
    Successful execution of python script,
    Handling CSV conversion now..."
} Catch {
    # Error Handling   
    Write-Output "
    Issue routing through python script - $($_.Exception.Message)"
}

# Open Excel on the current machine with a new workbook
Try {
    # Create a new Excel application instance
    $excel = New-Object -ComObject Excel.Application;

    # Make excel visible
    $excel.Visible = $true;

} Catch {
    Write-Output "
    There was an error opening Excel on this machine: `n$($_.Exception.Message))"
}

# Open the CSV file in the excel workbook
Try {
    # Establish output path
    $csvFilePath = Join-Path -Path $PSScriptRoot -ChildPath "\testOutput.csv"

    # Open the csv with the workbook
    $workbook = $excel.Workbooks.Open($csvFilePath)

    # Success message
    Write-Output "
    Successfully opened file in excel
    "
} Catch {
    Write-Output "
    There was an error opening the output file: 
    $($_.Exception.Message)
    "
}