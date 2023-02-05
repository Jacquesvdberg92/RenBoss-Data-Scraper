#install requests
#install bs4
from bs4 import BeautifulSoup
import requests
import time



#url's goes here
url = "https://fordspecialtools.service-solutions.com/en-US/Pages/ItemDetail.aspx?SKU=702%204106%20002%2000"

#requests the page
r = requests.get(url)
#creates an object of the page
soup = BeautifulSoup(r.content)

#find SKU
sku = soup.find(class_= 'itemName').get_text()
print("SKU: " + sku)

#find short title
sDesc = soup.find(id = 'PlaceHolderMain_SrsItemDetailControl_lblItemName').get_text()
print("Short Desc: " + sDesc)

#find price
price = soup.find(id = 'PlaceHolderMain_SrsItemDetailControl_lblPrice').get_text()
print("Price: " + price)

#find weight
weight = soup.find(id = 'lblWeight').get_text()
print("Weight: " + weight)

#find Description
lDesc = soup.find(id = 'lblItemDescription').get_text()
print("Destription: " + lDesc)

#find image
imgSrc = soup.find(id = 'PlaceHolderMain_SrsItemDetailControl_rptImagesZoom_NewImgZoomhref_0')
print(imgSrc['href'])