# a dictionary to
total_fruits_sold = {"apples": 88,
					"bananas": 56,
					"oranges": 72,
					"pears": 77}

# add a new key: grapes
total_fruits_sold["grapes"] = 10
print(total_fruits_sold)

# sort items from highest to lowest sales
ordered_sales = sorted(total_fruits_sold.items(), key=lambda x: x[1], reverse=True)
print(ordered_sales)
print("")

# checking if the keys apple and plums exist already
if "apples" in total_fruits_sold:
	print("'apples' is a key")
else:
	print("'apples' is not a key")
if "plums" in total_fruits_sold:
	print("'plums' is a key\n")
else:
	print("'plums' is not a key\n")

# looping through a dictionary to find the values abouve 70
for key in total_fruits_sold:
	if total_fruits_sold[key] > 70:
		print(key + " sold: " + str(total_fruits_sold[key]))
print("")

# list of dictionaries of different item sales
total_veg_sold = {"lettuce": 42,
				  "cucumbers": 29,
				  "carrots": 61,
				  "onions": 90}

item_sales = [total_fruits_sold, total_veg_sold]
print(item_sales)
print("")

# output summary of data in list
sum = 0
count = 0
MAX = item_sales[0]["apples"]
MIN = item_sales[0]["apples"]

for item in item_sales:
	for key in item:
		count += 1
		sum += item[key]
		MAX = max(MAX, item[key])
		MIN = min(MIN, item[key])

print("Total items sold: " + str(sum))
print("Average number of items sold: ", end="")
print(round(sum / count, 2))
print("Highest number of items sold: " + str(MAX))
print("Lowest number of itemss sold: " + str(MIN))