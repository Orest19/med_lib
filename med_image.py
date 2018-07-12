from time import sleep
from selenium import webdriver
import re
import httplib2

def dload_book (log_name, passw_name, url_book,folder):
    # Start Chrome, get start page
    browser = webdriver.Chrome()
    browser.get('http://www.medcollegelib.ru/cur_user/entry.html')

    # Enter into account
    user = browser.find_element_by_id('new_UName')
    passw = browser.find_element_by_id('new_PWord')
    user.send_keys(log_name)
    passw.send_keys(passw_name)
    form = browser.find_element_by_id('try_UNamePWord')
    form.click()

    # Get book page
    browser.get(url_book)
    sleep(3) # Time in seconds.
    read = browser.find_element_by_id('a-to_first_chapter')
    read.click()
    fin = browser.find_element_by_class_name('arrow-to-finish').find_element_by_tag_name("a")
    h2   = fin.get_property("href")

    nxt = browser.find_elements_by_class_name('arrow-right-tab')
    i = 0

    # Download image
    while True:
        try:
            sleep(3) # Time in seconds.
            i+=1
            page = browser.find_element_by_id('cur_page_content')
            nxt = browser.find_elements_by_class_name('arrow-right-tab')
            hm = page.get_attribute('innerHTML')
            res = re.findall("url..(.*jpg)",hm)
            im = res[0]
            h = httplib2.Http('.cache')
            response, content = h.request(im)

            # Choose place
            out = open(folder + '/img_%.3d.jpg' % i, 'wb')
            out.write(content)
            out.close()
            nxt[0].click()
        except:
    # Exit
            browser.quit()

log = "X093_"
passw = "KYHCEYQT"
link =  "http://www.medcollegelib.ru/book/ISBN9785970419458.html"
fol_name = "Pharm"
dload_book (log,passw,link,fol_name)
browser.quit()
break











