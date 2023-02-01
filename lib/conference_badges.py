def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    room_number = 1
    result = []
    for name in names:
        result.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
        room_number += 1
    return result

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
