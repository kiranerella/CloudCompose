import requests
import requests_cache
requests_cache.install_cache('cloudpricing_cache', expire_after=86400)

def get_aws_price(service_type):
    # sample - needs to be updated for service dynamically
    url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/index.json"
    data = requests.get(url).json()
    # cost estimation logic
    for sku, product in data["products"].items():
        if service_type in product["productFamily"]:
            terms = list(data["terms"]["OnDemand"].values())[0]
            price_dimensions = list(terms.values())[0]["priceDimensions"]
            price = list(price_dimensions.values())[0]["pricePerUnit"]["USD"]
            return float(price)
    return 0.0

def get_azure_price(meter_name):
    url = "https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Azure Database for PostgreSQL'"
    data = requests.get(url).json()
    for item in data["Items"]:
        if meter_name.lower() in item["meterName"].lower():
            return float(item["retailPrice"])
    return 0.0

def get_gcp_price(sku_description):
    url = "https://cloudbilling.googleapis.com/v1/services/{service_id}/skus"
    # Needs to enable GCP authentication
    return 0.0  
