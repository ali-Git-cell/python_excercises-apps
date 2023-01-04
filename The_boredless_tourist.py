destinations = ["Paris, France", "Shanghai, China","Los Angeles, USA","São Paulo, Brazil","Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']  ]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#print(get_destination_index("Los Angeles, USA"))


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)


attractions = [[], [], [], [], []]
#attractions = [[] for lst in destinations ]

#print(attractions)
#attractions_for_destination = []

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)

  if destination_index:
    for lst in attractions:
      attractions_for_destination = attractions[destination_index]
      attractions_for_destination.append(attraction)
      return attractions_for_destination


#add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)
