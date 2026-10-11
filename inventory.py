inventory = {"Laptop": {"price": 1200.00, "quantity": 15}, "Mouse": {"price": 25.00, "quantity": 3}, "Keyboard": {"price": 45.00, "quantity": 8}, "Monitor": {"price": 300.00, "quantity": 2}, "HDMI Cable": {"price": 12.50, "quantity": 20}}

def check_low_stock(threshold):
  print("Items with stock below " + str(threshold) + ":")
  found_low_stock = False
  for item_name, details in inventory.items():
    if details["quantity"] < threshold:
      print(item_name + ": Only " + str(details["quantity"]) + " left in stock. ($" + "{:.2f}".format(details["price"]) + ")")
      found_low_stock = True
  if not found_low_stock:
    print("All items are sufficiently stocked.")

check_low_stock(5)