import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Note: We removed 'Service' and 'webdriver_manager' imports 
# because we are using the system-installed geckodriver.

def scrape_laptops():
    options = webdriver.FirefoxOptions()
    
    # Run in headless mode to avoid display/GUI errors if you are in a terminal-only session
    options.add_argument("--headless") 
    
    # We do NOT set binary_location. 
    # The system geckodriver knows exactly where the system Firefox is.
    
    print("Connecting to system Firefox...")
    
    try:
        # Initialize driver without defining a service (it finds /usr/bin/geckodriver automatically)
        driver = webdriver.Firefox(options=options)
        
        url = "https://www.lazada.com.ph/catalog/?q=laptop"
        print(f"Navigating to {url}...")
        driver.get(url)

        wait = WebDriverWait(driver, 15)
        print("Waiting for products to load...")
        
        # Selectors
        product_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-qa-locator='product-item']")))

        print(f"Found {len(product_cards)} products. Extracting top 5...")

        laptop_data = []

        for index, card in enumerate(product_cards[:5]):
            try:
                title = card.find_element(By.CSS_SELECTOR, "div.RfADt > a").text
                price = card.find_element(By.CSS_SELECTOR, "span.ooOxS").text
                link = card.find_element(By.CSS_SELECTOR, "div.RfADt > a").get_attribute("href")

                laptop_data.append({
                    "Rank": index + 1,
                    "Model": title,
                    "Price": price,
                    "Link": link
                })
                print(f"Scraped #{index+1}: {title[:30]}...")

            except Exception as e:
                print(f"Error scraping item {index+1}: {e}")

        if laptop_data:
            df = pd.DataFrame(laptop_data)
            df.to_csv("top_5_laptops.csv", index=False)
            print("\nSUCCESS: Data saved to 'top_5_laptops.csv'")
            print(df)
        else:
            print("No data extracted.")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Diagnostic: If this fails, we know Firefox itself is broken
        if "binary" in str(e).lower():
            print("\nCRITICAL: Try running 'firefox --version' in your terminal.")
            print("If that fails, your Firefox installation is broken.")

    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    scrape_laptops()