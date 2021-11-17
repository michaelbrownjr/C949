class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_minutes(self, minutes_to_add):
        self.minutes += minutes_to_add

    def add_hours(self, hours_to_add):
        self.hours += hours_to_add
    
    def minus_minutes(self, minutes_to_minus):
        self.minutes -= minutes_to_minus
    
    def minus_hours(self, hours_to_minus):
        self.hours -= hours_to_minus

    def __str__(self):
        return('The time is %d:%d' % (self.hours,self.minutes))

my_time = Time(7, 15)
print(my_time)

print('What do you want to do?')
user_input = int(input('1. Add minutes\n2. Add hours\n3. Remove minutes\n4. Remove hours\n'))

if user_input == 1:
    minutes_to_add = int(input('How many minutes do you want to add?\n'))
    my_time.add_minutes(minutes_to_add)
    print(my_time)
elif user_input == 2:
    hours_to_add = int(input('How many hours do you want to add?\n'))
    my_time.add_hours(hours_to_add)
    print(my_time)
elif user_input == 3:
    minutes_to_minus = int(input('How many minutes do you want to minus?\n'))
    my_time.minus_minutes(minutes_to_minus)
    print(my_time)
elif user_input == 4:
    hours_to_minus = int(input('How many hours do you want to minus?\n'))
    my_time.minus_hours(hours_to_minus)
    print(my_time)
else:
    print('No such option.')

    