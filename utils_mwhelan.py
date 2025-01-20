
"""
Module: utils_mwhelan

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Meghan Whelan

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
is_publicly_funded: bool = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
number_of_students_awarded: int = 4

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_amount_of_grants: float = 1166.45

# declare a list of strings
# TODO: Add or replace this with your own list  
grants_offered: list = ["PELL", "Access Missouri", "SEOG"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
amount_of_grants: list = [700.5, 54.75, 3400.3, 510.25]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_grant: float = min(amount_of_grants)  
max_grant: float = max(amount_of_grants)  
mean_grant: float = statistics.mean(amount_of_grants)  
stdev_grant: float = statistics.stdev(amount_of_grants)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Higher Education in Missouri: Public Grants
---------------------------------------------------------
Is publicly funded:          {is_publicly_funded}
Number of students awarded:  {number_of_students_awarded}
Grants Offered:              {grants_offered}
Amount of Grants:            {amount_of_grants}
Minimum Grant Amount:        {min_grant}
Maximum Grant Amount:        {max_grant}
Mean Grant Amount: {mean_grant:.2f}
Standard Deviation of Grant Amounts: {stdev_grant:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
