# File Name: transformData.py
# Student Name: Chrystie Cadet
#               Joseph Adcock
# email: cadetce@mail.uc.edu
#        adcockjb@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: 4/17/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The project takes a .csv file and cleans the data

# Brief Description of what this module does: This module transforms the data in the list to reflect the assignments rules
# Citations: ChatGPT
#            https://app.zipcodebase.com/home

# Anything else that's relevant: N/A

import re
import json
import requests
import random

class transformList:

    def roundToTwo(self, data):
        """
        Rounds Gross Price to exactly 2 decimal places
        @param data List: The main list of data
        @param data List: The list with a rounded 'Gross Price' field
        """

        for row in data:
            price = float(row['Gross Price'])
            row['Gross Price'] = round(price, 2)
        
        return data


    def removeDuplicates(self, data):
        """
        Removes duplicate rows
        @param data List: The main list of data
        @param deDupedData List: The de-duped data
        """

        seen = set()
        deDupedData = []
    
        for row in data:
            rowTuple = tuple(sorted(row.items()))
            if rowTuple not in seen:
                seen.add(rowTuple)
                deDupedData.append(row)

        return deDupedData


    def removeAnomolies(self, data):
        """
        Audits records where customer did not purchase gas
        @param data List: The main list of data
        @param data List: The list of records with correct fuel types
        """

        data = [row for row in data if row.get('Fuel Type') != 'Pepsi']
        return data

    def documentAnomolies(self, data):
        """
        Removes records where customer did not purchase gas
        @param data List: The main list of data
        @param anomolies List: The list of records with anomoly data
        """

        anomolies = [row for row in data if row.get('Fuel Type') == 'Pepsi']
        return anomolies


    # Couldn't get to work
    def findZips(self, city, state, country, limit):
        """
        Adds zip code to address when missing
        @param data List: The main list of data
        @param data List: The list with a correct zip code in address
        """

        headers = {"apikey": "b38f7030-197c-11f0-8932-c5de6ec78589"}

        params = (
           ("city",city),
           ("state_name",state),
           ("country",country),
           ("limit",limit)
        )

        response = requests.get('https://app.zipcodebase.com/api/v1/code/city', headers=headers, params=params)
        string = response.content
        zipDictionary = json.loads(string)

        return zipDictionary["Results"]

    # Does nothing
    def fixZips(self, data):
        """
        Adds zip code to address when missing
        @param data List: The main list of data
        @param data List: The list with a correct zip code in address
        """



        return data