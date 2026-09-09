year = 2000
"""
First, calculate the number of days elapsed without leap years (365 * (year - 1970))
Then calculate the number of leap days that have occurred between January 1 of year and January 1, 1970.
The leap year directly before 1970 is 1968, so we can subtract 1968 from year to obtain the years elapsed
since the most recent leap year, then floor divide by 4 to get the number of leap days that have occurred.
However, there's one more step -- since we're going from January 1 of year, the leap day in year hasn't 
happened yet. So we need to subtract 1 from year so we don't count the leap day of that year (which will
happen after January 1).
"""
# then calculate the number of leap days that have occurred -- since leap days don't happen 
days_elapsed = 365 * (year - 1970) + ((year - 1 - 1968) // 4)
print(days_elapsed)

"""
We know our first full moon occurred on January 22, 1970, which is 21 days after January 1, 1970. 
We subtract 21 from days_elapsed to get the number of days elapsed since the first full moon,
then floor divide by the length of a synodic month to get the number of full moons that occurred
*after* the first full moon. Then we add 1 for that first full moon. 
"""
full_moons = (days_elapsed - 21) // 29.53 + 1
print(full_moons)
