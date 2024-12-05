import math
import re
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import os


GRAPH_API_BASE_URL = os.getenv("GRAPH_API_BASE_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
CATALOG_ID = os.getenv("CATALOG_ID")
META_BATCH_API_URL = f"https://graph.facebook.com/v21.0/{CATALOG_ID}/batch"
API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
SHOP_NAME = os.getenv("SHOP_NAME")


def clean_html_content(html_content):
    """
    Clean HTML content and return plain text.
    """
    if not html_content or not isinstance(html_content, str):
        return "No Product Description available"

    # Remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator=" ").strip()

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text if text else "No Product Description available"


def fetch_shopify_products():
    url = f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/2024-01/products.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["products"]
    else:
        print(f"Failed to fetch Shopify products. Status code: {response.status_code}")
        # print("Response:", response.text)
        return []


def transform_to_facebook_schema(shopify_products):
    transformed_products = []
    for product in shopify_products:
        for variant in product.get("variants", []):
            description = product.get("body_html")
            clean_description = clean_html_content(description)
            data = {
                    "retailer_id": int(variant["id"]),
                    "method": "CREATE",
                    "data": {
                        "name": product["title"],
                        "description": clean_description,
                        "availability": (
                            "in stock"
                            if variant.get("inventory_quantity", 0) > 0
                            else "out of stock"
                        ),
                        "condition": "new",
                        "price": (
                            int(float(variant["price"]) * 100)
                            if variant.get("price")
                            else 0
                        ),
                        "currency": "INR",
                        "brand": product.get("vendor", "Unknown Brand"),
                        "image_url": product.get("images", [{}])[0].get("src", "http://example.com"),
                        "url": f"https://{SHOP_NAME}.myshopify.com/products",
                        "visibility": "published",
                        "retailer_product_group_id": variant.get("product_id",0),
                        "status":"active"
                }
            }
            
            print("data=========================",data)
            transformed_products.append(
                {
                    "id": int(variant["id"]),
                    "retailer_id": int(variant["id"]),
                    "method": "CREATE",
                    "data": {
                        "name": product["title"],
                        "description": clean_description,
                        "availability": (
                            "in stock"
                            if variant.get("inventory_quantity", 0) > 0
                            else "out of stock"
                        ),
                        "condition": "new",
                        "price": (
                            int(float(variant["price"]) * 100)
                            if variant.get("price")
                            else 0
                        ),
                        "currency": "INR",
                        "brand": product.get("vendor", "Unknown Brand"),
                        "image_url": product.get("images", [{}])[0].get("src", "http://example.com"),
                        "url": f"https://{SHOP_NAME}.myshopify.com/products",
                        "visibility": "published",
                        "retailer_product_group_id": variant.get("product_id", 0),
                        # "status":"active"
                        # "color": variant.get("color"," ")
                    },
                    "color": variant.get("color",""),
                    
                }
            )

    print("Length of Transformed Products", len(transformed_products))
    return transformed_products


def send_meta_batch_request(meta_products):
    """
    Send a batch request to Meta API for updating products.
    """
    response = requests.post(
        META_BATCH_API_URL,
        headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
        json={"requests": meta_products},
    )
    print("response",response.json())
    return response.json()


def process_and_update_shopify_products():
    """
    Convert Shopify data to Meta format and update products using the Batch API.
    """
    shopify_products = fetch_shopify_products()
    transformed_products = transform_to_facebook_schema(shopify_products)

    response = send_meta_batch_request(transformed_products)
    print("Completed")
    return response




