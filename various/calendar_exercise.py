def hour_to_int(hour: str):
    return int(hour.replace(':',''))

def int_to_hour(integer: int):
    return str(integer)

def time_intersection(times: list, other_times: list):
    return [
        max(times[0], other_times[0]),
        min(times[1], other_times[1])
    ]

person1 = {
    'meetings': [
        ['9:00', '10:30'],
        ['12:00', '13:00'],
        ['16:00', '18:00'],
    ],
    'shift': ['9:00', '20:00']
}

person2 = {
    'meetings': [
        ['10:00', '11:30'],
        ['12:30', '14:30'],
        ['14:30', '15:00'],
        ['16:00', '17:00'],
    ],
    'shift': ['10:00', '18:30']
}

meeting_time = 30

person1['meetings'] = list(map(lambda m: list(map(lambda t: hour_to_int(t), m)), person1.get('meetings')))
person1['shift'] = list(map(lambda t: hour_to_int(t), person1['shift']))
person2['meetings'] = list(map(lambda m: list(map(lambda t: hour_to_int(t), m)), person2.get('meetings')))
person2['shift'] = list(map(lambda t: hour_to_int(t), person2['shift']))


print()
print('meetings as integers')
print(person1.get('meetings'))
print(person2.get('meetings'))

shift_overlap = time_intersection(person1.get('shift'), person2.get('shift'))

person1_free_blocks = 



print()
print('shift overlap')
print(shift_overlap)
