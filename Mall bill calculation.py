# Initialize an empty list to store the bill amounts for each floor
floor_bills = []

# Get the number of floors
num_floors = int(input("Enter the number of floors: "))

# Collect bill amounts for each floor
for i in range(num_floors):
    bill = float(input(f"Enter the bill amount for floor {i + 1}: "))
    floor_bills.append(bill)

# Calculate the grand total
grand_total = sum(floor_bills)

# Determine and apply the discount
if grand_total > 50000:
    discount = grand_total * 0.20
    grand_total -= discount
    print(f"A 20% discount of {discount} has been applied.")
elif grand_total > 10000:
    discount = grand_total * 0.10
    grand_total -= discount
    print(f"A 10% discount of {discount} has been applied.")
else:
    discount = 0
    print("No discount applied.")

# Print the bill for each floor
for i in range(num_floors):
    print(f"Bill for floor {i + 1}: {floor_bills[i]}")

# Print the grand total after discount
print(f"Grand total after discount: {grand_total}")

# Check if the grand total qualifies for a gift voucher
if grand_total > 5000:
    print("Congratulations! You qualify for a gift voucher.")
else:
    print("No gift voucher.")

