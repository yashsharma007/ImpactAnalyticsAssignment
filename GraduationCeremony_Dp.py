class graduationCeremony_Dp:
    def __init__(self,days):
        self.days = days
    def countLegalMissWays(self):
        # Initialize a dynamic programming array to store the number of ways to miss the ceremony
        dp = [0] * (self.days + 1)
        dp[0] = 1  # Base case: there is one way to not miss when there are no days
        
        # Iterate through the days from 1 to N
        for i in range(1, self.days + 1):
            dp[i] = dp[i - 1]  # If absent on day i, add ways to not miss on previous day
            
            # Check if absent on previous 2, 3, and 4 days and add the ways
            if i >= 2:
                dp[i] += dp[i - 2]
            if i >= 3:
                dp[i] += dp[i - 3]
            if i >= 4:
                dp[i] += dp[i - 4]
        
        # Subtract cases where missing 4 or more consecutive days to get legal ways
        legal_miss_ways = dp[self.days]
        legal_miss_ways -= dp[max(self.days - 4, 0)]
        return legal_miss_ways
        
    def countTotalNumberOfLegalWays(self):
        if self.days < 4:
            return 0
        
        # Initialize a dynamic programming array to store the number of ways to be absent
        dp = [0] * (self.days + 1)
        
        # Base cases
        dp[0] = 1  # No days, one way to be absent (absent for 0 days)
        dp[1] = 2  # One day, two ways (absent for 0 or 1 days)
        dp[2] = 4  # Two days, four ways (absent for 0, 1, or 2 days)
        dp[3] = 8  # Three days, eight ways (absent for 0, 1, 2, or 3 days)
        
        # Iterate through the days from 4 to n
        for i in range(4, self.days + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]
        
        # Subtract from total possible ways to get consecutive absent ways
        consecutive_absent_ways = 2 ** self.days - dp[self.days]
        return 2 ** self.days - consecutive_absent_ways
    
    def probability_to_miss_graduation_ceremony(self):
        # Calculate the probability of missing the graduation ceremony by dividing the number of ways the student misses
        # the ceremony by the number of eligible ways to attend.
        return (str(self.countLegalMissWays())+"/"+str(self.countTotalNumberOfLegalWays()))


