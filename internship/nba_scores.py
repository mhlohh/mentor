from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

while True:
    try:
        data = get(BASE_URL + ALL_JSON).json()
        printer.pprint(response)
    except ConnectionRefusedError:
        break


