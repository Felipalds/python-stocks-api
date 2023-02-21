from dotenv import load_dotenv
import requests
import os
import json

f = open("data.json")
data = json.load(f)

colors = {
    "green" : "\x1b[1;30;42m",
    "brazil": "\x1b[1;32;42m",
    "blue": "\x1b[0;30;44m",
    "end" : "\x1b[0m"
}

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def menu():
    print("=== Pystocks ===\n")
    if(data['brazil']):
        print(f"{colors['brazil']} Brazil Stocks {colors['end']}")
        b3 = data['brazil']
        print("TICKET \t\t AVERAGE \t\t CURRENT \t\t EARNS")
        for stock in b3:
            averagePrice = calculateAverage(stock["history"])
            currentPrice = getCurrentPrice(stock['ticket'])
            print(f"{colors['blue']}{stock['ticket'].upper()}{colors['end']} \t\t R${averagePrice:.2f} \t\t R${currentPrice}")

    print("Press [B] to buy a new stock amount\n")
    choice = input().strip().capitalize()
    
    match choice:
        case "V":
            #visualize()
            pass
        case "B":
            buy()

def buy():
    stock = input("Type the ticket you are buying (Ex: GGBR4):").strip().capitalize()
    amount = int(input(f"How much {stock} are you buying? "))


def calculateAverage(history):
    sum = 0
    price = 0
    for buy in history:
        price += buy["price"] * buy["amount"]
        sum += buy["amount"]
    return (price / sum)

def getCurrentPrice(ticket):
    data = requests.get(f"{BASE_URL}/{ticket}").json()
    return data["results"][0]["regularMarketPrice"]

f.close()