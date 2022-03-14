# Goal:
# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

# 3 options for shipping packages

# 1. Ground Shipping: which is a small flat charge plus a rate based on the weight of your package. 
# 2. Ground Shipping Premium: which is a much higher flat charge, but you aren’t charged for weight. 
# 3. Drone Shipping: which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

weight = 41.5 # Weight of package
cost_ground = int # Cost of basic ground shipping
premium_cost_ground = 125 # Cost of premium ground shipping
cost_drone = int

# Ground Shipping
# Checks for weight then prints cost of shipping that package of that weight

if weight <= 2:
  cost_ground = weight * 1.5 + 20
  print(cost_ground)
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
  print(cost_ground)
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
  print(cost_ground)
else:
  cost_ground = weight * 4.75 + 20
  print(cost_ground)

# Drone Shipping

if weight <= 2:
  cost_drone = weight * 4.5
  print(cost_drone)
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.0
  print(cost_drone)
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
  print(cost_drone)
else:
  cost_drone = weight * 14.25
  print(cost_drone)

# Additional Questions/Solutions

# Question: What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
# Answer: Ground Shipping | $34.40

# Question: What is the cheapest method of shipping a 41.5 pound package and how much would it cost?
# Answer: Premium Ground Shipping | $125.00
