stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print("Stock not found.")

print("\nPortfolio Summary")
print("-----------------")

with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-----------------\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total += value
        print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")
        file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}\n")

    print("Total Investment Value = $", total)
    file.write(f"\nTotal Investment Value = ${total}")