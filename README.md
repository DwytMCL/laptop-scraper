# Lazada Laptop Listing Scraper

A small Python automation project that opens Lazada Philippines in headless Firefox and exports up to five eligible laptop search listings to CSV.

Built with Selenium for browser automation and pandas for CSV output.

## What it does

- Opens the Lazada Philippines search page for `laptop`.
- Waits up to 15 seconds for product cards to appear.
- Skips cards containing `Sold Out` or `Out of Stock`, missing prices, or fields it cannot extract.
- Collects the first five eligible cards in the returned page order.
- Writes listing titles, displayed prices, links, and extraction order to `top_5_laptops.csv`.
- Closes Firefox when the run finishes or encounters an error.

`Rank` records extraction order. It does not measure product quality, value, popularity, or sales.

## Requirements

- Python 3
- Mozilla Firefox
- A compatible GeckoDriver available to Selenium
- Python packages: `selenium` and `pandas`

Install Firefox and [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for your operating system, and make the driver available on your `PATH`.

## Set up

```bash
git clone https://github.com/DwytMCL/laptop-scraper.git
cd laptop-scraper
python3 -m venv .venv
source .venv/bin/activate
python -m pip install selenium pandas
```

On Windows PowerShell, create and activate the environment with:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install selenium pandas
```

## Run

From the repository directory with the virtual environment active:

```bash
python LaptopPrices.py
```

The script prints progress and writes the CSV to the current working directory if it collects at least one listing. An existing file with that name is replaced on a successful export.

## CSV fields

| Column | Value |
| --- | --- |
| `Rank` | Sequential extraction order, starting at 1 |
| `Model` | Listing title as displayed on the page |
| `Price` | Displayed price text, without numeric conversion |
| `Link` | Product link from the listing |

## Limitations and troubleshooting

- The script reads one set of loaded search cards; it does not paginate or scroll through additional results.
- Availability checks rely on listing text. Product identity, stock, and prices are not independently verified.
- Fewer than five rows can be returned. If no valid rows are found, no CSV is written and an older CSV may remain unchanged.
- Lazada layout changes can break the product-card, title, or price selectors in `LaptopPrices.py`.
- Missing listings or a timeout can also result from network failures, access restrictions, or pages that require interaction.
- For Firefox startup errors, check the browser installation and GeckoDriver compatibility.
- Dependencies are currently unpinned, and the repository has no automated tests.

Use the script in accordance with Lazada's applicable terms and access rules.
