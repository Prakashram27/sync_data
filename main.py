import json

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import json

from services import delete_matching_products, get_products_by_group_id
from sync import process_and_update_shopify_products


app = FastAPI()


# Shopify Webhook handler route
@app.post("/product_delete")
async def shopify_webhook(request: Request):
    try:
        body = await request.body()
        # print(body)
        decoded_data = body.decode("utf-8")

        data = json.loads(decoded_data)
        shopify_product_group_id = int(data.get("id"))

        print(shopify_product_group_id)

        # products = get_meta_products(id_value)
        # filtered_products = filter_products_by_group_id(products,id_value)
        # delete_product_item(filtered_products)

        # REFINED COED BY CHATGPT
        meta_products = get_products_by_group_id(shopify_product_group_id)
        delete_matching_products(meta_products)


        # print(meta_products['data'])
        # print("1111111111111111111111")
        # matching_products = find_meta_products_by_group_id(shopify_product_group_id, meta_products)
        # print("222222222222222222222222222")

        # if not matching_products:
        #     return {"message": f"No products found for group ID {shopify_product_group_id}."}
        # print("000000000000000000000000000000000")

        # delete_matching_products(matching_products)
        # print("33333333333333333333333333333")
        # return {"message": f"Deleted {len(matching_products)} products for group ID {shopify_product_group_id}."}
        return None

    except Exception as e:
        print(f"Error processing webhook: {str(e)}")
        return {"error": "Failed to process the webhook."}

    print(id_value)
    # delete_product_item(id_value)
    # delete_products_by_shopify_group_id(id_value)
    return {"message": "Webhook received successfully"}


@app.get("/sync")
async def product_sync():
    process_and_update_shopify_products()

    return {"message": "Successfully synced"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

