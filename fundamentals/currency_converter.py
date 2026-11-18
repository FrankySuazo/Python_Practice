# Ask the user to enter an amount in US dollars.
# Convert the input from a string to a float.
usd = float(input("Enter amount in USD: "))

# Define example exchange rates for different currencies.
# These are fixed practice rates, not live exchange rates.
eur_rate = 0.92
gbp_rate = 0.79
jpy_rate = 150.00

# Convert USD into each currency by multiplying
# the dollar amount by its corresponding exchange rate.
eur = usd * eur_rate
gbp = usd * gbp_rate
jpy = usd * jpy_rate

# Display the original amount in US dollars.
print(f"USD: ${usd:.2f}")

# Display the converted amounts.
# :.2f formats each result to two decimal places.
print(f"EUR: €{eur:.2f}")
print(f"GBP: £{gbp:.2f}")
print(f"JPY: ¥{jpy:.2f}")

