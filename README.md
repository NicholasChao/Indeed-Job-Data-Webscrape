# Indeed-Job-Data-Webscrape
Python program to scrape Indeed job page for job market data.
_____
getFullData(cityName); takes a string input of a (US) city name and returns a matrix containing job market
data scraped from the Indeed page for that city.


ex.

getFullData('boston') returns:

[['boston', '$65,000', '(11493)'],
 ['boston', '$45,000', '(20687)'],
 ['boston', '$35,000', '(29728)'],
 ['boston', '$25,000', '(45572)'],
 ['boston', '$20,000', '(55079)'],
 ['boston', 'Internship', '(695)'],
 ['boston', 'Temporary', '(1236)'],
 ['boston', 'Commission', '(1460)'],
 ['boston', 'Contract', '(2425)'],
 ['boston', 'Part-time', '(10218)'],
 ['boston', 'Full-time', '(40178)'],
 ['boston', 'Senior', '(1142)'],
 ['boston', 'Mid', '(14085)'],
 ['boston', 'Entry', '(42354)']]
 
 _____
 getSpreadSheet(data); takes an input of a matrix (containing job market data for one or more cities) and creates an .xls 
 file of that data.
 
 You can easily combine data from cities using getFullData, then can pass the combined data through getSpreadSheet().
 
 ex.
 
 dataset = getFullData('boston') + getFullData('new-york') + getFullData('chicago')
 getSpreadSheet(dataset)
 
 
