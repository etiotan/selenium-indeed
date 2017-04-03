from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''
enters the page
'''
driver = webdriver.Firefox()
driver.get("https://www.indeed.ca/jobs?q=Web+Developer&sort=date&l=Toronto%2C+ON&radius=15")





'''
gets all the jobs for the page & total number of jobs on page
'''

all_jobs = driver.find_elements_by_class_name('turnstileLink')
for values in all_jobs:
    print (values.get_attribute("title"))
print(len(all_jobs))

#clicks first element
all_jobs[0].click()

print ("------------------preparing to switch to new window------------------")
time.sleep(3)

# switches to new window & closes page
driver.switch_to_window(driver.window_handles[-1])
print(driver.title)
button = driver.find_element_by_class_name('indeed-apply-button-label')
button.click()

print ("------------------filling in forms------------------")
time.sleep(3)
#swap to modal
driver.switch_to.frame

input_name = driver.find_element_by_id('applicant.name')
input_name.send_keys('Ricky Tan')

input_email = driver.find_element_by_id('applicant.email')
input_email.send_keys('Rickytan@gmail.com')

input_phoneNumber = driver.find_element_by_id('applicant.phoneNumber')
input_phoneNumber.send_keys('4169671111')


print("------------------preparing to switch to original window------------------")
time.sleep(3)

driver.close()
driver.switch_to_window(driver.window_handles[0])
print(driver.title)
