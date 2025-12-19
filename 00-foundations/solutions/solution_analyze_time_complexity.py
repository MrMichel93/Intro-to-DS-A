"""
Solution: Analyze Time Complexity (Challenge 1)

This file demonstrates the analysis techniques for determining time complexity
of code snippets. These are analytical problems, not implementation problems.

The key skill is recognizing patterns and counting operations.
"""


# =============================================================================
# PROBLEM 1A: Constant Time O(1)
# =============================================================================

def process_first_three(arr):
    """
    Process the first three elements of an array.
    
    TIME COMPLEXITY ANALYSIS:
    -------------------------
    Let's count operations:
    
    Line-by-line breakdown:
    1. len(arr) - O(1): Python lists store length as metadata
    2. if comparison - O(1): Single comparison operation
    3. arr[0] access - O(1): Direct index access
    4. arr[1] access - O(1): Direct index access
    5. arr[2] access - O(1): Direct index access
    6. First addition (+) - O(1): Arithmetic operation
    7. Second addition (+) - O(1): Arithmetic operation
    8. return statement - O(1): Single operation
    
    Total operations: 8 constant-time operations
    
    ANSWER: O(1) - Constant Time
    
    Why?
    ----
    - Number of operations does NOT depend on array size
    - Whether arr has 10 or 10,000,000 elements, we do ~8 operations
    - We only access first 3 elements, never iterate through the array
    - This is the definition of constant time complexity
    
    Real-World Example:
    -------------------
    Accessing your most recent email in Gmail is O(1) - the system knows
    exactly where it is and retrieves it instantly, regardless of how many
    total emails you have (10 or 100,000).
    """
    if len(arr) < 3:
        return None
    
    total = arr[0] + arr[1] + arr[2]
    return total


# =============================================================================
# PROBLEM 1B: Linear Time O(n)
# =============================================================================

def find_target_count(arr, target):
    """
    Count how many times target appears in array.
    
    TIME COMPLEXITY ANALYSIS:
    -------------------------
    Let n = length of array
    
    Line-by-line breakdown:
    1. count = 0 - O(1): Variable initialization
    2. for element in arr - O(n): Loop runs n times
       - Within loop:
         a. if comparison - O(1): Done n times
         b. count += 1 - O(1): Done at most n times
    3. return statement - O(1): Single operation
    
    Total operations: 1 + n*(1 to 2) + 1 ≈ 2n + 2
    
    ANSWER: O(n) - Linear Time
    
    Why?
    ----
    - Must examine EVERY element in the array
    - Operations scale linearly with input size
    - If array doubles in size, operations double
    - Cannot optimize further without additional data structures
    
    Best Case vs Worst Case:
    ------------------------
    - Best case: Still O(n) - must check all elements
    - Worst case: Still O(n) - must check all elements
    - Average case: O(n) - must check all elements
    
    Why always O(n)? Because even if target is at the start, we must
    continue to count ALL occurrences, so we scan the entire array.
    
    Real-World Example:
    -------------------
    Searching for all instances of a word in a document requires reading
    every word. A 100-page document takes ~100x longer than a 1-page document.
    This is O(n) behavior.
    """
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count


# =============================================================================
# DEMONSTRATION: How Array Size Affects Running Time
# =============================================================================

def demonstrate_complexity():
    """
    Demonstrates the difference between O(1) and O(n) complexity.
    """
    print("=== Time Complexity Demonstration ===\n")
    
    # Test with different array sizes
    sizes = [10, 100, 1000, 10000]
    
    print("CONSTANT TIME O(1) - process_first_three()")
    print("Array Size | Operations")
    print("-" * 30)
    for size in sizes:
        arr = list(range(size))
        operations = 8  # Always ~8 operations
        print(f"{size:10,} | {operations}")
    
    print("\nNotice: Operations stay constant as array grows!")
    print("This is O(1) - the hallmark of constant time.\n")
    
    print("=" * 60)
    print("\nLINEAR TIME O(n) - find_target_count()")
    print("Array Size | Approximate Operations")
    print("-" * 40)
    for size in sizes:
        arr = list(range(size))
        operations = 2 * size + 2  # ~2n operations
        print(f"{size:10,} | {operations:,}")
    
    print("\nNotice: Operations grow proportionally with array size!")
    print("This is O(n) - operations scale linearly with input.")
    
    print("\n" + "=" * 60)
    print("COMPARISON: Same Operation Count at Different Sizes")
    print("=" * 60)
    
    print("\nFor O(1) algorithm:")
    print("  Array of 10:     ~8 operations")
    print("  Array of 10,000: ~8 operations")
    print("  Ratio: 1:1 (no change!)")
    
    print("\nFor O(n) algorithm:")
    print("  Array of 10:     ~22 operations")
    print("  Array of 10,000: ~20,002 operations")
    print("  Ratio: 1:909 (nearly 1000x more work!)")


# =============================================================================
# KEY PATTERNS FOR RECOGNIZING TIME COMPLEXITY
# =============================================================================

def complexity_patterns():
    """
    Common patterns that indicate different time complexities.
    """
    print("\n=== Recognizing Time Complexity Patterns ===\n")
    
    patterns = {
        "O(1) - Constant Time": [
            "Direct array access: arr[5]",
            "Arithmetic operations: a + b, x * y",
            "Variable assignment: x = 10",
            "First/last element access: arr[0], arr[-1]",
            "Fixed number of operations regardless of input size"
        ],
        
        "O(n) - Linear Time": [
            "Single loop through array: for x in arr",
            "Visiting each element once: while i < len(arr)",
            "Linear search in unsorted data",
            "Summing/counting all elements",
            "Operations that must touch every element once"
        ],
        
        "O(log n) - Logarithmic Time": [
            "Binary search in sorted array",
            "Repeatedly dividing problem in half",
            "Tree operations on balanced trees",
            "Finding element in sorted data by halving"
        ],
        
        "O(n log n) - Linearithmic Time": [
            "Efficient sorting algorithms (merge sort, quicksort)",
            "Sorting followed by linear scan",
            "Tree-based operations on all elements"
        ],
        
        "O(n²) - Quadratic Time": [
            "Nested loops: for i in arr: for j in arr:",
            "Comparing every pair of elements",
            "Bubble sort, insertion sort",
            "Matrix operations"
        ]
    }
    
    for complexity, examples in patterns.items():
        print(f"{complexity}:")
        for example in examples:
            print(f"  - {example}")
        print()


# =============================================================================
# PRACTICE: Analyze These Code Snippets
# =============================================================================

def practice_problems():
    """
    Additional problems to practice complexity analysis.
    """
    print("\n=== Practice Problems ===\n")
    
    print("Analyze the time complexity of each function:\n")
    
    # Problem 1
    print("1. def get_last(arr):")
    print("       return arr[-1]")
    print("   Answer: O(1) - Direct index access\n")
    
    # Problem 2
    print("2. def find_max(arr):")
    print("       max_val = arr[0]")
    print("       for num in arr:")
    print("           if num > max_val:")
    print("               max_val = num")
    print("       return max_val")
    print("   Answer: O(n) - Single pass through array\n")
    
    # Problem 3
    print("3. def has_duplicates(arr):")
    print("       for i in range(len(arr)):")
    print("           for j in range(i+1, len(arr)):")
    print("               if arr[i] == arr[j]:")
    print("                   return True")
    print("       return False")
    print("   Answer: O(n²) - Nested loops comparing all pairs\n")
    
    # Problem 4
    print("4. def binary_search(arr, target):")
    print("       # Assumes arr is sorted")
    print("       left, right = 0, len(arr) - 1")
    print("       while left <= right:")
    print("           mid = (left + right) // 2")
    print("           if arr[mid] == target:")
    print("               return mid")
    print("           elif arr[mid] < target:")
    print("               left = mid + 1")
    print("           else:")
    print("               right = mid - 1")
    print("       return -1")
    print("   Answer: O(log n) - Halves search space each iteration\n")


# =============================================================================
# RUNNING ALL DEMONSTRATIONS
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("TIME COMPLEXITY ANALYSIS - CHALLENGE 1 SOLUTIONS")
    print("=" * 70)
    
    # Show the demonstrations
    demonstrate_complexity()
    
    print("\n" + "=" * 70)
    complexity_patterns()
    
    print("=" * 70)
    practice_problems()
    
    # Key Takeaways
    print("=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)
    print("""
1. COUNT OPERATIONS, NOT LINES OF CODE
   - Focus on how operations scale with input size
   - Constants don't matter in Big-O notation
   
2. LOOK FOR LOOPS
   - No loops (just direct access): O(1)
   - One loop: O(n)
   - Nested loops: O(n²)
   - Loop that halves: O(log n)
   
3. WORST CASE ANALYSIS
   - Big-O describes worst-case scenario
   - Even if best case is fast, analyze worst case
   
4. DROP CONSTANTS AND LOWER TERMS
   - O(3n + 5) → O(n)
   - O(n² + n) → O(n²)
   - O(2ⁿ + n²) → O(2ⁿ)
   
5. PRACTICE RECOGNIZING PATTERNS
   - More you analyze, faster you become
   - Start by counting operations explicitly
   - Eventually, patterns become intuitive
    """)
