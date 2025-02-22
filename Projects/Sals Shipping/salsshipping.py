weight = 1.5
premium = 125

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 +20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight *4.75 + 20

#Drone Shipping 

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Ground Shipping $" + str(cost_ground))
print("Ground Shpping Premium $" + str(premium ))
print("Drone Shipping $" + str(cost_drone))


#test