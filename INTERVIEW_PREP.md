# Technical Interview Preparation Guide

A comprehensive guide to preparing for data structures and algorithms technical interviews using the concepts from this course.

---

## 📋 Table of Contents

1. [Interview Process Overview](#interview-process-overview)
2. [Common Interview Patterns](#common-interview-patterns)
3. [Interview Tips and Strategies](#interview-tips-and-strategies)
4. [Practice Problem Roadmap](#practice-problem-roadmap)
5. [Module-Specific Interview Problems](#module-specific-interview-problems)
6. [Company-Specific Preparation](#company-specific-preparation)
7. [Mock Interview Guide](#mock-interview-guide)

---

## 🎯 Interview Process Overview

### Typical Technical Interview Structure

**1. Introduction (5 minutes)**
- Small talk and icebreaker
- Overview of interview format
- Questions about your background

**2. Coding Problem(s) (35-40 minutes)**
- 1-2 algorithmic problems
- Live coding on whiteboard or shared editor
- Discussion of approach and trade-offs

**3. Your Questions (5-10 minutes)**
- Your chance to ask about company/team/role
- Shows interest and engagement

### What Interviewers Look For

**✅ Problem-Solving Ability**
- Breaking down complex problems
- Thinking through edge cases
- Systematic approach

**✅ Coding Skills**
- Clean, readable code
- Proper syntax and structure
- Good variable naming

**✅ Communication**
- Explaining your thought process
- Asking clarifying questions
- Discussing trade-offs

**✅ Algorithm Knowledge**
- Understanding data structures
- Knowing time/space complexity
- Optimization awareness

**✅ Adaptability**
- Handling hints and feedback
- Pivoting when stuck
- Learning during the interview

---

## 🎨 Common Interview Patterns

Recognizing these patterns will help you solve 80% of interview problems faster.

### Pattern 1: Two Pointers

**When to use:** Array/string problems with pairs, triplets, or partitioning

**Common problems:**
- Two Sum (sorted array)
- Three Sum
- Container with most water
- Remove duplicates
- Reverse string/array

**Example from this course:**
- Arrays: Problem 2, Problem 4
- Linked Lists: Problem 3 (fast/slow pointers)

**Template:**
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Process current pair
        if condition:
            # Found solution
            return result
        elif need_smaller:
            right -= 1
        else:
            left += 1
```

**Time:** O(n) | **Space:** O(1)

---

### Pattern 2: Sliding Window

**When to use:** Subarray/substring problems with contiguous elements

**Common problems:**
- Maximum sum subarray of size k
- Longest substring without repeating characters
- Find all anagrams in a string
- Minimum window substring

**Example from this course:**
- Arrays: Problem 5, Problem 6

**Template:**
```python
def sliding_window(arr, k):
    window_start = 0
    # Initialize window state
    
    for window_end in range(len(arr)):
        # Add element to window
        
        # Shrink window if needed
        while window_condition:
            # Remove from window_start
            window_start += 1
        
        # Update result
```

**Time:** O(n) | **Space:** O(k)

---

### Pattern 3: Fast & Slow Pointers

**When to use:** Linked list cycle detection, finding middle

**Common problems:**
- Detect cycle in linked list
- Find middle of linked list
- Happy number problem
- Palindrome linked list

**Example from this course:**
- Linked Lists: Problem 3, Problem 5

**Template:**
```python
def fast_slow_pointers(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle detected
    
    return False
```

**Time:** O(n) | **Space:** O(1)

---

### Pattern 4: Hash Table Lookup

**When to use:** Need O(1) lookups, counting, finding pairs/complements

**Common problems:**
- Two Sum (unsorted)
- Group anagrams
- First non-repeating character
- Subarray sum equals k

**Example from this course:**
- Hash Tables: Problem 1, Problem 2, Problem 3

**Template:**
```python
def hash_lookup(arr):
    seen = {}  # or set()
    
    for element in arr:
        if complement in seen:
            return found_solution
        
        seen[element] = value
```

**Time:** O(n) | **Space:** O(n)

---

### Pattern 5: Stack for Parsing

**When to use:** Nested structures, matching pairs, parsing expressions

**Common problems:**
- Valid parentheses
- Evaluate reverse polish notation
- Daily temperatures
- Largest rectangle in histogram

**Example from this course:**
- Stacks: Problem 1, Problem 2, Problem 4

**Template:**
```python
def stack_parsing(s):
    stack = []
    
    for char in s:
        if is_opening(char):
            stack.append(char)
        elif is_closing(char):
            if not stack or not matches(stack[-1], char):
                return False
            stack.pop()
    
    return len(stack) == 0
```

**Time:** O(n) | **Space:** O(n)

---

### Pattern 6: BFS (Level Order)

**When to use:** Shortest path, level-by-level traversal

**Common problems:**
- Binary tree level order traversal
- Shortest path in unweighted graph
- Minimum depth of binary tree
- Rotting oranges

**Example from this course:**
- Trees: Problem 4
- Graphs: Problem 1, Problem 2

**Template:**
```python
from collections import deque

def bfs(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            # Process node
            
            # Add children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

**Time:** O(n) | **Space:** O(w) where w is max width

---

### Pattern 7: DFS (Recursive)

**When to use:** Tree traversal, backtracking, exploring all paths

**Common problems:**
- All paths from source to target
- Generate parentheses
- Word search
- Validate BST

**Example from this course:**
- Trees: Problem 1, Problem 2
- Graphs: Problem 3

**Template:**
```python
def dfs(node, path, result):
    if not node:
        return
    
    # Process current node
    path.append(node.val)
    
    # Base case
    if is_leaf(node):
        result.append(path[:])
    
    # Recursive case
    dfs(node.left, path, result)
    dfs(node.right, path, result)
    
    # Backtrack
    path.pop()
```

**Time:** O(n) | **Space:** O(h) where h is height

---

### Pattern 8: Binary Search

**When to use:** Sorted data, finding boundaries, optimization problems

**Common problems:**
- Search in rotated sorted array
- Find first and last position
- Search in 2D matrix
- Minimum in rotated sorted array

**Example from this course:**
- Searching: Problem 2, Problem 3

**Template:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

**Time:** O(log n) | **Space:** O(1)

---

### Pattern 9: Modified Binary Search

**When to use:** Search space reduction, finding min/max with constraints

**Common problems:**
- Capacity to ship packages within D days
- Koko eating bananas
- Minimum number of days to make m bouquets
- Split array largest sum

**Template:**
```python
def binary_search_on_answer(arr):
    left, right = min_possible, max_possible
    result = right
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if is_feasible(mid):
            result = mid
            right = mid - 1  # Try smaller
        else:
            left = mid + 1   # Need larger
    
    return result
```

**Time:** O(n log m) where m is search space | **Space:** O(1)

---

### Pattern 10: Merge Intervals

**When to use:** Overlapping ranges, scheduling problems

**Common problems:**
- Merge intervals
- Insert interval
- Meeting rooms
- Minimum number of arrows to burst balloons

**Template:**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:
            # Overlapping, merge
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    
    return merged
```

**Time:** O(n log n) | **Space:** O(n)

---

## 💡 Interview Tips and Strategies

### Before the Interview

**1-2 Weeks Before:**
- [ ] Review all data structures in this course
- [ ] Practice 20-30 problems covering all patterns
- [ ] Do 2-3 mock interviews
- [ ] Review complexity analysis

**1-2 Days Before:**
- [ ] Review pattern templates
- [ ] Skim through [COMPLEXITY_CHEATSHEET.md](./COMPLEXITY_CHEATSHEET.md)
- [ ] Get good sleep
- [ ] Prepare questions to ask interviewer

**Day of Interview:**
- [ ] Test your equipment (if remote)
- [ ] Have paper and pen ready
- [ ] Arrive 10 minutes early
- [ ] Stay calm and positive

---

### During the Interview: Step-by-Step Process

**Step 1: Understand the Problem (5 minutes)**

✅ DO:
- Read/listen to problem carefully
- Ask clarifying questions
- Confirm input/output format
- Discuss edge cases
- Write down examples

❌ DON'T:
- Jump straight to coding
- Make assumptions without confirming
- Stay silent

**Questions to ask:**
```
"What should I return if the input is empty?"
"Can the array contain negative numbers?"
"Should I modify the input array or create a new one?"
"What's the expected size of the input?"
"Are there any constraints on memory usage?"
```

---

**Step 2: Think Out Loud (5-10 minutes)**

✅ DO:
- Explain your thought process
- Discuss brute force approach first
- Mention time/space complexity
- Propose optimizations
- Draw diagrams if helpful

❌ DON'T:
- Think in silence for too long
- Dismiss brute force immediately
- Ignore hints from interviewer

**What to say:**
```
"The brute force approach would be to check every pair, which is O(n²)..."
"I could use a hash table to improve this to O(n)..."
"Let me draw this out to make sure I understand..."
"I'm thinking this looks like a two-pointer problem..."
```

---

**Step 3: Write Code (15-20 minutes)**

✅ DO:
- Start with function signature
- Write clean, readable code
- Use meaningful variable names
- Handle edge cases
- Add comments for complex logic

❌ DON'T:
- Worry about perfect syntax
- Spend too long on one approach
- Get stuck in implementation details

**Code structure:**
```python
def solve_problem(input_data):
    """
    Brief description of approach
    Time: O(?)
    Space: O(?)
    """
    # Handle edge cases
    if not input_data:
        return default_value
    
    # Initialize variables
    
    # Main logic
    
    # Return result
```

---

**Step 4: Test Your Solution (5 minutes)**

✅ DO:
- Walk through with example
- Test edge cases
- Check for off-by-one errors
- Verify return value

❌ DON'T:
- Assume code is perfect
- Skip testing
- Ignore obvious bugs

**Edge cases to consider:**
```
- Empty input
- Single element
- All same elements
- Minimum/maximum values
- Negative numbers (if applicable)
- Duplicates
```

---

**Step 5: Optimize (if time permits)**

✅ DO:
- Discuss time/space trade-offs
- Mention alternative approaches
- Explain why current solution is good

❌ DON'T:
- Completely rewrite without discussing
- Over-optimize unnecessarily

---

### Communication Tips

**Think Out Loud:**
```
BAD:  [Silence for 5 minutes] "I think I have it..."

GOOD: "I'm considering a hash table approach. I'd store each 
       element as I iterate, checking if its complement exists.
       This would give me O(n) time with O(n) space..."
```

**When Stuck:**
```
BAD:  [More silence] "I don't know..."

GOOD: "I'm stuck on this part. I think the issue is [explain].
       Could you give me a hint about [specific aspect]?"
```

**Receiving Hints:**
```
BAD:  "Okay" [continues without acknowledgment]

GOOD: "That's a great hint! So if I use a hash table here,
       I could... [explain how you'll apply the hint]"
```

---

### Common Mistakes to Avoid

**❌ Mistake 1: Going Silent**
- Interviewers can't read your mind
- They want to see your thought process
- Solution: Narrate your thinking

**❌ Mistake 2: Jumping to Code Too Fast**
- Leads to wrong approach
- Harder to change direction later
- Solution: Discuss approach first, get agreement

**❌ Mistake 3: Ignoring Edge Cases**
- Shows lack of attention to detail
- Can fail test cases
- Solution: Always ask about edge cases upfront

**❌ Mistake 4: Not Testing Code**
- Bugs are obvious to interviewer
- Shows lack of care
- Solution: Always walk through an example

**❌ Mistake 5: Giving Up Too Easily**
- Missing opportunity to show problem-solving
- Solution: Ask for hints, try simpler version

**❌ Mistake 6: Being Defensive**
- When interviewer points out issues
- Solution: Say "Good catch!" and fix it

**❌ Mistake 7: Overcomplicating**
- Trying to be too clever
- Solution: Start simple, optimize later

---

## 🗺️ Practice Problem Roadmap

A structured 4-week plan to prepare for interviews.

### Week 1: Arrays and Hash Tables (Patterns 1, 2, 4)

**This Course:**
- Arrays: Problems 1, 2, 4, 6
- Hash Tables: Problems 1, 2, 3

**LeetCode Problems (in order):**
1. Two Sum (Easy) - Hash table pattern
2. Valid Anagram (Easy) - Hash table
3. Contains Duplicate (Easy) - Hash table
4. Maximum Subarray (Easy) - Sliding window
5. Best Time to Buy and Sell Stock (Easy) - Two pointers
6. Container With Most Water (Medium) - Two pointers
7. 3Sum (Medium) - Two pointers + hash
8. Longest Substring Without Repeating Characters (Medium) - Sliding window
9. Product of Array Except Self (Medium) - Array manipulation
10. Subarray Sum Equals K (Medium) - Hash table + prefix sum

**Daily Practice:** 2-3 problems, 1-2 hours

---

### Week 2: Linked Lists and Stacks (Patterns 3, 5)

**This Course:**
- Linked Lists: Problems 1, 2, 3, 5
- Stacks: Problems 1, 2, 4

**LeetCode Problems:**
1. Reverse Linked List (Easy) - Fundamental
2. Merge Two Sorted Lists (Easy) - Two pointers
3. Linked List Cycle (Easy) - Fast/slow pointers
4. Valid Parentheses (Easy) - Stack
5. Middle of Linked List (Easy) - Fast/slow
6. Remove Nth Node From End (Medium) - Two pointers
7. Add Two Numbers (Medium) - Linked list
8. Reorder List (Medium) - Multiple techniques
9. Min Stack (Medium) - Stack design
10. Daily Temperatures (Medium) - Monotonic stack

**Daily Practice:** 2-3 problems, 1-2 hours

---

### Week 3: Trees and Graphs (Patterns 6, 7)

**This Course:**
- Trees: Problems 1, 2, 4, 5
- Binary Search Trees: Problems 1, 2, 3
- Graphs: Problems 1, 2, 3

**LeetCode Problems:**
1. Maximum Depth of Binary Tree (Easy) - DFS
2. Invert Binary Tree (Easy) - DFS/BFS
3. Same Tree (Easy) - DFS
4. Binary Tree Level Order Traversal (Medium) - BFS
5. Validate Binary Search Tree (Medium) - DFS
6. Lowest Common Ancestor of BST (Medium) - BST property
7. Number of Islands (Medium) - Graph DFS/BFS
8. Clone Graph (Medium) - Graph traversal
9. Course Schedule (Medium) - Topological sort
10. Binary Tree Right Side View (Medium) - BFS/DFS

**Daily Practice:** 2-3 problems, 1-2 hours

---

### Week 4: Advanced Patterns and Review (Patterns 8, 9, 10)

**This Course:**
- Searching: Problems 2, 3
- Sorting: Problems 1, 4, 5

**LeetCode Problems:**
1. Binary Search (Easy) - Pattern 8
2. First Bad Version (Easy) - Binary search variation
3. Search in Rotated Sorted Array (Medium) - Modified binary search
4. Merge Intervals (Medium) - Pattern 10
5. Kth Largest Element (Medium) - Heap/quickselect
6. Top K Frequent Elements (Medium) - Hash + heap
7. Meeting Rooms II (Medium) - Intervals + heap
8. Find Minimum in Rotated Sorted Array (Medium) - Binary search
9. Time Based Key-Value Store (Medium) - Binary search
10. Insert Interval (Medium) - Intervals

**Daily Practice:** 2-3 problems, 1-2 hours

**Plus:** Do 2-3 full mock interviews this week!

---

## 📚 Module-Specific Interview Problems

The most interview-relevant problems from each module in this course.

### Module 0: Foundations
**Key concepts for interviews:**
- Big O analysis (CRITICAL - will be asked)
- Space vs time trade-offs
- Problem-solving approach

**Interview relevance:** ⭐⭐⭐⭐⭐
**Time investment:** Review Big O thoroughly

---

### Module 1: Arrays ⭐⭐⭐⭐⭐

**Interview frequency:** Very High  
**Must-do problems from this module:**
- Problem 1: Basic array operations (warm-up)
- Problem 2: Two-pointer technique (very common)
- Problem 4: Sliding window (common)
- Problem 6: Array manipulation (optimization)

**Interview questions you can solve after:**
- Two Sum / Three Sum
- Maximum subarray
- Product of array except self
- Container with most water
- Trapping rain water

**Why important:** Arrays are in 60%+ of interviews

---

### Module 2: Linked Lists ⭐⭐⭐⭐

**Interview frequency:** High  
**Must-do problems from this module:**
- Problem 1: Traversal basics
- Problem 2: Insertion/deletion
- Problem 3: Fast/slow pointers (VERY COMMON)
- Problem 5: Reversal (VERY COMMON)

**Interview questions you can solve after:**
- Reverse linked list
- Detect cycle
- Find middle
- Merge two sorted lists
- Remove nth node from end

**Why important:** Tests pointer manipulation skills

---

### Module 3: Stacks ⭐⭐⭐⭐

**Interview frequency:** High  
**Must-do problems from this module:**
- Problem 1: Valid parentheses (CLASSIC)
- Problem 2: Evaluate expression
- Problem 4: Monotonic stack pattern

**Interview questions you can solve after:**
- Valid parentheses
- Min stack
- Daily temperatures
- Largest rectangle in histogram
- Evaluate reverse Polish notation

**Why important:** Many parsing and bracket problems

---

### Module 4: Queues ⭐⭐⭐

**Interview frequency:** Medium  
**Must-do problems from this module:**
- Problem 1: Queue basics
- Problem 3: Deque applications
- Problem 5: Priority queue

**Interview questions you can solve after:**
- Implement queue using stacks
- Design circular queue
- Sliding window maximum
- Task scheduler

**Why important:** Foundation for BFS and system design

---

### Module 5: Hash Tables ⭐⭐⭐⭐⭐

**Interview frequency:** Very High  
**Must-do problems from this module:**
- Problem 1: Two Sum pattern (CRITICAL)
- Problem 2: Frequency counting
- Problem 3: Grouping/categorizing
- Problem 5: Hash set applications

**Interview questions you can solve after:**
- Two Sum
- Group anagrams
- First non-repeating character
- Longest substring without repeating chars
- Subarray sum equals k

**Why important:** Optimization technique for many problems

---

### Module 6: Trees ⭐⭐⭐⭐

**Interview frequency:** High  
**Must-do problems from this module:**
- Problem 1: Tree traversals (FUNDAMENTAL)
- Problem 2: Recursion on trees
- Problem 4: Level order (BFS)
- Problem 5: Path problems

**Interview questions you can solve after:**
- Maximum depth
- Invert binary tree
- Level order traversal
- Path sum
- Lowest common ancestor

**Why important:** Tests recursion and problem decomposition

---

### Module 7: Binary Search Trees ⭐⭐⭐

**Interview frequency:** Medium-High  
**Must-do problems from this module:**
- Problem 1: BST validation (COMMON)
- Problem 2: BST search
- Problem 3: BST insertion
- Problem 6: BST successor/predecessor

**Interview questions you can solve after:**
- Validate BST
- Kth smallest element
- Lowest common ancestor in BST
- Convert sorted array to BST

**Why important:** Understanding ordered structures

---

### Module 8: Graphs ⭐⭐⭐⭐

**Interview frequency:** High (especially for senior roles)  
**Must-do problems from this module:**
- Problem 1: Graph representation
- Problem 2: BFS (CRITICAL)
- Problem 3: DFS (CRITICAL)
- Problem 5: Shortest path (if included)

**Interview questions you can solve after:**
- Number of islands
- Clone graph
- Course schedule
- Word ladder
- Pacific Atlantic water flow

**Why important:** Complex problems, shows advanced thinking

---

### Module 9: Searching Algorithms ⭐⭐⭐⭐

**Interview frequency:** High  
**Must-do problems from this module:**
- Problem 2: Binary search (FUNDAMENTAL)
- Problem 3: Modified binary search

**Interview questions you can solve after:**
- Binary search
- Search in rotated array
- Find first and last position
- Search in 2D matrix
- Find peak element

**Why important:** Optimization technique, O(log n) is powerful

---

### Module 10: Sorting Algorithms ⭐⭐⭐

**Interview frequency:** Medium  
**Must-do problems from this module:**
- Problem 1: Understanding different sorts
- Problem 4: Merge sort implementation
- Problem 5: Quick sort implementation

**Interview questions you can solve after:**
- Sort colors (Dutch flag)
- Merge intervals
- Largest number
- Sort list (linked list)

**Why important:** Understanding complexity, custom sorting

---

## 🏢 Company-Specific Preparation

### FAANG Companies

**Google** (Difficult, algorithmic focus)
- Emphasis on optimization
- Expect follow-up questions
- Strong CS fundamentals required
- **Focus:** All patterns, especially graphs and trees
- **Resources:** LeetCode Google tag

**Meta/Facebook** (Difficult, broad)
- Mix of easy and hard problems
- System design for senior roles
- **Focus:** Hash tables, graphs, dynamic programming
- **Resources:** LeetCode Facebook tag

**Amazon** (Medium difficulty, leadership principles)
- Often uses real scenarios
- Leadership questions too
- **Focus:** Arrays, trees, graphs, OOP
- **Resources:** LeetCode Amazon tag, Amazon's 14 leadership principles

**Apple** (Medium difficulty, practical)
- Focus on practical problems
- System design and architecture
- **Focus:** Arrays, strings, design problems
- **Resources:** LeetCode Apple tag

**Netflix** (Difficult, varied)
- Fewer interviews but very selective
- Senior level emphasis
- **Focus:** System design, algorithms, architecture
- **Resources:** Practice complex problems

**Microsoft** (Medium difficulty, balanced)
- Covers broad range of topics
- Some design questions
- **Focus:** Arrays, strings, trees, OOP design
- **Resources:** LeetCode Microsoft tag

### Tech Unicorns

**Stripe, Airbnb, Uber, etc.**
- Similar to FAANG but perhaps slightly easier
- Emphasize product thinking
- **Focus:** Core patterns, clean code, communication

### Startups

**Early-stage (< 50 people)**
- Often less rigorous algorithms
- More focus on practical skills
- **Focus:** Can you build things? General problem-solving

**Growth-stage (50-500 people)**
- Starting to standardize interviews
- Mix of practical and algorithmic
- **Focus:** Core patterns, especially arrays and hash tables

---

## 🎤 Mock Interview Guide

### Why Mock Interviews?

- Practice communication under pressure
- Get used to thinking out loud
- Receive feedback on weak areas
- Build confidence
- Reduce anxiety

### How to Do Mock Interviews

**Option 1: Peer Mock Interviews**

1. Find a partner (friend, classmate, online community)
2. Take turns being interviewer/interviewee
3. Use timer (45 minutes total)
4. Give honest feedback

**Option 2: Use Pramp (Free)**
- [Pramp.com](https://www.pramp.com)
- Peer-to-peer interviews
- Structured format
- Both sides get practice

**Option 3: Paid Services**
- interviewing.io (with engineers from top companies)
- Technical Mock Interview (varies)
- Worth it if you can afford

### Mock Interview Format

**Recommended schedule (45 minutes):**
- 0-5 min: Introduction and problem presentation
- 5-10 min: Clarifying questions and approach discussion
- 10-30 min: Coding
- 30-35 min: Testing and refinement
- 35-40 min: Discussion of complexity and improvements
- 40-45 min: Feedback session

### Being a Good Interviewer

If you're practicing with a peer:

**DO:**
- Give problem clearly
- Answer clarifying questions
- Give hints if stuck > 5 minutes
- Provide constructive feedback
- Time the interview

**DON'T:**
- Give away the answer
- Be overly critical
- Let them stay stuck too long
- Skip the feedback

### Being a Good Interviewee

**DO:**
- Think out loud constantly
- Ask questions
- Test your code
- Be open to feedback

**DON'T:**
- Go silent
- Give up easily
- Get defensive about mistakes

---

## ✅ Pre-Interview Checklist

**One Day Before:**
- [ ] Review pattern templates
- [ ] Skim complexity cheat sheet
- [ ] Run through 1-2 easy problems
- [ ] Prepare questions to ask interviewer
- [ ] Get good sleep

**Day Of:**
- [ ] Eat a good meal
- [ ] Test equipment (if remote)
- [ ] Have paper/pen ready
- [ ] Set up quiet environment
- [ ] Join 5-10 minutes early
- [ ] Take deep breaths, stay positive

**During Interview:**
- [ ] Listen carefully to problem
- [ ] Ask clarifying questions
- [ ] Discuss approach before coding
- [ ] Think out loud
- [ ] Write clean code
- [ ] Test with examples
- [ ] Analyze complexity
- [ ] Ask thoughtful questions at end

**After Interview:**
- [ ] Write down problems and solutions
- [ ] Note what went well
- [ ] Note what to improve
- [ ] Review any mistakes
- [ ] Don't overthink it!

---

## 📈 Progress Tracking

Track your preparation with this checklist:

### Foundations
- [ ] Can explain Big O notation clearly
- [ ] Can analyze time and space complexity
- [ ] Understand when to trade time for space

### Pattern Mastery
- [ ] Two Pointers (solved 5+ problems)
- [ ] Sliding Window (solved 5+ problems)
- [ ] Fast/Slow Pointers (solved 3+ problems)
- [ ] Hash Table Lookup (solved 10+ problems)
- [ ] Stack for Parsing (solved 5+ problems)
- [ ] BFS (solved 5+ problems)
- [ ] DFS (solved 5+ problems)
- [ ] Binary Search (solved 5+ problems)
- [ ] Modified Binary Search (solved 3+ problems)
- [ ] Merge Intervals (solved 3+ problems)

### Data Structures
- [ ] Arrays (completed module)
- [ ] Linked Lists (completed module)
- [ ] Stacks (completed module)
- [ ] Queues (completed module)
- [ ] Hash Tables (completed module)
- [ ] Trees (completed module)
- [ ] BST (completed module)
- [ ] Graphs (completed module)

### Practice Milestones
- [ ] Solved 50+ total problems
- [ ] Solved 20+ medium problems
- [ ] Solved 5+ hard problems
- [ ] Completed 3+ mock interviews
- [ ] Can solve easy problem in < 20 minutes
- [ ] Can solve medium problem in < 40 minutes

### Interview Skills
- [ ] Comfortable thinking out loud
- [ ] Can explain approach before coding
- [ ] Test code systematically
- [ ] Handle hints gracefully
- [ ] Discuss time/space complexity
- [ ] Ask good clarifying questions

---

## 💪 Final Tips

### The Night Before
- Review patterns, NOT new problems
- Get good sleep (seriously)
- Prepare your questions
- Set up your environment
- Stay confident

### Morning Of
- Light exercise to calm nerves
- Healthy breakfast
- Review one simple problem to warm up
- No cramming new material

### Remember
- **You don't need to be perfect** - Making mistakes is okay
- **Communication matters** - Talking through it is half the battle
- **Hints are fine** - All interviewers expect to give hints
- **Enjoy it** - This is a learning experience
- **You got this!** - You've prepared well

---

## 🔗 Related Resources

- [README.md](./README.md) - Course overview
- [LEARNING_PATH.md](./LEARNING_PATH.md) - Learning paths
- [RESOURCES.md](./RESOURCES.md) - External resources and platforms
- [COMPLEXITY_CHEATSHEET.md](./COMPLEXITY_CHEATSHEET.md) - Quick complexity reference
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Contribute to this course

---

**Good luck with your interviews! Remember: Preparation meets opportunity. You've done the preparation, now go get that opportunity! 🚀**
