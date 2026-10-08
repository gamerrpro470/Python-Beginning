hotel_name = "Sunrise Hotel" 
tax_percent = 10 
room_rates = {"single": 4000, "double": 6500, "suite": 12000} 

bookings = {
             201: {"guest": " zain abbas ", "room": "double", "nights": 3}, 
             202: {"guest": "NIDA FATIMA", "room": "single", "nights": 1}, 
             203: {"guest": "omar sheikh ", "room": "suite", "nights": 2}, 
             204: {"guest": "areeba noor", "room": "single", "nights": 5} 
             }

# question 1

print(f"===== SUNRISE HOTEL =====")
print(f"single room rate : {room_rates["single"]} PKR")
print(f"total bookings : 4\n")

# question 2

def clean_name(guest):
    return guest.strip().title()

# question 2

def calculate_room_cost(room, nights):
    return room_rates[room] * nights

# question 4

def get_discount(nights):
    if nights >= 5:
        return 15
    elif nights >= 3:
        return 10
    else:
        return 0

# question 5

def find_booking(booking_id):
    booking = bookings.get(booking_id)
    if booking is None:
        return "Booking Not Found"
    return f"{booking["guest"]} - Rs. {booking["total"]}"

# question 6

total_collection = 0
total_nights = 0
vip_count = 0

for booking_id in bookings:
    record = bookings[booking_id]
    name = clean_name(record["guest"])
    room = record["room"]
    nights = record["nights"]

    # question 7
    room_cost = calculate_room_cost(room, nights)
    discount_percent = get_discount(nights)
    discount_amount = room_cost * discount_percent // 100
    after_discount = room_cost- discount_amount
    tax = after_discount * tax_percent // 100
    total = after_discount + tax

    # question 8
    if room == "suite" and nights >= 2:
        guest_type = "VIP Guest"
        vip_count += 1 
    else:
        guest_type = "Regular Guest"

    # question 9
    record["guest"] = name
    record["total"] = total
    total_collection += total
    total_nights += nights

    # question 10
    print(f"Booking ID: {booking_id}")
    print(f"Guest: {name}")
    print(f"Room: {room} | Nights: {nights}")
    print(f"Room Cost: Rs. {room_cost}")
    print(f"Discount: {discount_percent}% (Rs. {discount_amount})")
    print(f"Tax ({tax_percent}%): Rs. {tax}")
    print(f"Total: Rs. {total}")
    print(f"Guest Type: {guest_type}\n")

# question 11
print("===== SUMMARY =====")
print(f"Total Nights Booked: {total_nights}")
print(f"VIP Guests: {vip_count}")
print(f"Total Collection: Rs. {total_collection}")

# question 12
print("\n===== SEARCH =====")
print("203 ->", find_booking(203))
print("999 ->", find_booking(999))



