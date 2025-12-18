# Repository Structure

This repository is organized to provide a clear learning path through data structures and algorithms.

## Directory Organization

Each topic has its own directory with practice problems organized into subdirectories:

```
repository-root/
├── arrays/
│   ├── README.md
│   ├── problem-1/
│   │   ├── problem1.md          # Problem description
│   │   ├── problem1.py          # Python starter file
│   │   ├── test_problem1.py     # Test file
│   │   └── __init__.py
│   ├── problem-2/
│   │   ├── problem2.md
│   │   ├── problem2.py
│   │   ├── test_problem2.py
│   │   └── __init__.py
│   └── ... (6 problems total)
├── stacks/
├── linked-lists/
├── queues/
├── hash-tables/
├── trees/
├── binary-search-trees/
├── graphs/
├── sorting-algorithms/
├── searching-algorithms/
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore patterns
└── CONTRIBUTING.md         # Contribution guidelines
```

## Total Content

- **10 Topics**: arrays, stacks, linked-lists, queues, hash-tables, trees, binary-search-trees, graphs, sorting-algorithms, searching-algorithms
- **60 Problems**: 6 problems per topic
- **180 Files**: Each problem has 3 files (markdown, python, test)

## File Naming Convention

- Problem directories: `problem-N` (where N is 1-6)
- Markdown files: `problemN.md`
- Python starter files: `problemN.py`
- Test files: `test_problemN.py`

## Running Tests

From within a problem directory:
```bash
cd arrays/problem-1
pytest test_problem1.py -v
```

From repository root for a specific problem:
```bash
pytest arrays/problem-1/ -v
```

## For Students

1. Navigate to a topic (e.g., `arrays/`)
2. Read the `README.md` for an overview of the topic
3. Choose a problem directory (e.g., `problem-1/`)
4. Read the problem description in `problemN.md`
5. Download and edit `problemN.py` to implement your solution
6. Run `pytest test_problemN.py` to validate your solution

## For Contributors

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines on adding new problems or improving existing content.
