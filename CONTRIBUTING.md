# Contributing to Intro to Data Structures and Algorithms

Thank you for your interest in contributing to this educational repository! This guide will help you understand the structure and how to work with the practice problems.

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
   pytest test_problemN.py -v
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
pytest test_problemN.py -v
```

### Run all tests for a specific problem from repository root:
```bash
pytest <topic>/problem-N/ -v
```

### Note on running tests:
Due to Python import naming conflicts when multiple directories have files with the same names, it's recommended to run tests from within each problem directory or specify the full path to a specific problem directory.

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

## Questions or Issues?

If you have questions or find issues:
1. Check existing issues in the repository
2. Create a new issue with a clear description
3. Include relevant code snippets or error messages

## License

This project is open source and available for educational purposes.

---

Happy coding! 🎓
