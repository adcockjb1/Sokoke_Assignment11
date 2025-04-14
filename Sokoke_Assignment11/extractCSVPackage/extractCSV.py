# File Name: dictFromCSV.py
# Student Name: Chrystie Cadet
#               Joseph Adcock
# email: cadetce@mail.uc.edu
#        adcockjb@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: 4/17/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The project takes a .csv file and cleans the data

# Brief Description of what this module does: This module extracts the CSV into python data structures
# Citations: ChatGPT

# Anything else that's relevant: N/A

import csv

class extractListFromCSV:
    def convertToList(self, fileName):
        """
        Convert a CSV to a Python List of Dictionaries
        @param filename String: Name of the file to convert
        @return List of data from the file
        """

        with open(fileName, mode="r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        return data