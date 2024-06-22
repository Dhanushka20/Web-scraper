import tkinter as tk
from tkinter import messagebox, filedialog
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import os

# Function to save the scraped data to a CSV file
def save_to_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Data"])
        for item in data:
            writer.writerow([item])

# Function to scrape the web page
# Function to scrape the web page
def scrape():
    url = url_entry.get()  # Get the URL from the input field
    tags = tags_entry.get()  # Get the HTML tags to scrape from the input field
    classes = classes_entry.get()  # Get the HTML classes to scrape from the input field
    links = links_var.get()  # Get whether to scrape links
    images = images_var.get()  # Get whether to scrape images
    filters = filters_entry.get()  # Get the filters from the input field (optional)
    start_page = int(start_page_entry.get())  # Get the start page number
    end_page = int(end_page_entry.get())  # Get the end page number
    
    if not url or not (tags or classes or links or images):
        messagebox.showerror("Error", "URL and at least one of Tags, Classes, Links, or Images fields are required!")
        return
    
    try:
        current_page = 1
        while url and current_page <= end_page:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            
            soup = BeautifulSoup(response.content, 'html.parser')
            filters_list = filters.split(',') if filters else []  # Split filters into a list if provided
            
            if current_page >= start_page:
                scraped_data = []
                
                # Extract data from the title element
                title_element = soup.find('title')
                if title_element:
                    scraped_data.append(title_element.text.strip())
                
                if tags:
                    tags_list = tags.split(',')
                    for tag in tags_list:
                        for element in soup.find_all(tag.strip()):  # Find all specified tags
                            if filters_list:
                                for filter in filters_list:
                                    if filter.strip() in element.text:  # Apply filters if specified
                                        scraped_data.append(element.text.strip())
                            else:
                                scraped_data.append(element.text.strip())
                
                if classes:
                    classes_list = classes.split(',')
                    for cls in classes_list:
                        for element in soup.find_all(class_=cls.strip()):  # Find all specified classes
                            if filters_list:
                                for filter in filters_list:
                                    if filter.strip() in element.text:  # Apply filters if specified
                                        scraped_data.append(element.text.strip())
                            else:
                                scraped_data.append(element.text.strip())
                
                if links:
                    for link in soup.find_all('a', href=True):
                        scraped_data.append(link['href'].strip())
                
                if images:
                    for img in soup.find_all('img', src=True):
                        scraped_data.append(img['src'].strip())
            
                if scraped_data:
                    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
                    if file_path:
                        save_to_csv(scraped_data, file_path)
                        messagebox.showinfo("Success", "Data saved successfully!")
            
            # Check for pagination: find the link to the next page
            next_page = soup.find('li', class_='next')
            if next_page:
                next_link = next_page.find('a')['href']
                url = urljoin(response.url, next_link)
                current_page += 1
            else:
                url = None  # No more pages

    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve URL: {e}")
        return


# Setting up the Tkinter GUI
root = tk.Tk()
root.title("Advanced Web Scraper")

# URL input
tk.Label(root, text="URL:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# HTML tags to scrape input
tk.Label(root, text="HTML Tags (comma separated):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
tags_entry = tk.Entry(root, width=50)
tags_entry.grid(row=1, column=1, padx=5, pady=5)

# HTML classes to scrape input
tk.Label(root, text="HTML Classes (comma separated):").grid(row=2, column=0, padx=5, pady=5, sticky='e')
classes_entry = tk.Entry(root, width=50)
classes_entry.grid(row=2, column=1, padx=5, pady=5)

# Checkbuttons for links and images
links_var = tk.BooleanVar()
images_var = tk.BooleanVar()
tk.Checkbutton(root, text="Scrape Links", variable=links_var).grid(row=3, column=0, padx=5, pady=5, sticky='w')
tk.Checkbutton(root, text="Scrape Images", variable=images_var).grid(row=3, column=1, padx=5, pady=5, sticky='w')

# Filters input
tk.Label(root, text="Filters (optional, comma separated):").grid(row=4, column=0, padx=5, pady=5, sticky='e')
filters_entry = tk.Entry(root, width=50)
filters_entry.grid(row=4, column=1, padx=5, pady=5)

# Start page input
tk.Label(root, text="Start Page:").grid(row=5, column=0, padx=5, pady=5, sticky='e')
start_page_entry = tk.Entry(root, width=50)
start_page_entry.grid(row=5, column=1, padx=5, pady=5)

# End page input
tk.Label(root, text="End Page:").grid(row=6, column=0, padx=5, pady=5, sticky='e')
end_page_entry = tk.Entry(root, width=50)
end_page_entry.grid(row=6, column=1, padx=5, pady=5)

# Scrape button
scrape_button = tk.Button(root, text="Scrape", command=scrape)
scrape_button.grid(row=7, column=1, padx=5, pady=5, sticky='e')

root.mainloop()

