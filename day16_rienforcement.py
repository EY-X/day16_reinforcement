my_dict = {
    'data': { 
        'rooms': [ 
            { 'id': 1, 'room_number': "201", 'capacity': 50}, 
            { 'id': 2, 'room_number': "301", 'capacity': 200 }, 
            { 'id': 3, 'room_number': "1B", 'capacity': 100} 
        ],
        'events': [
            { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
            { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
            { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
            { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
            { 'id': 5, 'room_id': 2, 'start_time': 18, 'end_time': 21, 'attendees': 420 },
        ]
  }
}

DB = my_dict['data']

rooms = DB["rooms"]
events = DB["events"]

# # EXERCISE 1
# # Retrieve the capacity of room 201 and store it in a variable.

# all_rooms = rooms # Get all rooms
# room = search(all_rooms, "room_number", "201") # Find specific room
# capacity = room["capacity"] # Get it's capacity

# print("Room:", room)
# # print("Capacity:", capacity)

# def search(list, key, value):
#     for item in list:
#         if item[key] == value:
#             return item


# capacity = rooms[0]['capacity']
# print("Capacity", capacity)

def get_room(room_number):
    for room in rooms:
        if room["room_number"] == room_number:
            return room


# capacity = get_room("1B")["capacity"]


# EXERCISE 2
# Find all the events taking place in room 201.

def validate_room_fits(room_id):
    room = get_room(room_id)

    for event in events:
        if event['room_id'] == room["id"]:
            if event["attendees"] < room["capacity"]:
                print("Ok", event)
            else:
                print("Room too small", event)


validate_room_fits("301")

# Iterate through them and print "ok" if the number of planned attendees will fit in the room.




