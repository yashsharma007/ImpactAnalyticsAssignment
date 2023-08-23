from itertools import product
class graduationCeremony:
    def __init__(self, days):
        if not isinstance(days, int):
            raise TypeError("Days must be of type int")
        
        # Number of given days.
        self.days = days
        
        # List of total number of combination to attend/absent classes on given days.
        self._totalWaysToAttendClassList = self.totalPossibleWaysToAttendClass()

    def totalPossibleWays(self):
        # This method returns the total number of possible ways to attend or miss class.
        return len(self._totalWaysToAttendClassList)

    def totalPossibleWaysToAttendClass(self):
        # This function returns the combinations of attending or missing class using 'A' and 'P'.
        return [''.join(p) for p in product('AP', repeat=self.days)]

    def ineligibleWaysToAttendClass(self):
        # This function filters and returns only the combinations with at least 4 consecutive absences.
        ineligible_ways = list(filter(lambda ans: "AAAA" in ans, self._totalWaysToAttendClassList))
        return ineligible_ways

    def eligibleWaysToAttendClass(self):
        # This function calculates the number of ways to attend class that are not ineligible.
        ineligible_ways_count = len(self.ineligibleWaysToAttendClass())
        return self.totalPossibleWays() - ineligible_ways_count

    def waysStudentMissesTheirGraduationCer(self):
        # This function filters and returns the combinations where the student is absent on the last day.
        eligible_ways_list = list(filter(lambda ans: "AAAA" not in ans, self._totalWaysToAttendClassList))
        records = [sol for sol in eligible_ways_list if sol[-1] == "A"]
        return len(records)

    def probabilitytoMissGradCeremony(self):
        # Calculate the probability of missing the graduation ceremony by dividing the number of ways the student misses
        # the ceremony by the number of eligible ways to attend.
        return str(self.waysStudentMissesTheirGraduationCer()) + "/" + str(self.eligibleWaysToAttendClass())
