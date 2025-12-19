"""
Solution: Daily Temperatures (Challenge 3)

Problem: Find days until next warmer temperature.
Classic monotonic stack pattern.
"""


def daily_temperatures(temperatures):
    """
    Find next warmer day using monotonic decreasing stack.
    
    Approach: Maintain stack of indices with decreasing temperatures.
    When warmer day found, pop all colder days and calculate wait times.
    
    Time Complexity: O(n) - each element pushed/popped once
    Space Complexity: O(n) - stack size
    
    Examples:
    >>> daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
    [1, 1, 4, 2, 1, 1, 0, 0]
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Store indices
    
    for i in range(n):
        # Pop all days colder than today
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day
        stack.append(i)
    
    return answer


if __name__ == "__main__":
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Temperatures: {temps}")
    print(f"Days to wait: {daily_temperatures(temps)}")
