# Stack Operations Visualizations

Visual representations of stack operations and common use cases.

## Stack Concept

```
Think of a stack of plates:
          
     [Plate 4]  ← Top (Last in)
     [Plate 3]
     [Plate 2]
     [Plate 1]  ← Bottom (First in)
    ───────────
     
Can only:
- Add plate to top (PUSH)
- Remove plate from top (POP)
- Look at top plate (PEEK)

This is LIFO: Last In, First Out
```

## Push Operation - O(1)

```
Push 10:
Empty → [10]
         ↑ top

Push 20:
[10] → [20]  ← top
       [10]

Push 30:
[10] → [20]  → [30]  ← top
       [20]    [20]
       [10]    [10]

Push 40:
[10] → [20] → [30] → [40]  ← top
       [20]   [20]   [30]
       [10]   [10]   [20]
                     [10]

Each push adds to top in constant time!
```

## Pop Operation - O(1)

```
Start:
    [40]  ← top
    [30]
    [20]
    [10]

Pop (remove and return 40):
    [30]  ← top
    [20]
    [10]
    
Returns: 40

Pop (remove and return 30):
    [20]  ← top
    [10]
    
Returns: 30

Pop (remove and return 20):
    [10]  ← top
    
Returns: 20

Pop (remove and return 10):
    Empty
    
Returns: 10

Each pop removes from top in constant time!
```

## Peek Operation - O(1)

```
Stack state:
    [40]  ← top
    [30]
    [20]
    [10]

Peek():
    [40]  ← Look at this, don't remove
    [30]
    [20]
    [10]
    
Returns: 40

Stack unchanged!
    [40]  ← top
    [30]
    [20]
    [10]
```

## Implementation Using Array

```
Python List as Stack:

stack = []           # Empty: []

stack.append(10)     # Push:  [10]
stack.append(20)     # Push:  [10, 20]
stack.append(30)     # Push:  [10, 20, 30]

top = stack[-1]      # Peek:  30 (stack unchanged)

val = stack.pop()    # Pop:   [10, 20], returns 30
val = stack.pop()    # Pop:   [10], returns 20

Stack visualization:
Index:  0   1   2   
Array: [10][20][30]
                ↑
              top (stack.pop() removes from end)
```

## Implementation Using Linked List

```
Linked List Stack (push/pop at head):

Empty:
head → None

Push 10:
head → [10|null]

Push 20:
head → [20]→[10|null]

Push 30:
head → [30]→[20]→[10|null]
        ↑
       top

Pop (remove head):
head → [20]→[10|null]
        ↑
       top
Returns: 30

Push at head = O(1)
Pop from head = O(1)
Perfect for a stack!
```

## Real-World Example 1: Function Call Stack

```
Code:
def a():
    b()

def b():
    c()

def c():
    return

Execution:

Step 1: Call a()
    [a()]  ← Current function

Step 2: a() calls b()
    [b()]
    [a()]

Step 3: b() calls c()
    [c()]  ← Current function
    [b()]
    [a()]

Step 4: c() returns
    [b()]  ← Resume here
    [a()]

Step 5: b() returns
    [a()]  ← Resume here

Step 6: a() returns
    Empty

Each function call is pushed, each return is popped!
This is why infinite recursion causes "stack overflow"
```

## Real-World Example 2: Undo/Redo

```
Text Editor Actions:

Type "H":
    [Type "H"]

Type "e":
    [Type "e"]
    [Type "H"]

Type "l":
    [Type "l"]
    [Type "e"]
    [Type "H"]

Type "l":
    [Type "l"]
    [Type "l"]
    [Type "e"]
    [Type "H"]

Undo (pop):
    [Type "l"]  ← Remove this
    [Type "e"]
    [Type "H"]
    
Text: "Hel"

Undo (pop):
    [Type "e"]  ← Remove this
    [Type "H"]
    
Text: "He"

Can implement redo with second stack!
```

## Real-World Example 3: Balanced Parentheses

```
Check if "(({[]}))" is balanced:

Input: ( ( { [ ] } ) )

Process each character:

See '(':
    [(]
    
See '(':
    [(]
    [(]
    
See '{':
    [{]
    [(]
    [(]
    
See '[':
    [[]
    [{]
    [(]
    [(]
    
See ']':  ← Must match '['
    [{]  ← Pop '[', matches! ✓
    [(]
    [(]
    
See '}':  ← Must match '{'
    [(]  ← Pop '{', matches! ✓
    [(]
    
See ')':  ← Must match '('
    [(]  ← Pop '(', matches! ✓
    
See ')':  ← Must match '('
    Empty ← Pop '(', matches! ✓

Stack empty and all matched = Balanced! ✓

Example of imbalanced: "({[}])"
When we see '}', top is '[' → Mismatch! ✗
```

## Real-World Example 4: Reverse a String

```
Reverse "HELLO":

Push each character:
    [O]
    [L]
    [L]
    [E]
    [H]

Pop each character:
Pop: O
    [L]
    [L]
    [E]
    [H]

Pop: L
    [L]
    [E]
    [H]

Pop: L
    [E]
    [H]

Pop: E
    [H]

Pop: H
    Empty

Result: "OLLEH"

LIFO naturally reverses order!
```

## Real-World Example 5: Browser Back Button

```
Page Navigation:

Visit google.com:
    [google.com]

Visit facebook.com:
    [facebook.com]
    [google.com]

Visit twitter.com:
    [twitter.com]
    [facebook.com]
    [google.com]

Click Back (pop):
    [facebook.com]  ← Go here
    [google.com]
    
Now viewing: facebook.com

Click Back (pop):
    [google.com]  ← Go here
    
Now viewing: google.com

Visit reddit.com:
    [reddit.com]  ← Push new page
    [google.com]
    
Forward history cleared!
```

## Stack vs Queue Comparison

```
STACK (LIFO):
Push → [4][3][2][1] ← Pop
               ↑
            Same end

Order: 4, 3, 2, 1
(Reverse order)


QUEUE (FIFO):
Enqueue → [1][2][3][4] ← Dequeue
          ↑           ↑
        Back         Front

Order: 1, 2, 3, 4
(Same order)
```

## Expression Evaluation

```
Infix: 3 + 4 * 2
Postfix (RPN): 3 4 2 * +

Evaluate postfix using stack:

Read 3:
    [3]

Read 4:
    [4]
    [3]

Read 2:
    [2]
    [4]
    [3]

Read '*': Pop 2 and 4, compute 4*2=8, push 8
    [8]
    [3]

Read '+': Pop 8 and 3, compute 3+8=11, push 11
    [11]

Result: 11
```

## Min Stack Challenge

```
Design a stack that supports push, pop, and getMin in O(1):

Use two stacks:
Main Stack     Min Stack
                
Push 5:
[5]            [5]

Push 3:
[3]            [3]  ← New minimum
[5]            [5]

Push 7:
[7]            [3]  ← Still 3
[3]            [3]
[5]            [5]

Push 1:
[1]            [1]  ← New minimum
[7]            [3]
[3]            [3]
[5]            [5]

getMin(): Return top of min stack = 1

Pop (remove 1):
[7]            [3]  ← Min is now 3
[3]            [3]
[5]            [5]

Min stack tracks minimum at each level!
```

## Key Takeaways

**Time Complexity**:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n) - not a common stack operation

**Space Complexity**:
- O(n) where n is number of elements

**Best Used For**:
✓ Reversing things
✓ Backtracking (undo, navigation)
✓ Matching pairs (parentheses, tags)
✓ Expression evaluation
✓ Function call management

**Remember**:
LIFO = Last In, First Out
Think: Stack of plates, browser back, undo
