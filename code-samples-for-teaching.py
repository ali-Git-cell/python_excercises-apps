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

# Example code for a short gradebook
semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
 
subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]
gradebook = [[subjects[0], grades[0]], [subjects[1], grades[2]], [subjects[2], grades[2]], [subjects[3], grades[3]]]
#print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][1] += 5 
#print(gradebook)


gradebook[2].remove(85)
gradebook[2].append("Pass")
#print(gradebook)


#####################################################

# Pizza shop example
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print("We sell {} different kinds of pizza!".format(num_pizzas))

pizza_and_prices = []

for i in range(num_pizzas):
  listopt = []
  listopt.append(prices[i])
  listopt.append(toppings[i])
  pizza_and_prices.append(listopt)
  
pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop(-1)

pizza_and_prices.insert(4, [2.5, "peppers"])
#print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
#print(three_cheapest)


#####################################################
# haicut shop price calculator
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price

#print("Total Price:", total_price)

average_price = total_price /  len(prices)
#print("Average Haircut Price:", average_price)

new_prices = [price - 5 for price in prices]
#print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
#print(total_revenue)

average_daily_revenue = total_revenue / 7
#print(average_daily_revenue)


cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if prices[i] < 30 ]
#print(cuts_under_30)

#######################################################################################

#Trip planner with python functions
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 {}".format("Johan"))


trip_planner_welcome("Rome")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(3.3)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in {}".format(origin))
  print("And you are traveling to {}".format(destination))
  print("You will be traveling by {}".format(mode_of_transport))
  print("It will take approximately {} hours".format(str(estimated_time)))

destination_setup("Delhi", "Mumbai", estimate)


#######################################################################################

# calculating fundamental physical properties with the help of pyhton functions
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)
#print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
#print(c_to_f(0))

c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return (mass * acceleration)


#######################################################################################



letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


letter_to_points = {key:val for key, val in zip(letters, points)}
letter_to_points[" "] = 0


def score_word(word):
  point_total = 0
  for let in word:
    point_total += letter_to_points.pop(let, 0)
  return point_total

brownie_points = score_word("BROWNIE")



player_to_words = {"players": ["BLUE", "TENNIS","EXit"], "wordNerd": ["BLUE", "TENNIS","EXit"], "Lexi Con": ["BLUE", "TENNIS","EXit"], "Prof Reader": ["BLUE", "TENNIS","EXit"]}

player_to_points = {}

for key, value in player_to_words.items():
  player_points = 0
  for word in value:
    player_points += score_word(word)
  print(player_points, key)
  player_to_points[key] = player_points
  #print(key, value)
print(player_to_points)

train_force = get_force(train_mass, train_acceleration)

#print("The GE train supplies {} Newtons of force.".format(train_force))

def get_energy(mass, c=3*10**8):
  return (mass * c)

bomb_energy = get_energy(bomb_mass)

#print("A 1kg bomb supplies {} Joules.".format(bomb_energy))

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

#print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))

#######################################################################################


