	
distance = float(input("Enter distance in kilometers: "))
rate_per_kilometer = float(input("Enter rate per kilometer(₱): "))

def total_delivery_fee(distance, rate_per_kilometer):
    return distance * rate_per_kilometer
    
total_fee = total_delivery_fee(distance, rate_per_kilometer)

print(f"Total Delivery Fee: ₱{total_fee:.2f}")
