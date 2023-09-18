from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from csv import writer
import time

# opening drivers and url
url = "https://www.nike.com/"
driver = Service("E:\learning\python\webscrapping\chromedriver.exe")
browser = webdriver.Chrome(service=driver)
browser.get(url)
browser.maximize_window()

#title of the web 
my_title = browser.title
print(my_title)


# searching the product you want 
search = browser.find_element(By.NAME,"search")
search.send_keys("Jackets")
search.send_keys(Keys.ENTER)
#html page source 
html_content = browser.page_source
soup = BeautifulSoup(html_content , "html.parser")


# detail of products 
products = soup.find_all("div", class_= "product-card")


file_name = input("Enter Your File Name : ")


with open(f'{file_name}.csv', 'w', encoding='utf8', newline='')as f:
    thewriter = writer(f)
    feild_names= ['NAME', 'PRICE', "URL"]
    thewriter.writerow(feild_names)
    for product in products:    
        # name / title of the product 
        
        name = product.find("div", class_= "product-card__title").text.strip()
        
        # extract the product price
        price = product.find("div", class_="product-price").text.strip()
        # image url 

        product_image_url = product.find("img", class_="product-card__hero-image")["src"]

    
        #printing detail in console 
        print("Name : ", name)
        print("Price : ", price)
        print("Url : ", product_image_url)
        print("\n")
        info = [name, price, product_image_url]
        thewriter.writerow(info)
    
#shutting down after given time interval 
time.sleep(10)