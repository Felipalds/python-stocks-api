import requests
import sys
from app import menu

print("Hello world!")
print(__name__)
if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        menu()
    elif sys.argv[1] == "-s":
        print("Fetching stocks")
        stock_symbol =sys.argv[2]
        api = requests.get(f"https://brapi.dev/api/quote/{stock_symbol}").json()
        print(api["results"][0]["symbol"], api["results"][0]["regularMarketPrice"])
    elif sys.argv[1] == "-b":
        print()