# Contributing to Intro to Data Structures and Algorithms

Thank you for your interest in contributing to this educational repository! We believe that diverse perspectives and approaches make learning better for everyone. Whether you're a student, educator, or developer, your contributions are welcome and valued!

## 🎯 Ways to Contribute

We encourage contributions in these areas:

### 1. 💡 Alternative Solution Approaches
- **Different algorithms:** Share alternative ways to solve the same problem
- **Different languages:** Implement solutions in other programming languages
- **Optimization:** Provide more efficient solutions with analysis
- **Trade-offs:** Explain when one approach is better than another

### 2. 📝 Additional Practice Problems
- **New problems:** Create problems that reinforce existing concepts
- **Real-world scenarios:** Add problems based on practical applications
- **Difficulty variations:** Easy/medium/hard versions of similar problems
- **Edge case focused:** Problems that highlight important corner cases

### 3. 📚 Better Explanations and Analogies
- **Clearer explanations:** Simplify complex concepts
- **Visual aids:** Add ASCII diagrams, drawings, or flowcharts
- **Real-world analogies:** Connect abstract concepts to everyday examples
- **Step-by-step walkthroughs:** Break down solutions into digestible steps
- **Common pitfalls:** Document mistakes learners often make

### 4. 🎨 Visualization Improvements
- **Interactive demos:** Links to visualizations or animations
- **Step-by-step execution:** Show how algorithms work with examples
- **Before/after comparisons:** Visual representations of transformations
- **Complexity graphs:** Visual comparison of different approaches

### 5. 🐛 Bug Fixes and Improvements
- **Fix typos or errors** in documentation
- **Improve test cases** for better coverage
- **Update outdated information**
- **Enhance code readability**

### 6. 📖 Documentation Enhancements
- **Expand READMEs** with more examples
- **Add FAQs** for common questions
- **Create study guides** for specific topics
- **Improve navigation** between related topics

---

## 🚀 Getting Started

### For First-Time Contributors

**Never contributed to open source before?** No problem! Here's how to get started:

1. **Browse the repository** and familiarize yourself with the structure
2. **Look for issues** labeled `good-first-issue` or `help-wanted`
3. **Read this guide** completely before making changes
4. **Start small** - even fixing a typo is a valuable contribution!
5. **Ask questions** if anything is unclear

### Prerequisites

- Basic understanding of Git and GitHub
- Python 3.7+ installed
- Familiarity with the topic you're contributing to
- pytest installed (`pip install pytest`)

---

## 📋 Contribution Guidelines

### Before You Start

1. **Check existing issues** to see if your idea is already being worked on
2. **Open an issue** to discuss major changes before implementing
3. **Search pull requests** to avoid duplicate work
4. **Review the code of conduct** (be respectful and constructive)

This guide will help you understand the structure and how to work with the practice problems.

## Repository Structure

Each data structure/algorithm topic is organized into its own directory with the following structure:

```
<topic>/
├── README.md                    # Lesson content and overview
├── Problem 1/
│   ├── problem1.md             # Problem description and examples
│   ├── problem1.py             # Python starter file with function stubs
│   └── test_problem1.py        # Pytest tests for validation
├── Problem 2/
│   ├── problem2.md
│   ├── problem2.py
│   └── test_problem2.py
└── ... (6 problems per topic)
```

## Working on Practice Problems

### For Students

1. **Read the problem**: Navigate to a Problem directory and open the `problemN.md` file to understand the requirements.

2. **Download the starter file**: Download the `problemN.py` file which contains:
   - Function signature with parameters
   - Docstring explaining what to implement
   - TODO comments to guide you
   - A main block for testing

3. **Implement your solution**: Write your code in the designated function.

4. **Test your solution**: Run the tests to validate your implementation:
   ```bash
   cd "<topic>/problem-N"
   python3 -m pytest test_problemN.py -v
   ```

5. **Iterate**: If tests fail, review your logic and try again!

### For Contributors

#### Adding New Problems

1. Create a new `problem-N` directory in the appropriate topic folder
2. Add three files:
   - `problemN.md`: Problem description with examples and hints
   - `problemN.py`: Starter file with function stub and comments
   - `test_problemN.py`: Test cases using pytest

#### Problem Markdown Template (`problemN.md`)

```markdown
# Problem N: [Title]

**Difficulty:** [Easy 🟢 | Medium 🟡 | Hard 🔴]

## Problem Statement

[Clear description of the problem]

### Example 1:
\```
Input: [example input]
Output: [example output]
Explanation: [optional explanation]
\```

### Example 2:
\```
Input: [example input]
Output: [example output]
\```

## Constraints

- [List any constraints or assumptions]

## Hints

<details>
<summary>Hint 1</summary>
[First hint]
</details>

<details>
<summary>Hint 2</summary>
[Second hint]
</details>

## Solution Approach

<details>
<summary>Click to reveal solution</summary>

### Algorithm

1. [Step-by-step algorithm]
2. [Continue steps]

### Python Implementation

\```python
def function_name(params):
    """
    [Docstring]
    """
    # Implementation
    pass
\```

### Time and Space Complexity

- **Time Complexity:** O(?) - [explanation]
- **Space Complexity:** O(?) - [explanation]

</details>

---

[← Back to [Topic]](../README.md)
```

#### Python Starter File Template (`problemN.py`)

```python
"""
[Problem Title]

TODO: Implement the solution for this problem.
Refer to problemN.md for problem details.
"""


def function_name(params):
    """
    [Brief description of what this function should do]
    
    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2
    
    Returns:
        Description of return value
    """
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    # Test your solution here
    # Example:
    # result = function_name(test_input)
    # print(f"Result: {result}")
    pass
```

#### Test File Template (`test_problemN.py`)

```python
"""
Tests for [Problem Title]
"""
import pytest
from problemN import function_name


def test_function_name_basic():
    """Test basic functionality"""
    # Test case 1
    assert function_name(input1) == expected1
    
    # Test case 2
    assert function_name(input2) == expected2


def test_function_name_edge_cases():
    """Test edge cases"""
    # Edge case 1
    assert function_name(edge_input1) == edge_expected1
    
    # Edge case 2
    assert function_name(edge_input2) == edge_expected2


def test_function_name_errors():
    """Test error handling"""
    with pytest.raises(ValueError):
        function_name(invalid_input)
```

## Running Tests

### Run tests for a specific problem:
```bash
cd "<topic>/problem-N"
python3 -m pytest test_problemN.py -v
```

### Note on running tests:
Always use `python3 -m pytest` (not just `pytest`) to ensure Python can properly resolve the local module imports. Tests should be run from within each problem directory.

## Dependencies

This project uses:
- **Python 3.7+**
- **pytest** for testing

Install dependencies:
```bash
pip install -r requirements.txt
```

## Code Style Guidelines

- Use clear, descriptive variable names
- Add comments for complex logic
- Include docstrings for all functions
- Follow PEP 8 style guidelines
- Keep functions focused and single-purpose

---

## 💡 Contribution Ideas

Not sure where to start? Here are some ideas:

### Beginner-Friendly Contributions

- **Fix typos** in any markdown file
- **Add examples** to existing problem descriptions
- **Write test cases** for edge cases
- **Improve comments** in code
- **Add links** to helpful resources

### Intermediate Contributions

- **Create alternative solutions** with different time/space complexity
- **Write detailed explanations** for complex problems
- **Add visualization links** for algorithms
- **Translate content** to other languages
- **Create practice problem sets** for specific interview companies

### Advanced Contributions

- **Design new problems** that teach specific patterns
- **Create interactive visualizations** or animations
- **Write comprehensive guides** (like the existing LEARNING_PATH.md)
- **Develop tools** to help learners (complexity calculators, etc.)
- **Add advanced topics** (dynamic programming, advanced graph algorithms)

---

## 🎓 Sharing Your Learning Journey

We encourage students to share their learning experiences:

### Learning Resources You Found Helpful

- Blog posts or articles that clarified concepts
- YouTube videos that explained topics well
- Online tools that helped you visualize algorithms
- Books that provided deeper understanding

**How to share:** Add them to [RESOURCES.md](./RESOURCES.md) via pull request

### Alternative Approaches You Discovered

- Different ways to solve existing problems
- More efficient solutions you came up with
- Creative applications of the concepts

**How to share:** Add as comments in solution files or create alternative solution files

### Real-World Applications You've Seen

- How you used these concepts in projects
- Industry examples of data structures in action
- Interesting case studies or articles

**How to share:** Add to module READMEs or create a new "Real-World Examples" section

---

## 🤝 Community Guidelines

### Be Respectful and Inclusive

- Welcome all skill levels and backgrounds
- Provide constructive feedback
- Be patient with beginners
- Celebrate others' contributions
- Give credit where credit is due

### Quality Standards

**Code Contributions:**
- Follow PEP 8 style guidelines for Python
- Include docstrings for functions
- Add comments for complex logic
- Write test cases for new code
- Ensure all tests pass before submitting

**Documentation Contributions:**
- Use clear, simple language
- Include examples where appropriate
- Check spelling and grammar
- Maintain consistent formatting
- Link to related sections

**Problem Contributions:**
- Provide clear problem statements
- Include multiple examples
- Specify constraints and edge cases
- Offer hints (in collapsible sections)
- Include solution with complexity analysis

---

## 📊 What Makes a Great Contribution?

### Excellent Problem Contribution Example

✅ **Good Problem:**
```markdown
# Problem: Two Sum

Given an array of integers and a target sum, find two numbers that add up to the target.

**Example 1:**
Input: arr = [2, 7, 11, 15], target = 9
Output: [0, 1] (because arr[0] + arr[1] = 9)

**Example 2:**
Input: arr = [3, 2, 4], target = 6
Output: [1, 2]

**Constraints:**
- Array has at least 2 elements
- Exactly one solution exists
- Can't use same element twice

**Hints:**
<details><summary>Hint 1</summary>
Consider what you need to find for each element.
</details>

**Solution:** [Detailed explanation with complexity analysis]
```

❌ **Poor Problem:**
```markdown
# Problem

Find two numbers that add up to target. Here's the answer: use a hash table.
```

### Excellent Explanation Example

✅ **Good Explanation:**
```markdown
## Understanding Binary Search Trees

A Binary Search Tree (BST) is like a sorted family tree where:
- Each parent has at most two children
- Left child is always smaller
- Right child is always greater

**Real-world analogy:** Think of a tournament bracket where winners (larger values) 
always move right, and losers (smaller values) go left.

**Visual Example:**
```
     10
    /  \
   5    15
  / \   / \
 3   7 12  20
```

Searching for 7: Start at 10 → Go left (7 < 10) → Go right (7 > 5) → Found!
```

❌ **Poor Explanation:**
```markdown
BST is a tree. Left is smaller, right is bigger. Here's the code: [code dump]
```

---

## 🎁 Recognition

We value and recognize our contributors!

- Contributors will be mentioned in release notes
- Significant contributions may be highlighted in README
- All contributions are tracked in GitHub's contribution graph
- Community appreciation and learning benefit

---

## ❓ Questions or Need Help?

### Questions About Contributing?

If you have questions or find issues:
1. Check existing issues in the repository
2. Read through [STRUCTURE.md](./STRUCTURE.md) for repository organization
3. Create a new issue with a clear description
4. Include relevant code snippets or error messages
5. Tag with appropriate labels (question, bug, enhancement, etc.)

### Where to Get Help

- **Issues:** For bugs, feature requests, and questions
- **Discussions:** For general questions and conversations
- **Pull Request Comments:** For feedback on specific changes

---

## 📜 Pull Request Process

1. **Fork** the repository
2. **Create a branch** with a descriptive name (e.g., `add-merge-sort-visualization`)
3. **Make your changes** following the guidelines above
4. **Test your changes** thoroughly
5. **Commit with clear messages** (e.g., "Add visualization for merge sort")
6. **Submit a pull request** with:
   - Clear title describing what you changed
   - Description of why the change is valuable
   - Reference to any related issues
   - Screenshots for visual changes

### Pull Request Template

```markdown
## Description
[Brief description of changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] New problem
- [ ] Alternative solution

## Changes Made
- [List specific changes]

## Testing Done
- [How you tested your changes]

## Related Issues
Closes #[issue-number]

## Additional Notes
[Any other context]
```

---

## 🌟 Thank You!

Every contribution, no matter how small, helps make this resource better for learners worldwide. Thank you for being part of this educational community!

## License

This project is open source and available for educational purposes.

---

**Happy contributing! Together, we're making learning data structures and algorithms accessible to everyone! 🎓✨**
