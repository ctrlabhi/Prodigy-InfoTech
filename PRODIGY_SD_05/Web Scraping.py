import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_products(target_url):
    """Scrapes product information from the given URL and stores it in a CSV file."""
    try:
        # Fetch the product listing page
        response = requests.get(target_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = BeautifulSoup(response.content, "html.parser")

        # Identify product listing elements (replace with website-specific selectors)
        product_listings = soup.find_all("div", class_="product-card")  # Adjust selector

        # Extract product details
        products = []
        for product_element in product_listings:
            product_name = product_element.find("div", class_="product-name").text.strip()  # Adjust selectors
            product_price = product_element.find("p", class_="discount-price").text.strip()  # Adjust selectors
            product_rating = product_element.find("div", class_="product-rating").get("data-rating")  # Adjust selectors
            product_image = product_element.find("img", class_="fy__img image").get("src")   # Adjust selectors

            products.append({
                "Name": product_name,
                "Price": product_price,
                "Rating": product_rating,
                "Image":product_image
            })

        # Create and save the CSV file
        df = pd.DataFrame(products)
        df.to_csv("products.csv", index=False)  # Adjust filename

        print("Product information scraped and saved to products.csv")

    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching the website: {e}")

    except AttributeError as e:
        print(f"Error: The website structure might have changed. Attribute not found: {e}")


if __name__ == "__main__":
    # Replace with the actual URL of the product listing page you want to scrape
    target_url = "https://www.tirabeauty.com/collection/fragrance-mens-fragrance-perfumes-edt-and-edp"

    scrape_products(target_url)
