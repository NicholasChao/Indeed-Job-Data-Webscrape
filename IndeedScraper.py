#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:45:46 2017

@author: NicholasChao
"""

import requests
from bs4 import BeautifulSoup
import xlwt


# Note: for cities whose name consists of more than
# one word, replace space with "+".
# e.g. for New York, write getSoup("new+york")

# function getData() will take city's name and return an array of salary data
 
def getSalary(cityName):
    page = requests.get("https://www.indeed.com/jobs?q=&l=" + cityName)
    soup = BeautifulSoup(page.content, 'html.parser')
    rbListSalary = soup.find_all(class_="rbList")[0]
    salaryArray = rbListSalary.find_all('a')
    returnSalaryArray = []
    for i in range(len(salaryArray)):
        returnSalaryArray.insert(0, (cityName + " " + salaryArray[i]['title']).split())
    return returnSalaryArray

# function getJobType() will return job type data
def getJobType(cityName):
    page = requests.get("https://www.indeed.com/jobs?q=&l=" + cityName)
    soup = BeautifulSoup(page.content, 'html.parser')
    rbListSalary = soup.find_all(class_="rbList")[1]
    salaryArray = rbListSalary.find_all('a')
    returnSalaryArray = []
    for i in range(len(salaryArray)):
        returnSalaryArray.insert(0, (cityName + " " + salaryArray[i]['title']).split())
    return returnSalaryArray

# function getJobLevel() will return job level data
def getJobLevel(cityName):
    page = requests.get("https://www.indeed.com/jobs?q=&l=" + cityName)
    soup = BeautifulSoup(page.content, 'html.parser')
    rbListSalary = soup.find_all(class_="rbList")[4]
    salaryArray = rbListSalary.find_all('a')
    returnSalaryArray = []
    for i in range(len(salaryArray)):
        jobLevelArray = salaryArray[i]['title'].split()
        del jobLevelArray[1]
        jobLevelArray.insert(0, cityName)
        returnSalaryArray.insert(0, jobLevelArray)   
    return returnSalaryArray

# this function will take in input of the three data types and


def getFullData(cityName):
    array = getSalary(cityName) + getJobType(cityName) + getJobLevel(cityName)
    return array


# this function will convert out data into a spreadsheet

def getSpreadSheet(data):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('sheet1')
    k = 1
    for i in range(len(data)):
        if i%14 == 0:
            sheet.write(k, 0, data[i][0])
            k+=1
    x = 1
    j = 1
    for i in range(len(data)):
        sheet.write(x, j, data[i][2])
        j+=1
        if (i+1)%14 == 0:
            x += 1
            j = 1
    for i in range(14):
        sheet.write(0, i+1, data[i][1])
    workbook.save("workBook.xls")

          


