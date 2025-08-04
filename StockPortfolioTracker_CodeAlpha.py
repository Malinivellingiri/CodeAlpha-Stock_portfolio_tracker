# Stock Portfolio Tracker - CodeAlpha Task 2
print("Welcome to the Stock Portfolio Tracker!")
print("Enter your stock names and quantities.")
print("Type 'done' when you are finished.\n")
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "INFY": 1600
}
portfolio = {}
total_investment = 0
while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Please try again.\n")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print(" Quantity should be positive.\n")
            continue
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += stock_prices[stock] * quantity
    print(f"Added {quantity} shares of {stock}.\n")
# Display result
print("\nPortfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    print(f"{stock}: {quantity} shares × ₹{price} = ₹{value}")
print(f"\nTotal Investment Value: ₹{total_investment}")