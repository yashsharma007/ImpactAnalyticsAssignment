from GraduationCeremony import graduationCeremony
from GraduationCeremony_Dp import graduationCeremony_Dp

if __name__ == "__main__":
    days = int(input())
    mL = graduationCeremony(days)
    print("No. of ways to attend the class with all possible combination is {}" .format(mL.totalPossibleWays()))
    print("No. of ways to attend the class without having 4 or more consecutive absence is {}".format(str(mL.eligibleWaysToAttendClass())))
    print("Probability to miss graduation Ceremony out of all eligible ways: "+ mL.probabilitytoMissGradCeremony())

    mL_dp = graduationCeremony_Dp(days)
    print("Probability to miss graduation Ceremony out of all eligible ways: "+ mL_dp.probability_to_miss_graduation_ceremony())
