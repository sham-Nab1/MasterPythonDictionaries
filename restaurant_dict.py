# Restaurant Table
restaurant_object1 = {
    "ID": 1,
    "Name": "Vikings Luxury Buffet",
    "Location": "Pasay City",
    "Cuisine Type": "Buffet",
    "Established Year": 2011,
    "Website or Contact": "www.vikings.ph"
}

restaurant_object2 = {
    "ID": 2,
    "Name": "Antonio's Restaurant",
    "Location": "Tagaytay",
    "Cuisine Type": "Fine Dining",
    "Established Year": 2002,
    "Website or Contact": "www.antoniosrestaurant.ph"
}

restaurant_object3 = {
    "ID": 3,
    "Name": "Mesa Filipino Moderne",
    "Location": "Makati City",
    "Cuisine Type": "Filipino",
    "Established Year": 2009,
    "Website or Contact": "www.mesa.ph"
}

restaurant_object4 = {
    "ID": 4,
    "Name": "Manam Comfort Filipino",
    "Location": "Quezon City",
    "Cuisine Type": "Filipino",
    "Established Year": 2013,
    "Website or Contact": "www.manam.ph"
}

restaurant_object5 = {
    "ID": 5,
    "Name": "Ramen Nagi",
    "Location": "Various Locations",
    "Cuisine Type": "Japanese",
    "Established Year": 2013,
    "Website or Contact": "www.ramennagi.com.ph"
}

# List of restaurant objects
restaurant_objects = [restaurant_object1, restaurant_object2, restaurant_object3, restaurant_object4, restaurant_object5]

# Print restaurant details
for restaurant in restaurant_objects:
    print(f"ID: {restaurant['ID']}, Name: {restaurant['Name']}, Location: {restaurant['Location']}, Cuisine Type: {restaurant['Cuisine Type']}, Established Year: {restaurant['Established Year']}, Website or Contact: {restaurant['Website or Contact']}")
