class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total_happiness = 0

        for i, child in enumerate(happiness):
            gain = child - i
            if gain <= 0 or i == k:
                break
            else:
                total_happiness += gain
        return total_happiness