# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC

# # import time

# # chrome_driver_path = r"C:\Users\Nizam\Desktop\lolwaagain\chromedriver.exe"

# # service = Service(chrome_driver_path)
# # browser = webdriver.Chrome(service=service)

# # browser.get('https://livingdailyy.com/')

# # time.sleep(5)
# # #button = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'LEARN HTML')))
# # #button = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div[1]/div/h4/a')))
# # button = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/div[3]/div/div[1]/div[2]/h3/a')
# # button.click()

# # time.sleep(8)

# # browser.close()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# chrome_driver_path = r"C:\Users\Nizam\Desktop\lolwaagain\chromedriver.exe"

# service = Service(chrome_driver_path)
# browser = webdriver.Chrome(service=service)

# browser.get('https://livingdailyy.com/')

# time.sleep(5)

# # Click on the specified article link
# button = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/div[3]/div/div[1]/div[2]/h3/a')
# button = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/div[3]/div/div[1]/div[2]/h3/a')
# button.click()

# time.sleep(5)

# # Scroll down by a specified amount
# def scroll_down(pixels):
#     browser.execute_script(f"window.scrollBy(0, {pixels});")
#     time.sleep(2)  # Adjust sleep time as needed

# # Scroll up by a specified amount
# def scroll_up(pixels):
#     browser.execute_script(f"window.scrollBy(0, -{pixels});")
#     time.sleep(2)  # Adjust sleep time as needed

# # Scroll to the bottom of the page
# def scroll_to_bottom():
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)  # Adjust sleep time as needed

# # Scroll to the top of the page
# def scroll_to_top():
#     browser.execute_script("window.scrollTo(0, 0);")
#     time.sleep(2)  # Adjust sleep time as needed

# # Example usage
# scroll_down(200)
# time.sleep(2) # Scroll down 500 pixels
# scroll_down(200)
# time.sleep(2)    # Scroll down another 500 pixels
# scroll_down(200)
# time.sleep(2) # Scroll down 500 pixels
# scroll_down(200)
# time.sleep(2)    # Scroll down another 500 pixels

# scroll_up(300)     # Scroll up 300 pixels
# scroll_to_bottom() # Scroll to the bottom of the page
# scroll_to_top()    # Scroll to the top of the page

# # Spend some more time on the article page
# time.sleep(8)

# # Close the browser
# browser.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r"C:\Users\Nizam\Desktop\article_reader\chromedriver.exe"

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

browser.get('https://livingdailyy.com/')

time.sleep(5)

# List to store article XPaths
article_xpaths = [
    '//*[@id="content"]/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div[2]/h3/a',
    '//*[@id="content"]/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div[2]/h3/a',
    '//*[@id="content"]/div[1]/div/div/div[1]/div/div[2]/div/div/div[7]/div/div[2]/h3/a',
    '//*[@id="content"]/div[1]/div/div/div[1]/div/div[2]/div/div/div[8]/div/div[2]/h3/a',
    '//*[@id="content"]/div[1]/div/div/div[1]/div/div[2]/div/div/div[9]/div/div[2]/h3/a'
]

def scroll_down(pixels):
    browser.execute_script(f"window.scrollBy(0, {pixels});")
    time.sleep(2)  # Adjust sleep time as needed

# Scroll up by a specified amount
def scroll_up(pixels):
    browser.execute_script(f"window.scrollBy(0, -{pixels});")
    time.sleep(2)  # Adjust sleep time as needed

# Scroll to the bottom of the page
def scroll_to_bottom():
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust sleep time as needed

# Scroll to the top of the page
def scroll_to_top():
    browser.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)  # Adjust sleep time as needed

# # Example usage
# scroll_down(200)
# time.sleep(2) # Scroll down 500 pixels
# scroll_down(200)
# time.sleep(2)    # Scroll down another 500 pixels
# scroll_down(200)
# time.sleep(2) # Scroll down 500 pixels
# scroll_down(200)
# time.sleep(2)    # Scroll down another 500 pixels

# scroll_up(300)     # Scroll up 300 pixels
# scroll_to_bottom() # Scroll to the bottom of the page
# scroll_to_top()    # Scroll to the top of the page

# Click on each article and do some action (e.g., scroll)
i  = 1
for xpath in article_xpaths:
    button = browser.find_element(By.XPATH, xpath)
    button.click()
    print(f'Article {i} opened')
    i = i + 1
    time.sleep(5)  # Add additional waiting time for the page to load
    scroll_down(200)
    time.sleep(2) # Scroll down 500 pixels
    scroll_down(200)
    
    print("spending time on article ")
    time.sleep(2)    # Scroll down another 500 pixels
    scroll_down(200)
    time.sleep(2) # Scroll down 500 pixels
    scroll_down(200)
    time.sleep(2)    # Scroll down another 500 pixels

    scroll_up(300)     # Scroll up 300 pixels
    scroll_to_bottom() # Scroll to the bottom of the page
    scroll_to_top()    # Scroll to the top of the page

    # After performing actions, go back to the main page
    browser.back()
    time.sleep(3)  # Add additional waiting time for the page to load

# Close the browser
browser.close()
