import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_laptops():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless") 

    print("Connecting to system Firefox...")
    try:
        driver = webdriver.Firefox(options=options)
        
        url = "https://www.lazada.com.ph/catalog/?q=laptop"
        print(f"Navigating to {url}...")
        driver.get(url)

        wait = WebDriverWait(driver, 15)
        print("Waiting for products to load...")
        
        # Get ALL product cards first (we might need to check more than 5 to find 5 valid ones)
        product_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-qa-locator='product-item']")))

        print(f"Found {len(product_cards)} total products. Filtering valid listings...")

        laptop_data = []
        
        # Loop through products until we have 5 valid ones or run out of items
        for card in product_cards:
            if len(laptop_data) >= 5:
                break

            try:
                # FILTERING LOGIC
                if "Sold Out" in card.text or "Out of Stock" in card.text:
                    print("Skipping sold out item...")
                    continue

                # Extract Data
                title_element = card.find_element(By.CSS_SELECTOR, "div.RfADt > a")
                title = title_element.text
                
                # Double check: Sometimes price is missing if unlisted
                try:
                    price = card.find_element(By.CSS_SELECTOR, "span.ooOxS").text
                except:
                    print("Skipping item with no price (likely unlisted)...")
                    continue

                link = title_element.get_attribute("href")

                laptop_data.append({
                    "Rank": len(laptop_data) + 1,
                    "Model": title,
                    "Price": price,
                    "Link": link
                })
                print(f"Scraped #{len(laptop_data)}: {title[:30]}...")

            except Exception as e:
                continue

        # Save to Spreadsheet
        if laptop_data:
            df = pd.DataFrame(laptop_data)
            df.to_csv("top_5_laptops.csv", index=False)
            print("\nSUCCESS: Data saved to 'top_5_laptops.csv'")
            print(df)
        else:
            print("No valid data extracted.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    scrape_laptops()