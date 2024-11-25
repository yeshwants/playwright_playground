import time
from playwright.sync_api import sync_playwright

def search_amazon_and_get_first_link(category, subcategory, manufacturer, model_name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Navigate to Amazon
            page.goto("https://www.amazon.com")
            
            # Search for the product
            time.sleep(1)
            search_query = f"{category} {subcategory} {manufacturer} {model_name}"
            #search_box = page.get_by_placeholder("Search Amazon").click()
            search_box = page.locator("#twotabsearchtextbox")
            search_box.fill(search_query)
            search_box.press("Enter")
            #breakpoint()
            # Wait for the search results container to load
            page.locator(".s-main-slot").wait_for(timeout=10000)
            
            # Find all products links and then return first one
            all_products = page.locator(".s-main-slot .s-result-item h2 a").all()
            if all_products:
                first_link = all_products[0].get_attribute("href")
                if first_link:
                    full_link = f"https://www.amazon.com{first_link}"
                    print("First product link:", full_link)
                    return full_link
                else:
                    print("No link found for the first product.")
            else:
                print("No products found.")
        except Exception as e:
            print("An error occurred:", str(e))
            page.screenshot(path="error_screenshot.png")
            print("Screenshot saved as 'error_screenshot.png'.")
        finally:
            # Close the browser safely
            browser.close()
            #print("Browser closed.")

# Input values
category = "electronics"
subcategory = "laptop"
manufacturer = "Dell"
model_name = "XPS 13"

# Execute the function
first_link = search_amazon_and_get_first_link(category, subcategory, manufacturer, model_name)
