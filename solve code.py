print("Average Speed Calculator")

trips = int(input("Enter number of trips: "))

i = 0
total_distance = 0
total_time = 0

while i < trips:
    distance = int(input("Enter distance: "))
    time = int(input("Enter time: "))

    if time == 0:
        print("Invalid time")
    else:
        total_distance = total_distance + distance
        total_time = total_time + time

        speed = distance / time
        print("Speed:", speed)

    i = i + 1

if total_time == 0:
    print("Cannot calculate average speed")
else:
    average_speed = total_distance / total_time
    print("Average Speed:", average_speed)

    if average_speed > 60:
        print("Fast travel")
    else:
        print("Slow travel")