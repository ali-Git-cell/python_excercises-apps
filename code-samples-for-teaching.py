import random

name = "John"
question = "Is the weather cold outside?"
answer = ""

random_number = random.randint(1, 9)

#print(random_number)
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

  
print(name,"asks:", question)
print("Magic 8-Ball's answer:", answer)



#####################################################

#shipping costs calculator

weight = 4.8

# Ground Shipping
cost_ground = 0
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight < 6:
  cost_ground = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20
  
#print("ground Shipping: ", cost_ground)


# Premium Shipping
cost_premium = 125.00
#print("premium Shipping:", cost_premium)


# Drone Shipping
cost_drone = 0
if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight < 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.0
else:
  cost_drone = weight * 14.25

#print("Drone Shipping:", cost_drone)

#####################################################
