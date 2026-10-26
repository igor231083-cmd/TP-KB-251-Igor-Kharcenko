import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

while True:
    currency = input("Enter currency (EUR, USD, PLN, q - exit): ").upper()

    if currency == "Q":
        break

    if currency not in ["EUR", "USD", "PLN"]:
        print("Wrong currency")
        continue

    amount = int(input("Enter amount: "))

    for elem in response.json():
        if elem["cc"] == currency:
            result = amount * elem["rate"]
            print("Rate:", elem["rate"])
            print("Result:", round(result, 2), "UAH")
            break
