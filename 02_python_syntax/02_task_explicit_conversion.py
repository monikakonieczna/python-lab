#Calculate how much each person needs to pay for a room
hotel_room_price = 100
tax = hotel_room_price * 0.08
total = hotel_room_price + tax
room_guests = 4
share_per_person = total/room_guests

print("Each person needs to pay: " + str(share_per_person)) # change a data type