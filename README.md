# Lazada Laptop Price Scraper

A Python automation script that scrapes the top 5 laptop listings from Lazada Philippines and exports the data (Model, Price, Rank, Link) into a CSV spreadsheet.

Built with **Selenium** and **Pandas**.

## Features

- **Automated Browsing:** Simulates a real user to bypass basic bot protections.
- **Headless Mode:** Runs in the background (no visible browser window) for speed.
- **Data Export:** Automatically saves results to `top_5_laptops.csv`.
- **Robust Selectors:** Uses specific CSS selectors to target product cards dynamically.

## Prerequisites

### 1. Python Libraries

You need Python installed. Install the required libraries using pip:

```bash
pip install selenium pandas
```

### 2. System Dependencies (Firefox & Geckodriver)

This script requires **Mozilla Firefox** and the **GeckoDriver**.

#### On Arch Linux (Recommended)

Arch Linux handles the driver best via the system package manager:

```bash
sudo pacman -S firefox geckodriver

```

#### On Windows / macOS

1. Install Firefox.
2. Download the [GeckoDriver](https://github.com/mozilla/geckodriver/releases).
3. Add it to your system PATH (or use `webdriver-manager` in Python).

## Usage

1. Clone this repository (or download the script).
2. Open your terminal in the project folder.
3. Run the script:

```bash
python LaptopPrices.py

```

### Expected Output

The console will show the scraping progress:

```text
Connecting to system Firefox...
Navigating to [https://www.lazada.com.ph/catalog/?q=laptop](https://www.lazada.com.ph/catalog/?q=laptop)...
Found 40 products. Extracting top 5...
Scraped #1: ASUS Vivobook 16...
Scraped #2: Lenovo ThinkPad...
...
SUCCESS: Data saved to 'top_5_laptops.csv'

```

A file named `top_5_laptops.csv` will appear in your folder.

## Troubleshooting

**Error: `binary is not a Firefox executable**`
This usually happens on Linux distributions like Arch or Ubuntu Snap installs.

- **Fix:** Ensure you installed the system driver (`sudo pacman -S geckodriver`) and are **not** setting a manual `binary_location` in the script unless necessary.

**Error: `Element not found**`
Lazada frequently updates their website layout. If the script fails to find products, the **CSS Selectors** in the code (`div.RfADt`, `span.ooOxS`) may need to be updated to match the new site structure.

## Disclaimer

This script is for **educational purposes only**. Scraping data from websites should be done responsibly and in accordance with the website's `robots.txt` file and Terms of Service. Avoid aggressive scraping that may overload servers.

### **How to add this to your project:**
1.  Create a new file in your folder called `README.md`.
2.  Paste the text above into it.
3.  Save the file.
4.  Run these commands to push it to GitHub:
    ```bash
    git add README.md
    git commit -m "Added documentation"
    git push
    ```

