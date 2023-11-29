def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    batch_badges = [f'Hello, my name is {name}.' for name in names]
    return batch_badges

def assign_rooms(names):
    roomDist = [f"Hello, {name}! You'll be assigned to room {names.index(name) +1}!" for name in names]
    return roomDist

def printer(names):
    badge_names = batch_badge_creator(names)
    rooms_assigned = assign_rooms(names)
    responses = [*badge_names, *rooms_assigned]
    for response in responses:
        print(response)
