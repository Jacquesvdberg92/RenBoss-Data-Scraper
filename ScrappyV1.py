#install requests
#install bs4
from bs4 import BeautifulSoup
import requests
import time
import sqlite3

#for testing
startTime = time.time()
iterations = 0
print("Run Started")

# Connect to a database (creates the database file if it doesn't exist)
conn = sqlite3.connect('C:/Users/jacqu/Desktop/Github - Jacques/RenBoss Data Scraper/DB.db')

#incase of F-ups
#conn.execute("DROP TABLE RawData")
#conn.commit()

# Create a table
conn.execute("CREATE TABLE IF NOT EXISTS RawData (id INTEGER PRIMARY KEY AUTOINCREMENT, SKU TEXT, sDesc TEXT, Price TEXT, Weight TEXT, Desc TEXT, Image Text)")

#url's goes here
url = conn.execute("SELECT * FROM urls")

for rows in url:
    #requests the page
    r = requests.get(rows[0])
    #creates an object of the page
    soup = BeautifulSoup(r.content)

    #find SKU
    sku = soup.find(class_= 'itemName').get_text()
    #print("SKU: " + sku)

    #find short title
    sDesc = soup.find(id = 'PlaceHolderMain_SrsItemDetailControl_lblItemName').get_text()
    #print("Short Desc: " + sDesc)

    #find price
    price = soup.find(id = 'PlaceHolderMain_SrsItemDetailControl_lblPrice').get_text()
    #print("Price: " + price)

    #find weight
    weight = soup.find(id = 'lblWeight').get_text()
    #print("Weight: " + weight)

    #find Description
    lDesc = soup.find(id = 'lblItemDescription').get_text()
    #print("Destription: " + lDesc)

    #find image
    imgSrc = soup.find(id = 'PlaceHolderMain_SrsItemDetailControl_rptImagesZoom_NewImgZoomhref_0')
    #print(imgSrc['href'])

    # Insert data into the table
    conn.execute("INSERT INTO RawData (SKU ,sDesc ,Price ,Weight ,Desc ,Image ) VALUES (?, ?, ?, ?, ?, ?)", (sku,sDesc,price,weight,lDesc,str(imgSrc['href'])))

    iterations = iterations + 1
    

#save your work
conn.commit()

#calc run time
endTime = time.time()
exceTime = startTime - endTime
print("Items completed: " + str(iterations))
print("Average Time per Item: " + str(exceTime / iterations))
print("Exce Time: " + str(exceTime))

# Close the connection
conn.close()