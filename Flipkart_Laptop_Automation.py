#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
import time


# In[7]:


search_item = input("Enter Your Product:- ")


# In[8]:


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")


# In[ ]:


try:
    driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z"]').click()
except:
    pass


# In[ ]:


driver.find_elements_by_xpath('//input[@name="q"]').send_keys(search_item)
driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()


# In[ ]:


time.sleep(3)


# In[ ]:


pcontainer = driver.find_element_by_xpath('//div[@class="_1YokD2 _2GoDe3"]')
container = pcontainer.find_elements _by_xpath('//div[@class="_1YokD2 _3Mn1Gg"]')[1]


# In[ ]:


all_products = container.find_elements_by_xpath('//div[@class="_13oc-S"]')


# In[ ]:


for product in all_products:
    product.click()
    driver.switch_to.window(driver.window_handles[1])


# In[ ]:


title = driver.find_element_by_xpath('//span[@class="B_NuCI"]').text
price = driver.find_element_by_xpath('//div[@class="_30jeq3 _16Jk6d"]').text


# In[ ]:


try:
    mrp = driver.find_element_by_xpath('//div[@class="_3I9_wc _2p6lqe"]').text
    discount = driver.find_element_by_xpath('//div[@class="_3Ay6Sb _31Dcoz"]').text
    seller_name = driver.find_element_by_id("sellerName").text
except:
    pass


# In[ ]:


print(f"Title: - {title}")
print(f"Price:- {price}")
try:
    print(f"MRP: - {mrp}")
    print(f"Discount:- {discount}")
    print(f"SellerName:- {seller_name}")
except:
    pass  


# In[ ]:


driver.close()
driver.switch_to.window(driver.window_handles[0])


# In[ ]:


driver.quit()


# In[ ]:





# In[11]:


from selenium import webdriver
import time

search_item = input("Enter Your Product:- ")

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")

try:
    driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z"]').click()
except:
    pass

driver.find_elements_by_xpath('//input[@name="q"]').send_keys(search_item)
driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()

time.sleep(3)

pcontainer = driver.find_element_by_xpath('//div[@class="_1YokD2 _2GoDe3"]')
container = pcontainer.find_elements_by_xpath('//div[@class="_1YokD2 _3Mn1Gg"]')[1]

all_products = container.find_elements_by_xpath('//div[@class="_13oc-S"]')

for product in all_products:
    product.click()
    driver.switch_to.window(driver.window_handles[1])
    
title = driver.find_element_by_xpath('//span[@class="B_NuCI"]').text
price = driver.find_element_by_xpath('//div[@class="_30jeq3 _16Jk6d"]').text

try:
    mrp = driver.find_element_by_xpath('//div[@class="_3I9_wc _2p6lqe"]').text
    discount = driver.find_element_by_xpath('//div[@class="_3Ay6Sb _31Dcoz"]').text
    seller_name = driver.find_element_by_id("sellerName").text
except:
    pass

print(f"Title: - {title}")
print(f"Price:- {price}")
try:
    print(f"MRP:- {mrp}")
    print(f"Discount:- {discount}")
    print(f"SellerName:- {seller_name}")
except:
    pass  

driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.quit()


# In[ ]:




