from selenium import webdriver
import time
import openpyxl

search_item = input("Enter Your Product:- ")

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")

try:
    driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z"]').click()
except:
    pass

driver.find_element_by_xpath('//input[@name="q"]').send_keys(search_item)
driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()


time.sleep(3)

pcontainer = driver.find_element_by_xpath('//div[@class="_1YokD2 _2GoDe3"]')
container = pcontainer.find_elements_by_xpath('//div[@class="_2kHMtA"]')[1]


all_products = container.find_elements_by_xpath('//div[@class="_13oc-S"]')

for product in all_products:
    product.click()
    driver.switch_to.window(driver.window_handles[1])

    try:
        title = driver.find_element_by_xpath('//span[@class="B_NuCI"]').text
        price = driver.find_element_by_xpath('//div[@class="_30jeq3 _16Jk6d"]').text
    except:
        pass

    try:
        mrp = driver.find_element_by_xpath('//div[@class="_3I9_wc _2p6lqe"]').text
        discount = driver.find_element_by_xpath('//div[@class="_3Ay6Sb _31Dcoz"]').text
        seller_name = driver.find_element_by_id("sellerName").text
    except:
        pass

    print(f"Title: - {title}")
    print(f"Price:- {price}")
    try:
        print(f"MRP: - {mrp}")
        print(f"Discount:- {discount}")
        print(f"SellerName:- {seller_name}")
    except:
        pass  

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
driver.quit()

