# Advanced Web Scraper

This Python-based Advanced Web Scraper application allows users to scrape data from web pages using specified HTML tags, classes, links, and images. It features pagination support and the ability to filter scraped data.

## Features

- Scrape data based on HTML tags, classes, links, and images.
- Support for pagination to scrape multiple pages.
- Apply filters to refine the scraped data.
- Save scraped data to a CSV file.

## Requirements

- Python 3.x
- `tkinter` (for GUI)
- `requests` (for HTTP requests)
- `beautifulsoup4` (for parsing HTML)
- `lxml` (for better parsing performance)
- `csv` (for saving data to CSV files)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/advanced-web-scraper.git
    cd advanced-web-scraper
    ```

2. Install the required Python packages:
    ```sh
    pip install requests beautifulsoup4 lxml
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Use the GUI to input the URL and specify the HTML tags, classes, and whether to scrape links or images. Optionally, provide filters, start page, and end page numbers.

3. Click the "Scrape" button to start the scraping process.

4. Save the scraped data to a CSV file when prompted.

## Fields

- **URL:** The target web page URL.
- **HTML Tags:** Comma-separated list of HTML tags to scrape.
- **HTML Classes:** Comma-separated list of HTML classes to scrape.
- **Scrape Links:** Check to scrape all links on the page.
- **Scrape Images:** Check to scrape all images on the page.
- **Filters:** Optional comma-separated filters to refine the scraped data.
- **Start Page:** The starting page number for pagination.
- **End Page:** The ending page number for pagination.

