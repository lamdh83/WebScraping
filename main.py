# Import libraries and packages for the project

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import csv
from pynput.keyboard import Key, Controller
keyboard = Controller()
key = "c"

print('- Finish importing package')


# Task 1: Login to Linkedin

# Task 1.1: Open Chrome and Access Linkedin login site
driver = webdriver.Chrome()
url = 'https://www.netflix.com/vn-en/login'
driver.get(url)
sleep(2)
print('- Finish initializing a driver')


# Task 1.2: Import username and password
user = open('user.txt')
line = user.readlines()
username = line[0]
password = line[1]
print('- Finish importing the login credentials')
sleep(2)

#dinh vi email theo id id_userLoginId
email_field = driver.find_element_by_id('id_userLoginId')
#nhap dia chi email
email_field.send_keys(username)
sleep(3)

#dinh vi password theo name password
password_field = driver.find_element_by_name('password')
password_field.send_keys(password)
print('- Finish keying in password')
sleep(2)

#dinh vi nut sign in bang xpath
login_field = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
login_field.click()
sleep(3)



# Task 3: Scrape the URLs of the profiles
# page_source = BeautifulSoup(driver.page_source)
# profiles = page_source.find_all('ul', class_='choose-profile')
# print(profiles)

# dinh vi prfile theo xpath //*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div

profile_adult = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div')
profile_adult.click()
sleep(3)


# Task 2: Search for the profile we want to crawl

# Task 2.1: Locate the search bar element
search_field = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button/span')
search_field.click()
sleep(2)

# keyboard.press(key)

#
# # Task 2.2: Input the search query to the search bar
# # search_query = input('What profile do you want to scrape? ')
#
# # dinh vi bang class name searchInput
# search_input = driver.find_element_by_class_name('searchInput')
# search_query = 'phim gia dinh'
# search_input.send_keys(search_query)

# Task 2.3: Search <=> nhan nut enter
# search_field.send_keys(Keys.RETURN)

#dung pagesoure lay danh sach tieu de luu vao file csv

page_source = BeautifulSoup(driver.page_source)
profiles = page_source.find_all('a', class_='rowTitle ltr-0')
print(profiles)

# Task 3: Scrape the URLs of the profiles

# Task 3.1: Write a function to extract the URLs of one page
def GetURL():
    with open('output.csv', 'w', newline='', encoding="utf-8") as file_output:
        headers = ['Name',  'URL']
        writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n', fieldnames=headers)
        writer.writeheader()
        page_source = BeautifulSoup(driver.page_source)
        profiles = page_source.find_all('a', class_='rowTitle ltr-0')
        all_profile_URL = []
        for profile in profiles:
            profile_ID = profile.get('href')
            name = profile.find('div').get_text()
            profile_URL = "https://www.netflix.com" + profile_ID
            print(f'{name}/{profile_URL}')
            if profile_URL not in all_profile_URL:
                all_profile_URL.append(profile_URL)
                writer.writerow({headers[0]: name,  headers[1]: profile_URL})

        return all_profile_URL


# Task 3.2: Navigate through many page, and extract the profile URLs of each page
#
# input_page = int(input('How many pages you want to scrape: '))
# URLs_all_page = []
# for page in range(input_page):
#     URLs_one_page = GetURL()
#     sleep(2)
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #scroll to the end of the page
#     sleep(3)
#     next_button = driver.find_element_by_class_name("artdeco-pagination__button--next")
#     driver.execute_script("arguments[0].click();", next_button)
#     URLs_all_page = URLs_all_page + URLs_one_page
#     sleep(2)
#
# print('- Finish Task 3: Scrape the URLs')



# Task 4: Scrape the data of 1 Linkedin profile, and write the data to a .CSV file
GetURL()
#

# Task 4: Scrape the data of 1 Linkedin profile, and write the data to a .CSV file

# with open('output.csv', 'w',  newline = '') as file_output:
#     headers = ['Name', 'Job Title', 'Location', 'URL']
#     writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n',fieldnames=headers)
#     writer.writeheader()
#     for linkedin_URL in URLs_all_page:
#         driver.get(linkedin_URL)
#         print('- Accessing profile: ', linkedin_URL)
#
#         page_source = BeautifulSoup(driver.page_source, "html.parser")
#
#         info_div = page_source.find('div',{'class':'flex-1 mr5'})
#         info_loc = info_div.find_all('ul')
#         name = info_loc[0].find('li').get_text().strip() #Remove unnecessary characters
#         print('--- Profile name is: ', name)
#         location = info_loc[1].find('li').get_text().strip() #Remove unnecessary characters
#         print('--- Profile location is: ', location)
#         title = info_div.find('h2').get_text().strip()
#         print('--- Profile title is: ', title)
#         writer.writerow({headers[0]:name, headers[1]:location, headers[2]:title, headers[3]:linkedin_URL})
#         print('\n')
#
# print('Mission Completed!')

