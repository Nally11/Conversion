import requests

def convert_usd_to_gbp(amount):
    base_url = "http://data.fixer.io/api/latest"
    access_key = "d7bd455444c7f747bd569d2c59426a19"  
    params = {
        "access_key": access_key,
        "symbols": "GBP",
        "base": "USD"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        gbp_rate = data["rates"]["GBP"]
        gbp_amount = amount * gbp_rate
        return gbp_amount
    else:
        print("Failed to fetch data from Fixer.io")
        return None

# Test the function
usd_amount = 100
gbp_equivalent = convert_usd_to_gbp(usd_amount)


#if gbp_equivalent is not None:
 #   print(f"{usd_amount} USD is equal to {gbp_equivalent:.2f} GBP")


response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)  # Print the entire response JSON
    gbp_rate = data.get("rates", {}).get("GBP")
    if gbp_rate is not None:
        gbp_amount = amount * gbp_rate
        return gbp_amount
    else:
       print("GBP rate not found in response")
       return None
    #else:
   #     print("Failed to fetch data from Fixer.io")
     #   return None