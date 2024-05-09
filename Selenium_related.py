from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pathlib import Path


def bridge( number, name):

    #open the webpage
    driver = webdriver.Edge()
    address = Path.cwd() / "test.html" 
    driver.get(address.as_uri())
    #get the IDs for the relelvent elements
    assignee = driver.find_element(By.CLASS_NAME, "select2-input")
    short_discription = driver.find_element(By.ID,"sp_formfield_u_short_description")
    long_discription = driver.find_element(By.ID,"sp_formfield_u_description")
    assignment_group = driver.find_element(By.ID,"s2id_autogen3_search")
    submit = driver.find_element(By.NAME,"submit")
    discription= f"Meetingroom Check {number} {name}"
    
    #fill the element
    assignee.send_keys("Paraic Cloherty")
    short_discription.send_keys(discription)
    long_discription.send_keys(discription)
    assignment_group.send_keys("EMEA GB Shardlondon EUC (STF)")
    submit.click()
    

    time.sleep(5)
    driver.quit()
