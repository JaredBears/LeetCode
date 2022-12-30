class Solution:
    # Calculate the angle between the hour and minute hands
    # To find the initial angle of the hour hand, we need to multiple the hour by 30 degrees
    # To find the angle of the minute hand, we need to multiple the minute by 6 degrees
    # To compensate for the movement of the minute hand, we need to add the number of minutes 
    # divided by 60 times 30 to the hour hand
    # To find the angle between the two hands, we need to find the absolute value of the difference
    # If the difference is greater than 180, we need to subtract the difference from 180
    def angleClock(self, hour: int, minutes: int) -> float:
        hourDeg = hour * 30
        minDeg = minutes * 6
        hourDeg += (minutes/60) * 30
        delta = abs(hourDeg - minDeg)
        if delta > 180:
            return 180 - (delta - 180)
        return delta