# put your python code here
def event_time(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds


def time_difference(a, b):
    return abs(a - b)


hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())

hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())

event_1 = event_time(hours_1, minutes_1, seconds_1)
event_2 = event_time(hours_2, minutes_2, seconds_2)

print(time_difference(event_1, event_2))
