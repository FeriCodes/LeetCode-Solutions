class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        largest = None
        second = None
        third = None

        for i in nums:

            # Ignore duplicate numbers
            if i == largest or i == second or i == third:
                continue

            # New largest number
            if largest is None or i > largest:
                third = second
                second = largest
                largest = i

            # New second largest number
            elif second is None or i > second:
                third = second
                second = i

            # New third largest number
            elif third is None or i > third:
                third = i

        # If there are fewer than 3 distinct numbers
        if third is None:
            return largest

        return third



            