"""
exercise-2.2.3

If I leave my house at 6:52 am and run 1 mile at an easy 
pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) 
and 1 mile at an easy pace again, what time do I get home 
for breakfast?

"""

# input
init_time     = 6 * 60 + 52     # minutes after 12:00 am

running_speed = 8 + 15 / 60.0   # minutes per mile
running_dist  = 1 + 1           # miles (before and after tempo)

tempo_speed   = 7 + 12 / 60.0   # minutes per mile
tempo_dist    = 3               # miles

# calculation
running_time  = running_dist * running_speed
tempo_time    = tempo_dist * tempo_speed
total_time    = running_time + tempo_time

time_at_home = init_time + total_time    # minutes

# convert minutes into time
hours = time_at_home // 60
minutes = time_at_home - hours * 60

print("I get home for breakfast at:", str(round(hours)) + ':' + str(round(minutes)))

