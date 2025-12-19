# Stacks Module - Practice Challenges

These challenges will help you master stack operations, including LIFO principles, balanced parentheses, monotonic stacks, and expression evaluation.

## Challenge 1: Valid Parentheses (Beginner)

**Difficulty:** Beginner 🟢

**Objective**: Determine if a string of brackets is valid and properly balanced.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(n)

**Real-World Use Case**: Code editors like Visual Studio Code use stack-based algorithms to validate bracket matching in real-time. As you type code, the editor highlights matching pairs and warns about unbalanced brackets, helping prevent syntax errors before compilation.

### Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

### Examples

**Example 1**:
```python
Input: s = "()"
Output: True
```

**Example 2**:
```python
Input: s = "()[]{}"
Output: True
```

**Example 3**:
```python
Input: s = "(]"
Output: False
Explanation: Opening '(' but closing with ']'
```

**Example 4**:
```python
Input: s = "([)]"
Output: False
Explanation: Brackets are not closed in correct order
```

### Constraints

- 1 ≤ s.length ≤ 10⁴
- s consists of parentheses only: '()[]{}' 

### Hints

<details>
<summary>Hint 1</summary>
Use a stack to keep track of opening brackets. When you encounter a closing bracket, check if it matches the most recent opening bracket.
</details>

<details>
<summary>Hint 2</summary>
Create a mapping of closing brackets to their corresponding opening brackets for quick lookup.
</details>

<details>
<summary>Hint 3</summary>
At the end, the stack should be empty for the string to be valid.
</details>

---

## Challenge 2: Min Stack (Beginner)

**Difficulty:** Beginner 🟢

**Objective**: Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.

**Expected Time Complexity**: O(1) for all operations
**Expected Space Complexity**: O(n)

**Real-World Use Case**: Stock trading platforms maintain a "min stack" to track the lowest stock price within a trading session. This allows traders to instantly see the session's minimum price without recalculating, crucial for high-frequency trading where microseconds matter.

### Problem Statement

Design a stack that supports the following operations in constant time:
- `push(val)`: Push element val onto the stack
- `pop()`: Remove the element on top of the stack
- `top()`: Get the top element
- `getMin()`: Retrieve the minimum element in the stack

### Examples

**Example 1**:
```python
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   # Returns -3
minStack.pop()
minStack.top()      # Returns 0
minStack.getMin()   # Returns -2
```

**Example 2**:
```python
minStack = MinStack()
minStack.push(5)
minStack.push(2)
minStack.push(7)
minStack.getMin()   # Returns 2
minStack.pop()
minStack.getMin()   # Returns 2
```

### Constraints

- -2³¹ ≤ val ≤ 2³¹ - 1
- Methods pop, top and getMin will always be called on non-empty stacks
- At most 3 × 10⁴ calls will be made to push, pop, top, and getMin

### Hints

<details>
<summary>Hint 1</summary>
Use two stacks: one for actual values, one for minimum values at each level.
</details>

<details>
<summary>Hint 2</summary>
When pushing, also push the current minimum onto the min stack.
</details>

<details>
<summary>Hint 3</summary>
Both stacks should always have the same size, so pop and push operations stay synchronized.
</details>

---

## Challenge 3: Daily Temperatures (Intermediate)

**Difficulty:** Intermediate 🟡

**Objective**: Find the number of days until a warmer temperature for each day.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(n)

**Real-World Use Case**: Weather forecasting apps use similar algorithms to provide "next warmer day" predictions. By processing historical temperature data with a monotonic stack, meteorologists can identify weather patterns and predict when temperatures will rise, helping users plan outdoor activities.

### Problem Statement

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Examples

**Example 1**:
```python
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation:
- Day 0: Next warmer is day 1 (74 > 73), wait 1 day
- Day 1: Next warmer is day 2 (75 > 74), wait 1 day
- Day 2: Next warmer is day 6 (76 > 75), wait 4 days
```

**Example 2**:
```python
Input: temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

**Example 3**:
```python
Input: temperatures = [30, 60, 90]
Output: [1, 1, 0]
```

### Constraints

- 1 ≤ temperatures.length ≤ 10⁵
- 30 ≤ temperatures[i] ≤ 100

### Hints

<details>
<summary>Hint 1</summary>
Use a monotonic decreasing stack that stores indices of days.
</details>

<details>
<summary>Hint 2</summary>
When you find a warmer day, pop all colder days from the stack and calculate their wait times.
</details>

<details>
<summary>Hint 3</summary>
Process temperatures from left to right, maintaining indices in the stack where we haven't found warmer days yet.
</details>

---

## Challenge 4: Evaluate Reverse Polish Notation (Intermediate)

**Difficulty:** Intermediate 🟡

**Objective**: Evaluate an arithmetic expression in Reverse Polish Notation.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(n)

**Real-World Use Case**: Programming language compilers convert infix expressions (like "2 + 3 * 4") to postfix notation (Reverse Polish Notation) for efficient evaluation. This stack-based evaluation is faster and simpler than parsing infix expressions with operator precedence, making it essential for interpreters and calculators.

### Problem Statement

Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Division between two integers should truncate toward zero.

### Examples

**Example 1**:
```python
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2**:
```python
Input: tokens = ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3**:
```python
Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
```

### Constraints

- 1 ≤ tokens.length ≤ 10⁴
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200]

### Hints

<details>
<summary>Hint 1</summary>
Use a stack to store operands. When you encounter an operator, pop two operands, apply the operation, and push the result back.
</details>

<details>
<summary>Hint 2</summary>
Process tokens from left to right. Numbers go on the stack, operators consume from the stack.
</details>

<details>
<summary>Hint 3</summary>
For division in Python, use int(a/b) to truncate toward zero, not a//b which floors toward negative infinity.
</details>

---

## Challenge 5: Largest Rectangle in Histogram (Advanced)

**Difficulty:** Advanced 🔴

**Objective**: Find the largest rectangular area in a histogram.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(n)

**Real-World Use Case**: Computer vision systems use histogram-based rectangle detection for image analysis. When processing building blueprints or architectural drawings, algorithms identify the largest rectangular spaces (rooms, parking areas) by treating wall heights as histogram bars, optimizing space utilization in construction planning.

### Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

### Examples

**Example 1**:
```python
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: The largest rectangle has height 5 and width 2 (bars at indices 2 and 3)
```

**Example 2**:
```python
Input: heights = [2, 4]
Output: 4
Explanation: Rectangle of height 2 and width 2
```

**Example 3**:
```python
Input: heights = [1, 1, 1, 1, 1]
Output: 5
Explanation: Rectangle of height 1 spanning all 5 bars
```

### Constraints

- 1 ≤ heights.length ≤ 10⁵
- 0 ≤ heights[i] ≤ 10⁴

### Hints

<details>
<summary>Hint 1</summary>
Use a monotonic increasing stack to track indices of bars.
</details>

<details>
<summary>Hint 2</summary>
When you find a bar shorter than the stack top, pop and calculate area using the popped bar's height.
</details>

<details>
<summary>Hint 3</summary>
The width of the rectangle is determined by the current index and the index below the popped element in the stack.
</details>

<details>
<summary>Hint 4</summary>
Add a sentinel value (0) at the end to ensure all bars are processed.
</details>

---

## Challenge 6: Basic Calculator (Advanced)

**Difficulty:** Advanced 🔴

**Objective**: Implement a basic calculator to evaluate a mathematical expression string with parentheses.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(n)

**Real-World Use Case**: Spreadsheet applications like Excel use stack-based expression evaluators to process formulas with nested parentheses (e.g., "=(A1+B1)*(C1-D1)"). The stack handles operator precedence and parentheses nesting, allowing users to create complex calculations without worrying about evaluation order.

### Problem Statement

Implement a basic calculator to evaluate a simple expression string containing:
- Non-negative integers
- The operators `+` and `-`
- Opening and closing parentheses `(` and `)`
- Spaces ` `

Return the result of the evaluation.

### Examples

**Example 1**:
```python
Input: s = "1 + 1"
Output: 2
```

**Example 2**:
```python
Input: s = " 2-1 + 2 "
Output: 3
```

**Example 3**:
```python
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

**Example 4**:
```python
Input: s = "2-(5-6)"
Output: 3
```

### Constraints

- 1 ≤ s.length ≤ 3 × 10⁵
- s consists of digits, '+', '-', '(', ')', and ' '
- s represents a valid expression
- Every number and running calculation fits in a 32-bit integer

### Hints

<details>
<summary>Hint 1</summary>
Use a stack to handle parentheses. Push current result and sign when you encounter '('.
</details>

<details>
<summary>Hint 2</summary>
Maintain current number, result, and sign as you scan the string.
</details>

<details>
<summary>Hint 3</summary>
When you encounter ')', pop from stack to get the result and sign before the parentheses, then combine with current result.
</details>

<details>
<summary>Hint 4</summary>
Handle multi-digit numbers by accumulating digits until you hit an operator or parenthesis.
</details>

---

## Summary and Next Steps

These challenges covered:
- ✅ Stack fundamentals with bracket matching (Challenge 1)
- ✅ Auxiliary stack for O(1) min retrieval (Challenge 2)
- ✅ Monotonic stack for next greater element patterns (Challenge 3)
- ✅ Stack-based expression evaluation (Challenge 4)
- ✅ Advanced monotonic stack for area calculations (Challenge 5)
- ✅ Complex expression parsing with nested operations (Challenge 6)

### Key Lessons

1. **Stacks perfect for matching/nesting** - Brackets, parentheses, tags
2. **Monotonic stacks solve "next greater/smaller" efficiently** - O(n) vs O(n²)
3. **Auxiliary structures enable O(1) queries** - Track min/max alongside main data
4. **Postfix evaluation simpler than infix** - No operator precedence needed
5. **Stacks handle nested operations naturally** - Recursion and parentheses

### Ready for More?

Once you're comfortable with these challenges, explore:
- **[Queues](../queues/)** - Learn FIFO operations
- **[Trees](../trees/)** - Master recursive structures (use call stack!)
- **[Graphs](../graphs/)** - Depth-First Search uses explicit/implicit stacks

---

💡 **Remember**: Whenever you see nested structures, matching pairs, or need to "remember and come back," think STACK!
