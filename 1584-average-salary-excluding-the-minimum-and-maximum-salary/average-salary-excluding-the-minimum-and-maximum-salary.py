class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = min(salary)
        max_sal = max(salary)
        total = sum(salary) - min_sal - max_sal
        average = total / (len(salary) - 2)
        return average
        