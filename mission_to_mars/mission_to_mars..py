#!/usr/bin/env python
# coding: utf-8

# In[3]:


# importing libraries
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


# In[4]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)


# # NASA Mars News Section

# In[6]:


html = browser.html


# In[7]:


nasa_Site = bs(html, 'html.parser')
nasa_Site


# In[8]:


#do i need to use the more next function? 

nasa_title = nasa_Site.find('div', class_="content_title").get_text()

# for nasa_titles in nasa_title:
#     print("Titles:")
#     print(nasa_titles.text)

print (nasa_title)


# In[ ]:





# In[ ]:





# In[9]:


#do i need to use the more next function? 

nasa_p = nasa_Site.find('div', class_='article_teaser_body').get_text()
nasa_p

# for nasa_ps in nasa_p:
#     print("Paragraph:")
#     print(nasa_ps.text)


# In[ ]:





# In[10]:


#create loop to output beautifulthe above image


# # JPL Mars Space Images - Featured Image

# In[11]:


image_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


# In[12]:


browser.visit(image_url)
html = browser.html


# In[13]:


featured_img=bs(html, 'html.parser')
print(featured_img.prettify())


# In[14]:


featured_image_url=featured_img.find_all('li', class_= 'slide')
featured_image_url


# In[15]:


link=[]

for link in featured_img.find_all(class_='fancybox'):
    print('https://www.jpl.nasa.gov/' + link.get('data-fancybox-href'))


# # Mars Weather

# In[16]:


weather_url = "https://twitter.com/marswxreport"
response = requests.get(weather_url)


# In[17]:


#browser.visit(weather_url)
#html = browser.html


# In[18]:


weather_site=bs(response.text, 'html.parser')
print(weather_site)


# In[19]:


for weather_find in weather_site.find_all('div', class_='js-tweet-text-container'):
  
        print(weather_find)
   


# In[20]:


weather_find= weather_site.find('p', class_='tweet-text').text
print(weather_find)
        


# In[ ]:





# In[ ]:





# # Mars Facts

# In[21]:


facts_url= "https://space-facts.com/mars/"


# In[22]:


tables = pd.read_html(facts_url)[0]
tables.columns=["Description", "Value"]
tables


# In[23]:


tables.to_html()


# In[ ]:





# # Mars Hemispheres

# In[27]:


hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)


# In[28]:


hemispheres = browser.html


# In[32]:



soup = bs(hemispheres, 'html.parser')

items = soup.find_all('div', class_='item')

hemisphere_image_urls = []

main_url = 'https://astrogeology.usgs.gov'


for x in items: 
  
    title = x.find('h3').text
    
    part_img_url = x.find('a', class_='itemLink product-item')['href']
    
    browser.visit(main_url + part_img_url)
   
    part_img_html = browser.html
    
    soup =bs( part_img_html, 'html.parser')
     
    img_url = main_url + soup.find('img', class_='wide-image')['src']
    
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    

hemisphere_image_urls


# In[ ]:




