"""
exercise-1.2.3

If you run a 10 kilometer race in 42 minutes 42 seconds, 
what is your average pace (time per mile in minutes and 
seconds)? What is your average speed in miles per hour?

"""

# average speed = total distance / total time
# 1.61 kms = 1 miles
# 1 km = 1 / 1.61 miles
# x km = x / 1.61 miles

# 60 minutes = 1 hour
# 1 minutes = 1 / 60 hour
# x minutes = x / 60 hour
# 
# 3600 seconds = 1 hour
# 1 seconds = 1 / 3600 hours
# y seconds = y / 3600 hours
# 

total_time = 42 / 60.0 + 42 / 3600.0    # in hours
total_dist = 10 / 1.61                  # in miles

avg_speed = total_dist / total_time

print("average speed:", round(avg_speed, 4), "miles per hour")

