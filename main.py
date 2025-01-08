from src.utils import get_soap
import json
from src.models import Products,Category

def main():
    url = "https://www.adidas.co.id/graphql?hash=1081972869&_filter_0={sku:{eq:IH5712},customer_group_id:{eq:0}}"
    data = get_soap(url)
    #with open("data.json", "w") as f:
    #    json.dump(data, f)

    product = Products(
        id = data["data"]["products"]["items"][0]["id"],
        sku = data["data"]["products"]["items"][0]["sku"],
        name = data["data"]["products"]["items"][0]["name"],
        price = data["data"]["products"]["items"][0]["price_range"]["minimum_price"]["final_price"]["value"],
        release_date = data["data"]["products"]["items"][0]["custom_attributes"]["launch_date"]["value"],
        category = Category.SHOES
    )

    print(product)
    with open("product.json", "w") as f:
        product = product.model_dump()
        product["release_date"] = product["release_date"].strftime("%Y-%m-%d")
        product["category"] = product["category"].value
        json.dump(product, f)

if __name__ == "__main__":
    main()