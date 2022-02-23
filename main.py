from selenium import webdriver
import datetime
import time

iterate_num = 0

# ------------------------------------ TIME HANDLING -------------------------------------

curr_time_min = datetime.datetime.now().minute

print(curr_time_min)

program_start_time = curr_time_min
# ------------------------------------ SITE FETCHING -------------------------------------
PATH = "chromedriver.exe"

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")


clicked_cookie = driver.find_element_by_css_selector("#bigCookie")
golden_cookie = driver.find_element_by_css_selector("#goldenCookie")
time.sleep(5)
# ------------------------------------ STRING PROCCESSING ---------------------------------


# ------------------------------------- PROGRAM -------------------------------------------
while program_start_time != program_start_time + 5:
    #--------------------------------- COOKIE NUMBER FETCHING -----------------------------
    cookie_counter = driver.find_element_by_css_selector("#cookies")
    cookie_counter_to_slice = cookie_counter.text
    cookie_splited = int(cookie_counter_to_slice.split(sep=" ", maxsplit =1 )[0].replace(",",""))
    # try:
    #     cookie_splited.replace(",","")
    # except:
    #     pass

    print(cookie_splited)
    # -------------------------------- UPGRADE COST FETCHING ------------------------------
    upgrade_1 = driver.find_element_by_css_selector("#productPrice0")
    upgrade_1_string = upgrade_1.text
    upgrade_int_cursor = int(upgrade_1_string.replace(",",""))
    upgrade_2 = driver.find_element_by_css_selector("#productPrice1")
    upgrade_2_string = upgrade_2.text   
    upgrade_int_grandmother = int(upgrade_2_string.replace(",",""))
    
    try:
        clicked_cookie.click()
    except:
        golden_cookie.click()


    try:
        if cookie_splited > 100:
            box_1_update = driver.find_element_by_xpath('//*[@id="upgrade0"]')
            box_1_update.click()
    except:
        pass
    


    try:
        upgrade_3 = driver.find_element_by_css_selector("#productPrice2")
        upgrade_3_string = upgrade_3.text
        upgrade_int_farm = int(upgrade_3_string.replace(",",""))
    except:
        pass
    else:
        if upgrade_int_cursor > upgrade_int_grandmother > upgrade_int_farm and cookie_splited > upgrade_int_farm:
            upgrade_3_click = driver.find_element_by_xpath('//*[@id="product2"]')
            upgrade_3_click.click()
    try:
        upgrade_4 = driver.find_element_by_css_selector("#productPrice3")
        upgrade_4_string = upgrade_4.text
        upgrade_int_mine = int(upgrade_4_string.replace(",",""))
    except:
        pass
    else:
        if upgrade_int_cursor > upgrade_int_grandmother > upgrade_int_farm > upgrade_int_mine and cookie_splited > upgrade_int_mine:
            upgrade_4_click = driver.find_element_by_xpath('//*[@id="product2"]')
            upgrade_4_click.click()
    try:
        upgrade_5 = driver.find_element_by_css_selector("#productPrice4")
        upgrade_5_string = upgrade_5.text
        upgrade_int_5 = int(upgrade_5_string.replace(",",""))
    except:
        pass
    else:
        if upgrade_int_cursor > upgrade_int_grandmother > upgrade_int_farm > upgrade_int_mine > upgrade_int_5 and cookie_splited > upgrade_int_5:
            upgrade_5_click = driver.find_element_by_xpath('//*[@id="product2"]')
            upgrade_5_click.click()
    try:
        upgrade_6 = driver.find_element_by_css_selector("#productPrice5")
        upgrade_6_string = upgrade_6.text
        upgrade_int_6 = int(upgrade_6_string.replace(",",""))
    except:
        pass
    else:       
        if upgrade_int_cursor > upgrade_int_grandmother > upgrade_int_farm > upgrade_int_mine > upgrade_int_5 > upgrade_int_6 and cookie_splited > upgrade_int_6:
            upgrade_5_click = driver.find_element_by_xpath('//*[@id="product2"]')
            upgrade_5_click.click()
   

    if upgrade_int_cursor > upgrade_int_grandmother and  cookie_splited > upgrade_int_grandmother:
        upgrade_2_click = driver.find_element_by_xpath('//*[@id="product1"]')
        upgrade_2_click.click()

    if cookie_splited > upgrade_int_cursor and iterate_num % 10000:
        upgrade_1_click = driver.find_element_by_xpath('//*[@id="product0"]')
        upgrade_1_click.click()

    iterate_num =+ 1

