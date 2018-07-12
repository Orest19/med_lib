from time import sleep
from selenium import webdriver
import re
import httplib2

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32gui
from pynput.keyboard import Key, Controller
keyboard = Controller()
browser = webdriver.Chrome()

def dload_book (log_name, passw_name, url_book,file):

    #Open browser  and sign in
    browser.get('http://www.medcollegelib.ru/cur_user/entry.html')
    user = browser.find_element_by_id('new_UName')
    passw = browser.find_element_by_id('new_PWord')
    user.send_keys(log_name)
    passw.send_keys(passw_name)
    form = browser.find_element_by_id('try_UNamePWord')
    form.click()
    browser.get(url_book)
    sleep(5) # Time in seconds.
    read = browser.find_element_by_id('a-to_first_chapter')
    read.click()
    sleep(2) # Time in seconds.
    appname = file_name #"Фарма.docx - Word (Сбой активации продукта)"
    window = win32gui.FindWindow(None, appname)

    while True:
        try:
            # Find borders
            st = browser.find_element_by_class_name('wrap-book-mode')
            end_bro = browser.find_element_by_id("mm4-doc-nav-pgs-bottom")
            ActionChains(browser).move_to_element(st).perform()
            ActionChains(browser).move_by_offset(-30,35).perform()
            ActionChains(browser).double_click().perform()
            sleep(2) # Time in seconds.
            ActionChains(browser).key_down(Keys.SHIFT).perform()
            ActionChains(browser).move_to_element_with_offset(end_bro,650,-20).perform()
            ActionChains(browser).click().perform()
            ActionChains(browser).key_up(Keys.SHIFT).perform()

            # Copy text
            ActionChains(browser).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
            win32gui.ShowWindow(window, 4)
            win32gui.SetForegroundWindow(window)

            # Paste
            keyboard.press(Key.ctrl.value) #this would be for your key combination
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release(Key.ctrl.value) #this would be for your key combination

            # Go back to Chrome
            sleep(2)
            toplist, winlist = [], []
            def enum_cb(hwnd, results):
                winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
            win32gui.EnumWindows(enum_cb, toplist)

            #print (winlist)
            #print (len(notepad))

            notepad = [(hwnd, title) for hwnd, title in winlist if 'chrome' in title.lower()]
            notepad= notepad[0]
            hwnd = notepad[0]

            #print (win32gui.GetWindowText(hwnd))
            #print(hwnd)
            win32gui.ShowWindow(hwnd, 4)
            win32gui.SetForegroundWindow(hwnd)
            nxt = browser.find_elements_by_class_name('arrow-right-tab')
            ro =  nxt[0].find_element_by_tag_name("a").get_property("href")
            browser.get(ro)
        except:
            browser.quit()
            break

log = "X093_"
passw = "KYHCEYQT"
link =  'http://www.medcollegelib.ru/book/ISBN9785970435854.html'
file_name = "ISBN9785970435854.docx - LibreOffice Writer"
dload_book (log,passw,link,file_name)
browser.quit()











