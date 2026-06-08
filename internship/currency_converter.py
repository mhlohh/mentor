from requests import get
from pprint import PrettyPrinter

API_KEY = "fca_live_LNSB71rcR4NOr5WYefXMiTvLHXZTKiVUWngMAMov"
BASE_URL = "https://api.freecurrencyapi.com/"

currency_List = []

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    data = data["data"]
    currency_List = list(data)
    return data,currency_List

currencies,currency_List =  get_currencies()

try:
    while True:
        isConvert = input("\nDo you want to convert currency(y/n): ")
        print()
        if isConvert =='n':
            break
        print("-----Currencies Options:----")
        for i,key in enumerate(currency_List):
            print(f" {key}: [{i}]")
        
        
        option1 = int(input("Enter the option 1: "))
        print(f"\n----You choose {currency_List[option1]}----\n")
        option2 = int(input("Enter the option 2: ")) 
        print(f"\n----You choose {currency_List[option2]}----\n")
        
        
        value1 = currencies[currency_List[option1]]
        value2 = currencies[currency_List[option2]]
        
        value = int(input(f"Enter the value in {currency_List[option1]}: "))
        
        Rate = value2/value1
        print(f"{currency_List[option1]} -> {currency_List[option2]} = {(value * Rate):.2f} {currency_List[option2]}")
        
        
        
except ValueError:
    print("Invalid Input!")