# Used Car Dealer Simulator

# 1. Welcome Message
print("--- Welcome to Keep'em Clean David Used Car Emporium ---")
print("Where every car is an 'Experience'! \n")

# 2. Ask for the car
car_name = input("Which car are you interested in buying? ")

# 3. Ask for the price
base_price = float(input(f"What is the base price of the {car_name}? $"))

# 4. Calculate fees
# Sleaze tax: 5% of base price
# Restocking fee: 12% of base price
sleaze_tax = base_price * 0.05
restocking_fee = base_price * 0.12
# Dummy flat fees
documentation_fee = 299.00
license_fee = 150.00

total_cost = base_price + sleaze_tax + restocking_fee + documentation_fee + license_fee

# 5. Output report with formatted prices
print("\n" + "="*30)
print(f"SALES REPORT: {car_name}")
print("="*30)
print(f"Base Price:       ${base_price:,.2f}")
print(f"Sleaze Tax (5%):  ${sleaze_tax:,.2f}")
print(f"Restocking (12%): ${restocking_fee:,.2f}")
print(f"Documentation:    ${documentation_fee:,.2f}")
print(f"License Fee:      ${license_fee:,.2f}")
print("-"*30)
print(f"Total Cost:       ${total_cost:,.2f}")
print("="*30)
print("Thank you for trusting Smooth Talk David!")
