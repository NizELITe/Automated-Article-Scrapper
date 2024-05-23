from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# # Set up proxy (example with a hypothetical proxy IP)
# proxy_ip = "your_residential_proxy:port"
# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = proxy_ip
# proxy.ssl_proxy = proxy_ip
# chrome_options.proxy = proxy

# Path to your ChromeDriver
chrome_driver_path = r"C:\Users\Nizam\Desktop\lolwaagain\chromedriver.exe"

# Initialize the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define a function to read articles
def read_articles(driver, num_articles):
    for i in range(num_articles):
        # Navigate to the article
       # article_links = driver.find_elements(By.CSS_SELECTOR, '.nr-post-title a')
        article_links = driver.find_elements(By.CSS_SELECTOR, "#content a[href*='/category/']")
       # article_links = driver.find_elements_by_css_selector("#content a[href*='/category/']")
        
        if i < len(article_links):
            article_link = article_links[i]
            article_link.click()
            
            # Simulate reading the article by scrolling slowly
            last_height = driver.execute_script("return document.body.scrollHeight")
            start_time = time.time()
            while time.time() - start_time < 120:  # 2 minutes
                driver.execute_script("window.scrollBy(0, window.innerHeight/5);")
                time.sleep(2)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                
            driver.back()
        else:
            print(f"Less than {num_articles} articles available.")
            break

# Define a function to interact with advertisements
def interact_with_advertisement(driver):
    try:
        # Find and click on an advertisement
        ad = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".advertisement-selector"))
        )
        ad.click()
        
        # Simulate reading the advertisement for at least 8 minutes
        start_time = time.time()
        while time.time() - start_time < 480:  # 8 minutes
            driver.execute_script("window.scrollBy(0, window.innerHeight/5);")
            time.sleep(2)
    except Exception as e:
        print("No advertisement found or error in clicking ad:", e)

# Main function
def main():
    driver.get("https://livingdailyy.com/")
    time.sleep(5)
    
    # Read 5 articles
    read_articles(driver, 5)
    
    # Interact with an advertisement
    interact_with_advertisement(driver)
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
