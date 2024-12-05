# import dotenv 
# import os
# import requests
# from facebook_business.adobjects.productitem import ProductItem

# dotenv.load_dotenv()

# GRAPH_API_BASE_URL = os.getenv("GRAPH_API_BASE_URL")
# ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


# # def fetch_meta_products():
# #     headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
# #     products = []
# #     url = GRAPH_API_BASE_URL + "?fields=id,retailer_product_group_id,retailer_id"
# #     while url:
# #         response = requests.get(url, headers=headers)
# #         if response.status_code == 200:
# #             data = response.json()
# #             products.extend(data["data"])
# #             url = data.get("paging", {}).get("next")  # Get the next page if it exists
# #         else:
# #             print(f"Error fetching Meta products: {response.text}")
# #             break
# #     return products

# # def find_meta_product(shopify_product_id, meta_products):
# #     for product in meta_products:
# #         if product["retailer_product_group_id"] == shopify_product_id:
# #             return product
# #     return None





import os
import requests
import dotenv
import json

dotenv.load_dotenv()

GRAPH_API_BASE_URL = os.getenv("GRAPH_API_BASE_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
BUSINESS_ID = os.getenv("BUSINESS_ID")


# def delete_product_item(product_id_list):
#     """
#     Deletes a product item from the catalog.
#     """
#     for i in product_id_list["id"]:
#         url = f"{GRAPH_API_BASE_URL}/{i}"
#         headers = {
#             "Authorization": f"Bearer {ACCESS_TOKEN}"
#         }

#         response = requests.delete(url, headers=headers)

#         if response.status_code == 200:
#             print(f"Product item {i} deleted successfully!")
        
#         else:
#             print("Error during deletion:")
#             print(f"Status Code: {response.status_code}")
#             print(response.json())

# def filter_products_by_group_id(data: dict, group_id: str) -> list:
#     """
#     Filters products in a JSON object by retailer_product_group_id.

#     :param data: JSON data containing a list of products under a key 'products'.
#     :param group_id: The retailer_product_group_id to filter by.
#     :return: A list of products that match the given retailer_product_group_id.
#     """
#     if not isinstance(data, dict) or 'products' not in data:
#         raise ValueError("Invalid JSON structure. Ensure 'products' key is present.")
    
#     return [
#         product for product in data.get('products', [])
#         if product.get('retailer_product_group_id') == group_id
#     ]


# def get_meta_products(id):

#     url = f"https://graph.facebook.com/v17.0/{BUSINESS_ID}/owned_product_catalogs"
#     fields="products{id,retailer_product_group_id,retailer_id,product_group,vendor_id,color,name,description,additional_variant_attributes,brand,availability,category}"
#     # Define the parameters for the API request
#     params = {
#         "fields": fields,
#         "access_token": ACCESS_TOKEN
#     }
#     response = requests.get(url, params=params)
#     response_json = response.json()
#     if response_json:
#         return json.loads(response_json)
    


# def fetch_meta_products():
#     """
#     Fetch all products from the Meta catalog.
#     """
#     headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
#     products = []
#     url = GRAPH_API_BASE_URL + "?fields=id,retailer_product_group_id,retailer_id"
#     while url:
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             data = response.json()
#             products.extend(data["data"])
#             url = data.get("paging", {}).get("next")  # Get the next page if it exists
#         else:
#             print(f"Error fetching Meta products: {response.text}")
#             break
#     return products


# def find_meta_products_by_group_id(group_id, meta_products):
#     """
#     Find products in Meta catalog by retailer_product_group_id.
#     """
#     return [product for product in meta_products if product["retailer_product_group_id"] == group_id]


# def delete_meta_product(product_id):
#     """
#     Delete a single product by Meta product ID.
#     """
#     url = f"{GRAPH_API_BASE_URL}/{product_id}"
#     headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
#     response = requests.delete(url, headers=headers)

#     if response.status_code == 200:
#         print(f"Product item {product_id} deleted successfully!")
#     else:
#         print(f"Error during deletion of {product_id}:")
#         print(f"Status Code: {response.status_code}")
#         print(response.json())


# def delete_products_by_shopify_group_id(shopify_product_group_id):
#     """
#     Main function to handle product deletion by Shopify product group ID.
#     """
#     # Step 1: Fetch all products from Meta
#     meta_products = fetch_meta_products()

#     # Step 2: Find products that match the retailer_product_group_id
#     matching_products = find_meta_products_by_group_id(shopify_product_group_id, meta_products)

#     if not matching_products:
#         print(f"No products found with group ID: {shopify_product_group_id}")
#         return

#     # Step 3: Delete each matching product
#     for product in matching_products:
#         delete_meta_product(product["id"])


# Example usage:
# Replace this with the retailer_product_group_id received from Shopify
# shopify_group_id = "8753580933342"
# delete_products_by_shopify_group_id(shopify_group_id)








#REFINED CODE USING CHATGPT
# def fetch_meta_products(shopify_product_group_id):
#     """
#     Fetches all products from the Meta catalog.
#     """
    
    # fields="products{id,retailer_product_group_id,retailer_id,product_group,vendor_id,color,name,description,additional_variant_attributes,brand,availability,category}"
    
    # products = []
    # # url = f"{GRAPH_API_BASE_URL}/{BUSINESS_ID}/owned_product_catalogs?fields=f{fields}"
    # url = f"{GRAPH_API_BASE_URL}/{BUSINESS_ID}/owned_product_catalogs?fields={fields}"
    

    # while url:
    #     response = requests.get(url, headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
    #     if response.status_code == 200:
    #         data = response.json()
    #         products.extend(data.get("products", []))
    #         url = data.get("paging", {}).get("next")  # Fetch the next page, if available
    #     else:
    #         print(f"Error fetching Meta products: {response.text}")
    #         break

    # return products
    # url = f"{GRAPH_API_BASE_URL}/{BUSINESS_ID}/products"
    # params = {
    #     "fields": "id,retailer_id,retailer_product_group_id,name",
    #     "access_token": ACCESS_TOKEN,
    #     "filter": f"retailer_product_group_id=='{shopify_product_group_id}'"
    # }

    # try:
    #     response = requests.get(url, params=params)
    #     response.raise_for_status()
    #     data = response.json()

    #     # Extract product items
        
    #     products = data.get("data", [])
    #     print(products)
    #     return products

    # except requests.exceptions.RequestException as e:
    #     print(f"Error fetching products: {e}")
    #     return []
    
# def fetch_all_products():
#     """
#     Fetches all products from the Meta catalog.
#     """
#     url = f"{GRAPH_API_BASE_URL}/{BUSINESS_ID}/owned_product_catalogs"
#     params = {
#         "fields": "id,retailer_id,retailer_product_group_id,name",
#         "access_token": ACCESS_TOKEN,
#     }

#     products = []
#     while url:
#         response = requests.get(url, params=params)
#         if response.status_code == 200:
#             data = response.json()
#             products.extend(data.get("data", []))
#             # url = data.get("paging", {}).get("next")  # Get the next page if available
#         else:
#             print(f"Error fetching products: {response.status_code} {response.text}")
#             break

#     return products



def delete_matching_products(products):
    """
    Deletes a list of products from the Meta catalog.
    """
    for product in products:
        url = f"{GRAPH_API_BASE_URL}/{product}"
        response = requests.delete(url, headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})

        if response.status_code == 200:
            print(f"Product {product} deleted successfully.")
        else:
            print(f"Failed to delete product {product}: {response.json()}")
            
            
def fetch_all_products():
    """
    Fetches all products from the Meta catalog using a for loop for pagination.
    """
    url = f"{GRAPH_API_BASE_URL}/{BUSINESS_ID}/owned_product_catalogs"
    params = {
        "fields": "id,retailer_id,products{retailer_product_group_id},name",
        # "fields": "id,name,products{id,retailer_product_group_id,retailer_id,product_group,vendor_id,color,name,description,additional_variant_attributes,brand,availability,category},",
        "access_token": ACCESS_TOKEN,
    }

    products = []
    response = requests.get(url, params=params)
    

    return response.json()



# def get_products_by_group_id(retailer_product_group_id):
#     """
#     Filters products based on retailer_product_group_id.

#     :param retailer_product_group_id: The group ID to filter the products.
#     :return: A list of filtered product items.
#     """
#     try:
#         all_products = fetch_all_products()  # Fetch data from the source
#         filtered_products = []
        
#         print(all_products.json())
#         #     filtered_products.extend([
#         #         {
#         #             "id": product.get("id"),
#         #             "retailer_id": product.get("retailer_id"),
#         #             "name": product.get("name"),
#         #             "description": product.get("description"),
#         #             "brand": product.get("brand"),
#         #             "availability": product.get("availability"),
#         #         }
#         #         for product in products_data
#         #         if not retailer_product_group_id or product.get("retailer_product_group_id") == retailer_product_group_id
#         #     ])

#         # return filtered_products
#     except KeyError as e:
#         print(f"KeyError while processing data: {e}")
#         return []
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return []

# def get_products_by_group_id(retailer_product_group_id):
#     """
#     Filters products based on retailer_product_group_id.

#     :param retailer_product_group_id: The group ID to filter the products.
#     :return: A list of filtered product items.
#     """
#     all_products = fetch_all_products()
#     # filtered_products = [
#     #     product for product in all_products["data"][0]["products"]["data"]
#     #     if product.get("retailer_product_group_id") == retailer_product_group_id
#     # ]
#     filtered_products = []
#     for item in all_products['data']:
#         if "products" in item:
#             products = item["products"]["data"]
#             for product in products:
#                 product_info = {
#                     "id": product["id"],
#                     "retailer_id": product["retailer_id"],
#                     "name": product["name"],
#                     "description": product["description"],
#                     "brand": product["brand"],
#                     "availability": product["availability"]
#                 }
#                 filtered_products.append(product_info)

#     print("filtered_products========================",filtered_products)
#     return filtered_products

# def get_products_by_group_id(retailer_product_group_id):
#     """
#     Filters products based on retailer_product_group_id.

#     :param retailer_product_group_id: The group ID to filter the products.
#     :return: A list of filtered product items.
#     """
#     all_products = fetch_all_products()  # Fetch data from the source
    
#     delete_ids = []
#     for product in all_products['data']:
#         if "products" in product:
#             final = product["products"]['data']
#             for fin in final:
#                 if fin["retailer_product_group_id"] == f"{retailer_product_group_id}":
#                     print(fin)
#                     delete_ids.append(fin['id'])
                    
                    
                
def get_products_by_group_id(retailer_product_group_id):
    all_products = fetch_all_products() 
    delete_ids = [
        fin['id']
        for product in all_products.get('data', [])
        if 'products' in product
        for fin in product["products"].get('data', [])
        if fin.get("retailer_product_group_id") == str(retailer_product_group_id)
    ]
    return delete_ids
            




# def find_meta_products_by_group_id(group_id, meta_products):
#     """
#     Filters products by the retailer_product_group_id.
#     """
#     product = [
#         product for product in meta_products['data']
#         if product.get("retailer_product_group_id") == int(group_id)
#     ]
    
#     print(product)


