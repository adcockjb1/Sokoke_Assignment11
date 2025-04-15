# File Name: main.py
# Student Name: Chrystie Cadet
#               Joseph Adcock
# email: cadetce@mail.uc.edu
#        adcockjb@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: 4/17/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The project takes a .csv file and cleans the data

# Brief Description of what this module does: This module serves as the entry point for the program
# Citations: ChatGPT

# Anything else that's relevant: Other issues with the data:
#       - The dates are all formatted differently
#       - Fuel Quantity is all rounded differently
#       - The last few hundred records are out of order
#       - Inconsistent naming for Fuel Type

from extractCSVPackage.extractCSV import*
from transformationPackage.transformData import*
from loadCSVPackage.loadCSV import*

if __name__ == "__main__":

    path = "Data/"

    # Extract CSV into Dictionary
    csvConv = extractListFromCSV()
    originalFileName = path + "fuelPurchaseData.csv"

    rawData = csvConv.convertToList(originalFileName)


    # Transfrom CSV
    transformer = transformList()

    rawData = transformer.roundToTwo(rawData)

    rawData = transformer.removeDuplicates(rawData)

    anomolyRecords = transformer.documentAnomolies(rawData)
    rawData = transformer.removeAnomolies(rawData)

    rawData = transformer.fixZips(rawData)


    # Load to CSV
    dictionaryConv = loadCSVFromList()
    cleanedFileName = path + "cleanedData.csv"
    anomaliesFileName = path + "dataAnomalies.csv"

    cleanedData = dictionaryConv.convertToCSV(rawData, cleanedFileName)
    anomalyData = dictionaryConv.convertToCSV(anomolyRecords, anomaliesFileName)