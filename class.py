import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


UTORID = ''
PASSWORD = ''

COURSE_CODE = ''

loginPageCheck = False
loginCheck = False
coursePageCheck = False
courseCheck = False

def loginPage(driver):

    global loginPageCheck

    URL = 'http://www.rosi.utoronto.ca/'
    LoginButton_Xpath = '/html/body/div[2]/div/div[4]/div/div[1]/div[3]/p[2]/a'

    driver.get(URL)

    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, LoginButton_Xpath))).click()

    loginPageCheck = True

    return driver

def login(driver):

    global UTORID, PASSWORD, loginCheck

    utorid_xpath = '//*[@id="inputID"]'
    password_xpath = '//*[@id="inputPassword"]'
    submit_xpath = '//*[@id="query"]/button'

    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, utorid_xpath))).send_keys(UTORID)
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, password_xpath))).send_keys(PASSWORD)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, submit_xpath))).click()

    loginCheck = True

    return driver

def goToCoursePage(driver):

    global coursePageCheck

    courseButton_xpath = '//*[@id="main-content"]/div[2]/div[1]/div/div/div[4]/div/div[1]/div[3]/a'

    WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, courseButton_xpath))).click()

    coursePageCheck = True

    return driver

def searchCourse(driver):

    courseXpath = '//*[@id="addToEnrolmentCart"]'
    inputBox_xpath = '//*[@id="typeaheadInput"]'

    global courseCheck, COURSE_CODE

    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, inputBox_xpath))).send_keys(COURSE_CODE)
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, courseXpath))).click()

    courseCheck = True

    return driver

if __name__ == '__main__':

    driver = webdriver.Chrome('./chromedriver')

    try:
        while(loginPageCheck != True):
            loginPage(driver)
        while(loginCheck != True):
            login(driver)
        while(coursePageCheck != True):
            goToCoursePage(driver)
        while(courseCheck != True):
            searchCourse(driver)
    except:
        pass

