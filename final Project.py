from bs4 import BeautifulSoup
import requests
import csv

urls = ['https://www.newegg.com/d/Best-Sellers/Gaming-Desktops/s/ID-3742?tid=897483', 'https://www.newegg.com/d/Best-Sellers/Gaming-Desktops/s/ID-3742/Page-2?tid=897483', 'https://www.newegg.com/d/Best-Sellers/Gaming-Desktops/s/ID-3742/Page-3?tid=897483', 'https://www.newegg.com/d/Best-Sellers/Gaming-Desktops/s/ID-3742/Page-4?tid=897483', 'https://www.newegg.com/d/Best-Sellers/Gaming-Desktops/s/ID-3742/Page-5?tid=897483']
number = int(input("What page would you like to recieve from 1-5: "))     ##Input for the page you would like to see of the computers, corresponding number is then taken to the url list.
source = requests.get(urls[number-1])                           ##Input for getting html from the specific url
soup = BeautifulSoup(source.content,'html.parser')              ##Parses the HTML into a readable format in python
budget = int(input("What is your max budget?: "))               ##Asking the user for a max budget
title = soup.find_all('a', class_="goods-title")                ##Finds all the titles on the page through finding the specific class type in the HTML
elems = soup.find_all('div', class_='grid-col bg-white')            ##Finds all of the listings
soldout = soup.find_all('div', class_='goods-price-soldout text-darkorange')        ##Finds the sold out listings just in case there is no price since they are different classes
price = soup.find_all('span', class_='goods-price-value')       ##Finds all the prices of each listing
dollars = []             ##Creating a list to store all of the price values
names = []                 ##Creating a list to store all of the Title values
for p in title:                   ##Appending each name to the list of names
    names.append(p.text)
for e in elems:                     ##Appending either sold out or the price to the dollars list 
    if e.find('div', class_='goods-price-soldout text-darkorange'):
        dollars.append(-1)
    else:
        dollars.append(float(e.find('span', class_='goods-price-value').text.replace(",","")))      ##Changes the string that it gets to a float and removes the commas and quotations
lst = {}                ##Creating a dictionary to pair up the Title and Price, and to make it easier to write to a csv file
for a in names:                      ##Appending the right key(title) to the right price in the dictionary
    for d in dollars:
        lst[a] = d
        dollars.remove(d)
        break
for k in lst:                               ##Iterates over the list checking the value of each key to see if it is under the budget or not, if not it is replaced.
    if lst[k] > budget or lst[k] == -1:
        lst[k] = "Out of Budget"
file = 'computers.csv'                      ##Creating a csv file 
with open(file, 'w') as f:                      ##Opening the csv file to write to it
    dict_writer = csv.writer(f)
    for l in lst:                                   ##Writing to the rows of the csv file format, unfortunately could not figure out how to get the price in seperate columns
        dict_writer.writerow([l])
        dict_writer.writerow([lst[l]])
print("Created Computers.csv file on your Computer!")




    
    
    






