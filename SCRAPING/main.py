from bs4 import BeautifulSoup
import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    # options.add_argument("--headless")   # Uncomment to run headless
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_restaurants(max_pages, output_csv_path):
    base_url = "https://www.yellowpages.com/los-angeles-ca/restaurants"
    driver = get_driver()
    results = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Processing page {page}: {url}")
        driver.get(url)
        time.sleep(random.uniform(3, 5))  # wait for page to load
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        listings = soup.find_all("div", class_="result")
        if not listings:
            print("No more listings found, breaking.")
            break
        
        for l in listings:
            # 1. Name
            name_tag = l.find("a", class_="business-name")
            name = name_tag.get_text(strip=True) if name_tag else ""
            
            # 2. Categories
            categories_tag = l.find("div", class_="categories")
            if categories_tag:
                raw = categories_tag.get_text(separator=", ", strip=True)
                categories = ", ".join([c.strip() for c in raw.split(",") if c.strip()])
            else:
                categories = ""
            
            # 3. YP Rating from classes of <div class="result-rating ...">
            yp_rating = ""
            rating_div = l.find("div", class_="result-rating")
            if rating_div:
                classes = rating_div.get("class", [])
                # Map textual number to float
                def textual_to_num(text):
                    mapping = {
                        "one": 1.0,
                        "two": 2.0,
                        "three": 3.0,
                        "four": 4.0,
                        "five": 5.0,
                        "zero": 0.0
                    }
                    return mapping.get(text, None)
                
                base_num = None
                for word in ["five", "four", "three", "two", "one", "zero"]:
                    if word in classes:
                        base_num = textual_to_num(word)
                        break
                if base_num is not None:
                    if "half" in classes:
                        yp_rating = base_num + 0.5
                    else:
                        yp_rating = base_num
                else:
                    yp_rating = ""
            else:
                yp_rating = ""
            
                   
            # 4. Contact number
            phone = ""
            phone_tag = l.find("div", class_="phones phone primary")
            if phone_tag:
                phone = phone_tag.get_text(strip=True)
            
            # 5. Open status
            open_status = ""
            hours_tag = l.find("div", class_="open-status")
            if hours_tag:
                open_status = hours_tag.get_text(strip=True)
            else:
                hours_span = l.find("span", class_="open")
                if hours_span:
                    open_status = hours_span.get_text(strip=True)
                else:
                    open_status = "Hours not listed"
            
            results.append({
                "Name": name,
                "Categories": categories,
                "YP_Rating": yp_rating,
                "Phone": phone,
                "Open_Status": open_status
            })
        
        # Small pause
        time.sleep(random.uniform(2,4))
    
    driver.quit()
    
    # Write to CSV
    keys = ["Name", "Categories", "YP_Rating", "Phone", "Open_Status"]
    with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    
    print(f"Scraped {len(results)} restaurants. Data saved to {output_csv_path}")
    return results


if __name__ == "__main__":
    scrape_restaurants(max_pages=1, output_csv_path="la_restaurants.csv")
