# creating initial list of paintings
paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
# creating list of painting dates
dates = [1939, 1933, 1946, 1940]
# combining painting title list with dates list
paintings = list(zip(paintings, dates))
# adding three more paintings and dates to running painting list
paintings.append(("The Broken Column", 1944))
paintings.append(("The Wounded Deer", 1946))
paintings.append(("Me and My Doll", 1937))
# printing list to confirm appends - remove once confirmed
print(paintings)
# printing length of paintings list to get an item count for new id number list - remove once confirmed
print(len(paintings))
# create list of id numbers for audio tour stops for each painting
audio_tour_number = list(range(1, 8))
# zip audio tour number list to paintings list with names and dates
master_list = list(zip(audio_tour_number, paintings))
# print combined list to console
print(master_list)
