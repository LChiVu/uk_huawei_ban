import os
from bs4 import BeautifulSoup
import csv

# set directory 
directory = '/Users/linhchivu02/Desktop/da401/data/ChinaRawHTML'  

# Open the output CSV file outside of the loop to write the headers and contents just once
with open("extracted_data.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Date Published", "Publisher", "Author", "Content Type", "Body Text"])  # Column headers

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".html"):  # Check if the file is an HTML file
            file_path = os.path.join(directory, filename)  # Get the full path of the file
            
            # Open and read the HTML file
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, "lxml")
                
                # Extract the necessary information
                title = soup.find("title").text.strip()
                date_published = soup.find("span", class_="pub_time").text.strip() if soup.find("span", class_="pub_time") else "Not found"
                author = soup.find("span", class_="byline").text.strip() if soup.find("span", class_="byline") else "Not found"
                publisher_meta = soup.find("meta", id="MetaAuthor")
                publisher = publisher_meta["content"] if publisher_meta else "Unknown"
                content_type_meta = soup.find("meta", id="channel_name")
                if content_type_meta and "OPINION" in content_type_meta["content"].upper():
                    content_type = "Opinion"
                else:
                    content_type = "News"
                
                # Adjust extraction for body text with <br/> tags
                article_content_div = soup.find("div", class_="article_content")
                if article_content_div:
                    # Extract text nodes directly, considering <br/> as separators
                    body_text = ''.join(article_content_div.stripped_strings)
                else:
                    body_text = "Not found"
                
                # Write the extracted information for each file
                writer.writerow([title, date_published, publisher, author, content_type, body_text])
        else:
            continue  # Skip non-HTML files

print("Data extraction and writing to CSV complete.")


