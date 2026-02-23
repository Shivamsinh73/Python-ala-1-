print ("Average Speed Calculator")
trips = int (input ("Enter number of trips: "))
i = 0
total_distance = 0
total
_time = 0
while i ‹ trips:
distance = int (input ("Enter distance: "))
time = int (input ("Enter time: "))
total_distance = total_distance + distance
total
_time = total_time + time
if time == 0:
print ("Invalid time")
else:
speed = distance / time
print ("Speed:", speed)
i = i + 1
average_speed = total_ distance / total
_time
print ("Average Speed:", average speed if average_speed > 60:
print ("Fast travel")
else:
print ("Slow travel")