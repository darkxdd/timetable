
schedule = {
    'Faculty 1': {
        'Monday': {
            '9:00 AM - 10:00 AM': 'Subject A',
            '10:00 AM - 11:00 AM': 'Subject B',
            '11:00 AM - 12:00 PM': 'Subject C',
        },
        'Tuesday': {
            '9:00 AM - 10:00 AM': 'Subject D',
            '10:00 AM - 11:00 AM': 'Subject E',
            '11:00 AM - 12:00 PM': 'Subject F',
        },
    },
    'Faculty 2': {
        'Monday': {
            '9:00 AM - 10:00 AM': 'Subject X',
            '10:00 AM - 11:00 AM': 'Subject Y',
            '11:00 AM - 12:00 PM': 'Subject Z',
        },
        'Tuesday': {
            '9:00 AM - 10:00 AM': 'Subject P',
            '10:00 AM - 11:00 AM': 'Subject Q',
            '11:00 AM - 12:00 PM': 'Subject R',
        },
    },
}


print("Faculty\t\tDay\t\tTime\t\tSubject")
for faculty, faculty_schedule in schedule.items():
    for day, day_schedule in faculty_schedule.items():
        for time, subject in day_schedule.items():
            print(f"{faculty}\t{day}\t{time}\t{subject}")