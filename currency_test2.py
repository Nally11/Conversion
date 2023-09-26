import requests

def convert_usd_to_gbp(amount, api_key):
    base_url = "https://api.apilayer.com/exchangerates_data/latest"

    params = {
        "base": "USD",
        "symbols": "GBP",
        "apikey": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        gbp_rate = data.get("rates", {}).get("GBP")
        if gbp_rate is not None:
            gbp_amount = amount * gbp_rate
            return gbp_amount
        else:
            print("GBP rate not found in response")
            return None
    else:
        print("Failed to fetch data from ExchangeRatesAPI")
        return None

# Test the function.
usd_amount = 100
exchangerates_api_key = "9f8f5ea0efff453eb2ad44941febd314"

gbp_equivalent = convert_usd_to_gbp(usd_amount, exchangerates_api_key)

if gbp_equivalent is not None:
    print(f"{usd_amount} USD is equal to {gbp_equivalent:.2f} GBP")
