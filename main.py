import requests
from bs4 import BeautifulSoup
import re

def scrape_5_letter_words():
    base_url = "https://www.bestwordlist.com/5letterwords"
    words = set()  

    for i in range(1, 27):
        if i == 1:
            url = f"{base_url}.htm"
        else:
            url = f"{base_url}page{i}.htm"
        
        print(f"Scraping {url}...")
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve {url}")
            continue

        soup = BeautifulSoup(response.content, "html.parser")

        page_text = soup.get_text(separator=" ")
        found_words = re.findall(r'\b[a-zA-Z]{5}\b', page_text)
        for word in found_words:
            words.add(word.lower())

    return sorted(words)

if __name__ == "__main__":
    five_letter_words = scrape_5_letter_words()
    
    with open("5_letter_words.txt", "w") as f:
        for word in five_letter_words:
            f.write(word + "\n")
    
    print(f"Scraped {len(five_letter_words)} unique 5-letter words. Saved to 5_letter_words.txt")
