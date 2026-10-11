flight_route = [("New Orleans", "Chicago"), ("Chicago", "Des Moines"),
                ("Des Moines", "Denver"), ("Denver", "Los Angeles"),
                ("Los Angeles", "Phoenix"), ("Pheonix", "Austin"),
                ("Austin", "Atlanta"), ("Atlanta", "Miami"),
                ("Miami", "New York"), ("New York", "Nashville"),
                ("Nashville", "New Orleans")]

def print_itinerary(route_list):
  print("Flight itinerary:")
  for item in route_list:
    departure_city, arrival_city = item
    print("  " + departure_city + " to " + arrival_city)

print_itinerary(flight_route)