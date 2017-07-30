from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import threading,time
import datetime
import queue
import sched
from datetime import timedelta
def lastclick(driver):
    try:
        elem=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/button')
        time.sleep(3)
        print("wait for all treads to come same point",datetime.datetime.now())
        elem.click()
        time.sleep(30)
        driver.close()
    except Exception as e:
        if driver:driver.close()
        print(e)
        
    

def timing(driver):
    s=sched.scheduler(time.time)
    print(time.time())
    s.enter(120,0,lastclick(driver))
    s.run()
    
def testcase(test_name):
    try:
        url='http://safechamp-8000.herokuapp.com/'
        driver=webdriver.Chrome()
        driver.get(url)
        
        #login ###########################
        
        profile=['dem1@g.com','12b14e20D']
        
        elem1=driver.find_element(By.XPATH,'//input[@name="email"]')
        s=driver.window_handles[0]
        elem1.send_keys(profile[0])
        elem2 = driver.find_element(By.XPATH,'//input[@type="password"]')
        elem2.send_keys(profile[1])
        driver.find_element_by_id('loginButton').click()
        time.sleep(20) # wait for login
        
        #toggle bar and click action#######################
        
        driver.find_element(By.XPATH,'/html/body/ohs-navbar/div[1]/a[1]').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/a').click()
        time.sleep(10)
        
        #click for new action##############################
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/h2/div/a').click()
        time.sleep(10)
        
        #fill the form and submit##########################
        driver.find_element(By.ID,'reportedDate').click()
        time.sleep(10)
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/table/tbody/tr[3]/td[7]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/form/div[2]/div[2]/input').send_keys(test_name)
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/form/div[3]/div[2]/input').send_keys(test_name)
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/form/div[4]/div[2]/select').click()
        time.sleep(10)
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/form/div[4]/div[2]/select/option[2]').click()
        driver.find_element(By.ID,'dueDate').click()
        time.sleep(10)
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/form/div[6]/div[2]/div/div/div/table/tbody/tr[6]/td[1]').click()
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/form/div[7]/div[2]/input').send_keys(test_name)
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/form/div[9]/div[2]/textarea').send_keys(test_name+" "+str(time.time()))
        timing(driver)
        #click submit button############################
        #print("wait for all treads to come same point")
        #time.sleep(60)
        #print(datetime.time())
        
        #driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div/div/button').click()
        #time.sleep(15)
        #driver.close()
    except Exception as e:
        print(e)
        driver.close()
def threader():
    while True:
        value=q.get() 
        result=testcase(value)
        q.task_done()
def exampling(test_list):
    global q
    q=queue.Queue()
    for x in range(30):
        t=threading.Thread(target=threader)
        #t.deamon=True
        t.start() 
    for value in test_list:
        q.put(value)
    q.join()    

def main():
    test_list=["Test "+str(i) for i in range(5)]
    print(test_list)
    exampling(test_list)
    
    
    
    
if __name__=="__main__": 
    main()
        