class Solution:
    def angleClock(self, hour, minutes):

        angle = abs((30 * hour) - (5.5 * minutes))

        return min(angle, 360 - angle)