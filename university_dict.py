# University Table
university_object1 = {
    "ID": 1,
    "Name": "University of the Philippines",
    "Location": "Quezon City",
    "Established Year": 1908,
    "Type": "Public",
    "Website": "www.up.edu.ph"
}

university_object2 = {
    "ID": 2,
    "Name": "Ateneo de Manila University",
    "Location": "Quezon City",
    "Established Year": 1859,
    "Type": "Private",
    "Website": "www.ateneo.edu"
}

university_object3 = {
    "ID": 3,
    "Name": "De La Salle University",
    "Location": "Manila",
    "Established Year": 1911,
    "Type": "Private",
    "Website": "www.dlsu.edu.ph"
}

university_object4 = {
    "ID": 4,
    "Name": "University of Santo Tomas",
    "Location": "Manila",
    "Established Year": 1611,
    "Type": "Private",
    "Website": "www.ust.edu.ph"
}

university_object5 = {
    "ID": 5,
    "Name": "Polytechnic University of the Philippines",
    "Location": "Manila",
    "Established Year": 1904,
    "Type": "Public",
    "Website": "www.pup.edu.ph"
}

# List of university objects
university_objects = [university_object1, university_object2, university_object3, university_object4, university_object5]

# Print university details
for university in university_objects:
    print(f"ID: {university['ID']}, Name: {university['Name']}, Location: {university['Location']}, Established Year: {university['Established Year']}, Type: {university['Type']}, Website: {university['Website']}")
