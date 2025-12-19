"""
Solution: Analyze Nested Operations (Challenge 2)

This file demonstrates analysis of nested loops and their impact on time complexity.
Understanding nested loops is critical for recognizing O(n²) algorithms.
"""


# =============================================================================
# PROBLEM 2A: Quadratic Time O(n²) - All Pairs
# =============================================================================

def print_pairs(arr):
    """
    Print all possible pairs from an array.
    
    TIME COMPLEXITY ANALYSIS:
    -------------------------
    Let n = length of array
    
    Outer loop iterations: n
    Inner loop iterations per outer:
    - When i=0: inner runs (n-1) times
    - When i=1: inner runs (n-2) times
    - When i=2: inner runs (n-3) times
    - ...
    - When i=n-2: inner runs 1 time
    - When i=n-1: inner runs 0 times
    
    Total iterations: (n-1) + (n-2) + ... + 1 + 0
    This is an arithmetic series: sum = n(n-1)/2
    
    Expanding: n(n-1)/2 = (n² - n)/2 = 0.5n² - 0.5n
    
    In Big-O notation:
    - Drop constants: 0.5n² → n²
    - Drop lower-order terms: n² - 0.5n → n²
    
    ANSWER: O(n²) - Quadratic Time
    
    Why?
    ----
    - Nested loops with both dependent on input size
    - For each element, we process multiple other elements
    - Operations grow quadratically with input size
    
    Examples:
    ---------
    n=5:  (5-1) + (5-2) + (5-3) + (5-4) = 4+3+2+1 = 10 pairs
    n=10: (10-1) + (10-2) + ... + 1 = 9+8+7+6+5+4+3+2+1 = 45 pairs
    
    Formula: n(n-1)/2
    - n=5:  5*4/2 = 10 ✓
    - n=10: 10*9/2 = 45 ✓
    
    Real-World Example:
    -------------------
    Handshakes at a party: if 10 people each shake hands with the other 9,
    that's 45 unique handshakes. For 100 people, it's 4,950 handshakes.
    This quadratic growth is O(n²).
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(f"Pair: {arr[i]}, {arr[j]}")


def count_pairs(n):
    """
    Calculate how many pairs for array of length n.
    
    Formula: n(n-1)/2
    
    This is a mathematical solution to avoid running the nested loops.
    """
    return n * (n - 1) // 2


# =============================================================================
# PROBLEM 2B: Quadratic Time O(n²) - Full Grid
# =============================================================================

def create_grid(n):
    """
    Create an n×n multiplication table.
    
    TIME COMPLEXITY ANALYSIS:
    -------------------------
    Outer loop: n iterations
    Inner loop: n iterations per outer iteration
    Total iterations: n × n = n²
    
    Each iteration does O(1) work:
    - One multiplication: O(1)
    - One append: O(1)
    
    ANSWER: O(n²) - Quadratic Time
    
    SPACE COMPLEXITY ANALYSIS:
    ---------------------------
    Creating a grid of size n×n:
    - Total elements stored: n × n = n²
    
    ANSWER: O(n²) - Quadratic Space
    
    This is a case where time and space complexity match!
    
    Examples:
    ---------
    n=3:  3×3 = 9 elements, 9 multiplications
    n=10: 10×10 = 100 elements, 100 multiplications
    n=100: 100×100 = 10,000 elements, 10,000 multiplications
    
    Real-World Example:
    -------------------
    Creating a distance matrix for all pairs of cities. With 100 cities,
    you need 10,000 entries (100×100). With 1,000 cities, you need
    1,000,000 entries. This quadratic growth makes large-scale problems
    computationally expensive.
    """
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        grid.append(row)
    return grid


# =============================================================================
# COMPARING: O(n) vs O(n²)
# =============================================================================

def demonstrate_quadratic_growth():
    """
    Demonstrates the dramatic difference between O(n) and O(n²).
    """
    print("=== O(n) vs O(n²) Growth Comparison ===\n")
    
    print("Input Size (n) | O(n) Operations | O(n²) Operations | Ratio")
    print("-" * 70)
    
    sizes = [10, 50, 100, 500, 1000]
    
    for n in sizes:
        linear = n
        quadratic = n * n
        ratio = quadratic / linear if linear > 0 else 0
        print(f"{n:14} | {linear:15,} | {quadratic:16,} | {ratio:.0f}x")
    
    print("\nNotice: As n grows, O(n²) grows MUCH faster than O(n)!")
    print("At n=1000, quadratic is 1000x more operations than linear.")


def demonstrate_pair_counting():
    """
    Demonstrates why the inner loop starting at i+1 gives n(n-1)/2.
    """
    print("\n=== Understanding Pair Counting ===\n")
    
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    
    print(f"Array: {arr}")
    print(f"Length: {n}\n")
    
    print("Iteration breakdown:")
    total_pairs = 0
    
    for i in range(len(arr)):
        pairs_this_iteration = len(arr) - i - 1
        total_pairs += pairs_this_iteration
        print(f"i={i} (arr[{i}]={arr[i]}): pairs with {pairs_this_iteration} later elements")
        
        # Show the actual pairs
        for j in range(i + 1, len(arr)):
            print(f"  -> ({arr[i]}, {arr[j]})")
    
    print(f"\nTotal pairs: {total_pairs}")
    print(f"Formula n(n-1)/2: {n}*{n-1}/2 = {count_pairs(n)}")
    print(f"Both match: {total_pairs == count_pairs(n)}")


# =============================================================================
# TYPES OF NESTED LOOPS
# =============================================================================

def nested_loop_patterns():
    """
    Different nested loop patterns and their complexities.
    """
    print("\n=== Nested Loop Patterns ===\n")
    
    patterns = [
        {
            "name": "Full nested (both loops depend on n)",
            "code": "for i in range(n):\n    for j in range(n):",
            "complexity": "O(n²)",
            "iterations": "n × n = n²",
            "example": "Comparing every element with every other element"
        },
        {
            "name": "Triangular (inner starts from i)",
            "code": "for i in range(n):\n    for j in range(i+1, n):",
            "complexity": "O(n²)",
            "iterations": "n(n-1)/2 ≈ n²/2 = O(n²)",
            "example": "Finding all pairs (like handshakes)"
        },
        {
            "name": "Fixed inner loop",
            "code": "for i in range(n):\n    for j in range(100):",
            "complexity": "O(n)",
            "iterations": "n × 100 = 100n = O(n)",
            "example": "Processing each element a constant number of times"
        },
        {
            "name": "Dependent but different inputs",
            "code": "for i in range(n):\n    for j in range(m):",
            "complexity": "O(n × m)",
            "iterations": "n × m",
            "example": "Processing two different-sized datasets together"
        },
        {
            "name": "Triple nested",
            "code": "for i in range(n):\n    for j in range(n):\n        for k in range(n):",
            "complexity": "O(n³)",
            "iterations": "n × n × n = n³",
            "example": "3D matrix operations, comparing triplets"
        }
    ]
    
    for i, pattern in enumerate(patterns, 1):
        print(f"{i}. {pattern['name']}")
        print(f"   Code: {pattern['code']}")
        print(f"   Complexity: {pattern['complexity']}")
        print(f"   Iterations: {pattern['iterations']}")
        print(f"   Example: {pattern['example']}")
        print()


# =============================================================================
# COMMON O(n²) ALGORITHMS
# =============================================================================

def bubble_sort_example(arr):
    """
    Classic O(n²) algorithm: Bubble Sort
    
    Time Complexity: O(n²)
    - Outer loop: n passes
    - Inner loop: up to n comparisons per pass
    - Total: ~n² comparisons and swaps
    
    This is why bubble sort is inefficient for large datasets!
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        # Each pass bubbles the largest element to the end
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def selection_sort_example(arr):
    """
    Another O(n²) algorithm: Selection Sort
    
    Time Complexity: O(n²)
    - Outer loop: n selections
    - Inner loop: n-i comparisons to find minimum
    - Total: n(n-1)/2 ≈ n²/2 = O(n²)
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        # Find minimum element in remaining unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum with first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


# =============================================================================
# RUNNING ALL DEMONSTRATIONS
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("NESTED OPERATIONS ANALYSIS - CHALLENGE 2 SOLUTIONS")
    print("=" * 70)
    
    # Demonstrate growth difference
    demonstrate_quadratic_growth()
    
    # Show pair counting in detail
    demonstrate_pair_counting()
    
    # Explain different patterns
    nested_loop_patterns()
    
    # Show grid example
    print("\n=== Grid Creation Example ===\n")
    grid_3x3 = create_grid(3)
    print("3×3 multiplication table:")
    for row in grid_3x3:
        print(row)
    print(f"\nOperations: 3² = {3*3}")
    
    # Show sorting examples
    print("\n=== O(n²) Sorting Algorithms ===\n")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {test_arr}")
    print(f"Bubble Sort: {bubble_sort_example(test_arr)}")
    print(f"Selection Sort: {selection_sort_example(test_arr)}")
    print(f"\nBoth are O(n²) - inefficient for large arrays!")
    
    # Key Takeaways
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)
    print("""
1. NESTED LOOPS → MULTIPLY COMPLEXITIES
   - One loop: O(n)
   - Two nested loops: O(n × n) = O(n²)
   - Three nested loops: O(n × n × n) = O(n³)

2. O(n²) GROWS VERY FAST
   - n=10: 100 operations
   - n=100: 10,000 operations (100x more!)
   - n=1000: 1,000,000 operations (10,000x more!)

3. EVEN HALF THE PAIRS IS STILL O(n²)
   - n(n-1)/2 simplifies to O(n²)
   - Constants don't matter in Big-O
   - 0.5n² is still quadratic growth

4. WATCH OUT FOR NESTED LOOPS IN PRODUCTION
   - O(n²) algorithms become bottlenecks at scale
   - 1000 users = 1 million operations
   - 10,000 users = 100 million operations
   - Often need to optimize to O(n log n) or O(n)

5. COMMON O(n²) SCENARIOS
   - Comparing all pairs
   - Nested iterations over same data
   - Bubble sort, selection sort, insertion sort
   - Naive matrix multiplication
   - Finding all substrings

6. HOW TO OPTIMIZE O(n²)
   - Use hash sets for O(1) lookups → O(n)
   - Use sorting + two pointers → O(n log n)
   - Use better data structures (trees, graphs)
   - Cache/memoize repeated calculations
    """)
