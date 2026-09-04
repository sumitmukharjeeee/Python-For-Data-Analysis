# # import requests

# # url = 'https://www.ibm.com/'
# # r = requests.get(url)

# # print(r)
# # print(r.status_code)
# # print(r.headers)
# # print(r.request.body)
# # print(r.encoding)

# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.facebook.com/'

# # Sending https requests

# response = requests.get(url)

# # storing the html content in a variable

# html_content = response.text

# #  to parse using beautiful soap

# soup = BeautifulSoup(html_content,'html.parser')

# # display content

# # print(soup.prettify())

# # display a snippet

# print(html_content[:500])

# # finding all the a tags

# links = soup.find_all('a')

# for link in links:
#     print(link.text)

# scrapy is an open source web crawling framework for python
# it is used to extract the data fromm website

# selenium is tool used for controlling web browser through programs and automating browser taks

# from selenium import webdriver
# driver = webdriver.firefox()
# driver.get("https://www.facebook.com/")