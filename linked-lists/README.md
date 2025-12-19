# Linked Lists

## Overview
A **linked list** is a dynamic linear data structure where elements (nodes) are stored in non-contiguous memory locations, with each node containing data and a reference (pointer) to the next node. Unlike arrays with fixed contiguous memory, linked lists can grow and shrink dynamically, making insertions and deletions efficient. Think of it like a treasure hunt where each clue leads you to the next location, or a chain where each link connects to the next.

## Why It Matters
Linked lists solve real-world problems where dynamic sizing and frequent modifications are essential:

- **Music Playlist Management (Spotify, YouTube Music)**: Your playlist is a linked list where each song points to the next. Adding or removing songs is instant—no need to reorganize the entire playlist like you would with an array. The "Next Song" button simply follows the link to the next node.

- **Browser Navigation History (Chrome, Firefox)**: The forward/back buttons use a doubly linked list. Each page visited is a node pointing to both the previous and next pages. When you click back, the browser follows the "previous" pointer; clicking forward follows the "next" pointer.

- **Photo Carousel on Social Media (Instagram, Facebook)**: Swipe left/right through photos? That's a linked list! Each photo node points to the next and previous photos. The circular linked list variant allows wrapping from the last photo back to the first.

- **Undo/Redo in Text Editors (Google Docs, Microsoft Word)**: Each edit action is a node in a doubly linked list. Undo follows the "previous" pointer, redo follows the "next" pointer. Easy insertion of new actions without shifting everything.

- **Operating System Process Scheduling**: The OS maintains a linked list of running processes. Adding a new process or removing a completed one is fast—just adjust a few pointers without moving other processes in memory.

## Visual Representation
```
Singly Linked List:
┌─────┬────┐    ┌─────┬────┐    ┌─────┬────┐    ┌─────┬────┐
│  A  │  ●─┼───▶│  B  │  ●─┼───▶│  C  │  ●─┼───▶│  D  │null│
└─────┴────┘    └─────┴────┘    └─────┴────┘    └─────┴────┘
   ↑
  head
  
Data: "A"    Data: "B"    Data: "C"    Data: "D"
Next: ●      Next: ●      Next: ●      Next: null (end)

Memory Layout (Non-contiguous):
Address 1000: [A | ●→2500]         Located anywhere in RAM
Address 2500: [B | ●→1200]         Not next to each other!
Address 1200: [C | ●→3000]         Can be scattered
Address 3000: [D | null]           Order maintained by pointers

Doubly Linked List:
     ┌────┬─────┬────┐    ┌────┬─────┬────┐    ┌────┬─────┬────┐
null◀┤ ●  │  A  │  ●─┼───▶│ ●  │  B  │  ●─┼───▶│ ●  │  C  │null│
     └────┴─────┴────┘    └────┴─────┴────┘    └────┴─────┴────┘
        ↑                    ▲│
       head                  └───prev link (can go backwards)

prev: null   prev: ●       prev: ●
data: "A"    data: "B"     data: "C"
next: ●      next: ●       next: null

Circular Linked List:
┌─────┬────┐    ┌─────┬────┐    ┌─────┬────┐
│  A  │  ●─┼───▶│  B  │  ●─┼───▶│  C  │  ●─┼─┐
└─────┴────┘    └─────┴────┘    └─────┴────┘ │
   ↑                                          │
  head ◀────────────────────────────────────-─┘
  (Last node points back to first - creates cycle)

Adding a Node (middle insertion):
Before:  A → B → D
         1. Create new node C
         2. Set C.next = B.next (C points to D)
         3. Set B.next = C (B points to C)
After:   A → B → C → D
         Only 2 pointer updates! O(1) once at position

Removing a Node:
Before:  A → B → C → D
         1. Set B.next = C.next (B now points to D)
         2. C is orphaned and garbage collected
After:   A → B → D
         Only 1 pointer update! O(1) once at position
```

## Key Concepts

### 1. **Node Structure**
Each node is a container with two parts: the data and a reference (pointer) to the next node. The last node points to `null`/`None` to signify the end.

**Think Like a Programmer:** Nodes are independent objects in memory. The "linking" happens through storing memory addresses, not physical proximity.

### 2. **Head Pointer**
The head is a reference to the first node in the list. Without it, you'd lose access to the entire list! It's your entry point.

**Think Like a Programmer:** Always maintain the head pointer. Losing it means losing access to your entire list—it becomes unreachable garbage in memory.

### 3. **Dynamic Size**
Unlike arrays, linked lists don't have a fixed size. You can keep adding nodes as long as memory is available. No pre-allocation needed.

**Think Like a Programmer:** This flexibility comes at a cost—each node needs extra memory for the pointer(s), typically 4-8 bytes per node.

### 4. **Sequential Access**
To access the 5th node, you must traverse nodes 1→2→3→4→5. There's no direct "jump" like array indexing.

**Think Like a Programmer:** This makes linked lists slow for random access (O(n)) but excellent for sequential processing or when you know you'll work through elements in order.

### 5. **Efficient Insertion/Deletion**
Once you're at the right position, inserting or deleting a node is just a matter of updating 1-2 pointers—no shifting required like in arrays.

**Think Like a Programmer:** The catch is "once you're at the right position." Getting there takes O(n) time, so total insertion/deletion is O(n). But if you're already at the spot (like at the head), it's O(1)!

### 6. **Pointer Manipulation**
The real skill with linked lists is carefully updating pointers. One wrong pointer assignment can break your entire list or create a memory leak.

**Think Like a Programmer:** Always draw diagrams when working with pointers. Visualize the before and after states. Double-check pointer updates in the correct order—updating in the wrong sequence can lose references to nodes.

## How It Works

### Node and List Creation
Creating a linked list involves defining a Node class with data and next pointer, then a LinkedList class to manage operations.

**Step-by-step process:**
1. Define Node class with data and next attributes
2. Initialize LinkedList with head = None (empty list)
3. Add first node by creating it and setting head to point to it
4. Add subsequent nodes by traversing to the end and linking

### Example Walkthrough

**Scenario:** Building a collaborative playlist for a road trip

```python
# Each song is a node
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None  # Points to next song

# The playlist is a linked list
class Playlist:
    def __init__(self, name):
        self.name = name
        self.head = None  # First song
        self.size = 0
```

**Step 1: Creating an Empty Playlist (O(1))**
```python
road_trip_mix = Playlist("Summer Road Trip 2024")
# head = None (no songs yet)
```

**Step 2: Adding First Song (O(1))**
```python
# Create first song
song1 = Song("Blinding Lights", "The Weeknd")

# Make it the head
road_trip_mix.head = song1
road_trip_mix.size = 1

# Visualization:
# head → [Blinding Lights | null]
```

**Step 3: Adding Second Song at End (O(n) to find end, O(1) to insert)**
```python
song2 = Song("Levitating", "Dua Lipa")

# Must traverse to find the end
current = road_trip_mix.head
while current.next != None:  # Find last song
    current = current.next

# Now current is the last song, link it to new song
current.next = song2
road_trip_mix.size = 2

# Visualization:
# head → [Blinding Lights | ●] → [Levitating | null]
```

**Step 4: Inserting Song in Middle (O(n) to find position, O(1) to insert)**
```python
# Want to insert "Uptown Funk" between first and second song
song_insert = Song("Uptown Funk", "Bruno Mars")

# Navigate to the node before insertion point
previous = road_trip_mix.head  # Start at first song

# Set up the links (ORDER MATTERS!)
song_insert.next = previous.next  # New song points to what was second
previous.next = song_insert       # First song now points to new song
road_trip_mix.size = 3

# Visualization:
# head → [Blinding Lights | ●] → [Uptown Funk | ●] → [Levitating | null]
#
# Behind the scenes:
# Step 1: song_insert.next = previous.next
#         (Uptown Funk now points to Levitating)
# Step 2: previous.next = song_insert
#         (Blinding Lights now points to Uptown Funk)
# Result: Chain maintained, Uptown Funk inserted!
```

**Step 5: Removing a Song (O(n) to find, O(1) to delete)**
```python
# Remove "Uptown Funk" (middle song)
# Need pointer to the node BEFORE the one to delete

previous = road_trip_mix.head
current = previous.next  # Song to delete

# Bypass the node to delete
previous.next = current.next  # Link around Uptown Funk
road_trip_mix.size = 2

# current is now orphaned—Python's garbage collector will clean it up

# Visualization:
# head → [Blinding Lights | ●] → [Levitating | null]
#                                 
# Uptown Funk is gone! Previous now points directly to Levitating
```

**Step 6: Playing Through Playlist (Traversal - O(n))**
```python
def play_all():
    current = road_trip_mix.head
    position = 1
    
    while current != None:
        print(f"{position}. {current.title} by {current.artist}")
        current = current.next  # Move to next song
        position += 1

play_all()
# Output:
# 1. Blinding Lights by The Weeknd
# 2. Levitating by Dua Lipa

# Behind the scenes:
# Start at head → Print → Follow next pointer → Print → Next is null → Stop
```

**Step 7: Finding a Specific Song (Search - O(n))**
```python
def find_song(title):
    current = road_trip_mix.head
    position = 1
    
    while current != None:
        if current.title == title:
            return position
        current = current.next
        position += 1
    
    return -1  # Not found

pos = find_song("Levitating")
print(f"Found at position {pos}")  # Position 2

# Must check each node sequentially until found
```

## Python Implementation

```python
# ============================================
# NODE CLASS - Building Block of Linked List
# ============================================

class Node:
    """
    Represents a single node in a linked list.
    Contains data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data      # The value stored in this node
        self.next = None      # Reference to next node (None if last)
    
    def __repr__(self):
        """String representation for debugging"""
        return f"Node({self.data})"


# ============================================
# SINGLY LINKED LIST IMPLEMENTATION
# ============================================

class LinkedList:
    """
    A singly linked list implementation with common operations.
    Each node points to the next node in the sequence.
    """
    
    def __init__(self):
        """
        Initialize empty linked list.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None      # Reference to first node
        self.size = 0         # Track number of nodes
    
    def is_empty(self):
        """
        Check if list is empty.
        Time: O(1), Space: O(1)
        """
        return self.head is None
    
    def __len__(self):
        """
        Get number of nodes in list.
        Time: O(1) if we track size, O(n) if we count
        Space: O(1)
        """
        return self.size
    
    # =============== INSERTION OPERATIONS ===============
    
    def insert_at_head(self, data):
        """
        Insert new node at the beginning of list.
        Time Complexity: O(1) - just update pointers
        Space Complexity: O(1) - one new node
        
        Real-world: Adding most recent item to history
        """
        new_node = Node(data)
        
        # Link new node to current head
        new_node.next = self.head
        
        # Update head to point to new node
        self.head = new_node
        
        self.size += 1
        
        return self
    
    def insert_at_tail(self, data):
        """
        Insert new node at the end of list.
        Time Complexity: O(n) - must traverse to end
        Space Complexity: O(1) - one new node
        
        Real-world: Appending to the end of a playlist
        
        Note: Could optimize to O(1) by maintaining tail pointer
        """
        new_node = Node(data)
        
        # Special case: empty list
        if self.is_empty():
            self.head = new_node
            self.size += 1
            return self
        
        # Traverse to last node
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Link last node to new node
        current.next = new_node
        
        self.size += 1
        
        return self
    
    def insert_at_position(self, data, position):
        """
        Insert node at specific position (0-indexed).
        Time Complexity: O(n) - traverse to position
        Space Complexity: O(1) - one new node
        
        Think Like a Programmer: Must handle edge cases:
        - Position 0 (insert at head)
        - Position beyond list size (insert at tail)
        - Middle positions
        """
        # Validate position
        if position < 0:
            raise ValueError("Position must be non-negative")
        
        # Insert at head
        if position == 0:
            return self.insert_at_head(data)
        
        # Insert at position beyond end → insert at tail
        if position >= self.size:
            return self.insert_at_tail(data)
        
        # Insert in middle
        new_node = Node(data)
        current = self.head
        
        # Navigate to node BEFORE insertion position
        for _ in range(position - 1):
            current = current.next
        
        # Insert: new_node goes between current and current.next
        new_node.next = current.next
        current.next = new_node
        
        self.size += 1
        
        return self
    
    # =============== DELETION OPERATIONS ===============
    
    def delete_at_head(self):
        """
        Remove and return first node's data.
        Time Complexity: O(1) - just update head
        Space Complexity: O(1)
        
        Real-world: Removing most recent browser history entry
        """
        if self.is_empty():
            raise Exception("Cannot delete from empty list")
        
        # Save data to return
        data = self.head.data
        
        # Move head to next node (orphaning old head)
        self.head = self.head.next
        
        self.size -= 1
        
        return data
    
    def delete_at_tail(self):
        """
        Remove and return last node's data.
        Time Complexity: O(n) - must traverse to second-to-last
        Space Complexity: O(1)
        
        Note: Doubly linked list would make this O(1) with tail pointer
        """
        if self.is_empty():
            raise Exception("Cannot delete from empty list")
        
        # Special case: only one node
        if self.head.next is None:
            return self.delete_at_head()
        
        # Traverse to second-to-last node
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        # Save data and unlink last node
        data = current.next.data
        current.next = None
        
        self.size -= 1
        
        return data
    
    def delete_by_value(self, target):
        """
        Delete first node with matching value.
        Time Complexity: O(n) - search + delete
        Space Complexity: O(1)
        
        Returns: True if deleted, False if not found
        """
        if self.is_empty():
            return False
        
        # Special case: deleting head
        if self.head.data == target:
            self.delete_at_head()
            return True
        
        # Search for node with target value
        current = self.head
        while current.next is not None:
            if current.next.data == target:
                # Found it! Bypass this node
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False  # Not found
    
    def delete_at_position(self, position):
        """
        Delete node at specific position (0-indexed).
        Time Complexity: O(n) - traverse to position
        Space Complexity: O(1)
        """
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} out of bounds")
        
        # Delete at head
        if position == 0:
            return self.delete_at_head()
        
        # Navigate to node BEFORE deletion position
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        # Save data and bypass node
        data = current.next.data
        current.next = current.next.next
        
        self.size -= 1
        
        return data
    
    # =============== SEARCH OPERATIONS ===============
    
    def search(self, target):
        """
        Find first node with target value.
        Time Complexity: O(n) - may need to check all nodes
        Space Complexity: O(1)
        
        Returns: Index if found, -1 if not found
        """
        current = self.head
        index = 0
        
        while current is not None:
            if current.data == target:
                return index
            current = current.next
            index += 1
        
        return -1  # Not found
    
    def get_at_position(self, position):
        """
        Access node data at specific position.
        Time Complexity: O(n) - must traverse
        Space Complexity: O(1)
        
        Note: Unlike arrays, no O(1) random access!
        """
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} out of bounds")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    # =============== UTILITY OPERATIONS ===============
    
    def reverse(self):
        """
        Reverse the linked list in place.
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(1) - only three pointers
        
        Think Like a Programmer: Three pointers technique
        - prev: node before current
        - current: node being processed
        - next: node after current (saved before changing pointers)
        
        Real-world: Undo chain reversal
        """
        prev = None
        current = self.head
        
        while current is not None:
            # Save next node before we change current.next
            next_node = current.next
            
            # Reverse the pointer
            current.next = prev
            
            # Move prev and current forward
            prev = current
            current = next_node
        
        # Update head to what was the last node
        self.head = prev
        
        return self
    
    def find_middle(self):
        """
        Find middle node using fast/slow pointer technique.
        Time Complexity: O(n) - one pass
        Space Complexity: O(1) - two pointers
        
        Think Like a Programmer: "Tortoise and Hare" algorithm
        - Slow moves 1 step at a time
        - Fast moves 2 steps at a time
        - When fast reaches end, slow is at middle!
        """
        if self.is_empty():
            return None
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next        # Move 1 step
            fast = fast.next.next   # Move 2 steps
        
        return slow.data
    
    def has_cycle(self):
        """
        Detect if list has a cycle (circular reference).
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Uses Floyd's Cycle Detection (fast/slow pointers)
        If there's a cycle, fast will eventually catch up to slow
        """
        if self.is_empty():
            return False
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:  # They met → cycle exists
                return True
        
        return False  # fast reached end → no cycle
    
    def to_list(self):
        """
        Convert linked list to Python list.
        Time Complexity: O(n)
        Space Complexity: O(n) - new list created
        
        Useful for testing and visualization
        """
        result = []
        current = self.head
        
        while current is not None:
            result.append(current.data)
            current = current.next
        
        return result
    
    def __repr__(self):
        """
        String representation for printing/debugging.
        Shows: head → [data] → [data] → ... → null
        """
        if self.is_empty():
            return "LinkedList: empty"
        
        nodes = []
        current = self.head
        
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        
        return "LinkedList: " + " → ".join(nodes) + " → null"


# ============================================
# DOUBLY LINKED LIST (BONUS)
# ============================================

class DoublyNode:
    """Node with both next and previous pointers"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    Doubly linked list allows traversal in both directions.
    Useful for: browser history, music players (prev/next), undo/redo
    """
    def __init__(self):
        self.head = None
        self.tail = None  # Track both ends
        self.size = 0
    
    def insert_at_tail(self, data):
        """O(1) insertion at tail (we maintain tail pointer)"""
        new_node = DoublyNode(data)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        return self


# ============================================
# DEMONSTRATION EXAMPLES
# ============================================

def example_playlist():
    """Real-world example: Music playlist"""
    print("=== Music Playlist Example ===")
    
    playlist = LinkedList()
    
    # Add songs
    playlist.insert_at_tail("Blinding Lights - The Weeknd")
    playlist.insert_at_tail("Levitating - Dua Lipa")
    playlist.insert_at_tail("Save Your Tears - The Weeknd")
    
    print(f"Playlist: {playlist}")
    print(f"Total songs: {len(playlist)}")
    
    # Find middle song
    print(f"Middle song: {playlist.find_middle()}")
    
    # Remove a song
    playlist.delete_by_value("Levitating - Dua Lipa")
    print(f"After removing Levitating: {playlist}")
    
    return playlist

def example_browser_history():
    """Real-world example: Browser history"""
    print("\n=== Browser History ===")
    
    history = LinkedList()
    
    # Visit pages
    pages = ["google.com", "github.com", "stackoverflow.com", "python.org"]
    for page in pages:
        history.insert_at_head(page)  # Most recent at head
    
    print(f"History (most recent first): {history}")
    
    # Go back (remove most recent)
    recent = history.delete_at_head()
    print(f"Went back from: {recent}")
    print(f"Current history: {history}")
    
    return history


# ============================================
# DEMO
# ============================================
if __name__ == "__main__":
    # Create and manipulate linked list
    ll = LinkedList()
    
    # Build list: 1 → 2 → 3 → 4 → 5
    for i in range(1, 6):
        ll.insert_at_tail(i)
    
    print(f"Original: {ll}")
    
    # Insert in middle
    ll.insert_at_position(99, 2)
    print(f"After inserting 99 at position 2: {ll}")
    
    # Search
    pos = ll.search(99)
    print(f"Found 99 at index: {pos}")
    
    # Reverse
    ll.reverse()
    print(f"Reversed: {ll}")
    
    # Run real-world examples
    example_playlist()
    example_browser_history()
```

## Time and Space Complexity

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Access by index | O(n) | O(1) | Must traverse from head |
| Search | O(n) | O(1) | Must check each node |
| Insert at head | O(1) | O(1) | Just update head pointer |
| Insert at tail | O(n) | O(1) | Must traverse to end (O(1) with tail pointer) |
| Insert at position | O(n) | O(1) | Traverse + O(1) insertion |
| Delete at head | O(1) | O(1) | Just update head pointer |
| Delete at tail | O(n) | O(1) | Must find second-to-last (O(1) with tail in doubly) |
| Delete at position | O(n) | O(1) | Traverse + O(1) deletion |
| Delete by value | O(n) | O(1) | Search O(n) + delete |
| Find middle | O(n) | O(1) | Fast/slow pointer technique |
| Reverse | O(n) | O(1) | One pass with pointer manipulation |
| Detect cycle | O(n) | O(1) | Floyd's cycle detection |
| Get size | O(1) | O(1) | If maintaining size counter; O(n) if counting |

**Key Insight:** Linked lists excel at insertions/deletions once you're at the position (O(1)), but finding that position takes O(n). Arrays are opposite: O(n) for insert/delete but O(1) for access.

## When to Use

✅ **Use linked lists when:**
- You need frequent insertions/deletions, especially at beginning
- Size is unpredictable and changes often
- You don't need random access by index
- Sequential access is your primary use case
- Memory fragmentation is a concern (nodes can be anywhere in memory)
- Implementing other data structures (stacks, queues, graphs)

❌ **Don't use linked lists when:**
- You need fast random access by index (use arrays)
- Memory overhead matters (each node needs extra pointer space)
- You need cache-friendly sequential access (arrays are better)
- You frequently search for elements (arrays allow binary search if sorted)
- You need to access elements from both ends frequently without traversal (use doubly linked list or deque)

**Think Like a Programmer:** Choose linked lists for dynamic data with frequent modifications at the ends. Choose arrays for static data with frequent random access. For real-world projects, Python's `collections.deque` is often better than implementing your own linked list.

## Common Pitfalls

### 1. **Losing Reference to Head**
If you lose the head pointer, the entire list becomes inaccessible!
```python
# ❌ Wrong - loses original head
def broken_insert(ll, data):
    new_node = Node(data)
    ll.head = new_node  # Original list is now orphaned!

# ✓ Correct - preserve the chain
def correct_insert(ll, data):
    new_node = Node(data)
    new_node.next = ll.head  # Link to existing list
    ll.head = new_node       # Update head
```

**Think Like a Programmer:** Always preserve the chain before updating pointers. Draw the before/after state to visualize.

### 2. **Incorrect Pointer Update Order**
The sequence of pointer updates matters! Wrong order breaks the chain.
```python
# ❌ Wrong - loses rest of list!
def broken_insert_middle(prev_node, data):
    new_node = Node(data)
    prev_node.next = new_node  # Lost reference to what was after prev!
    new_node.next = prev_node.next  # This is now None - too late!

# ✓ Correct - save reference first
def correct_insert_middle(prev_node, data):
    new_node = Node(data)
    new_node.next = prev_node.next  # Link new to rest of list FIRST
    prev_node.next = new_node       # Then update prev to point to new
```

### 3. **Not Handling Empty List**
Many operations crash on empty lists. Always check!
```python
# ❌ Wrong - crashes on empty list
def broken_delete_tail(ll):
    current = ll.head
    while current.next.next is not None:  # Error if head is None!
        current = current.next

# ✓ Correct - handle empty case
def correct_delete_tail(ll):
    if ll.head is None:  # Check for empty
        return None
    if ll.head.next is None:  # Only one node
        data = ll.head.data
        ll.head = None
        return data
    # ... rest of logic
```

### 4. **Off-by-One in Traversal**
Common when you need the node BEFORE a target position.
```python
# When inserting at position 3, you need to navigate to position 2
# (the node BEFORE where new node goes)

# ❌ Wrong - ends up one position off
for i in range(position):  # Goes too far!
    current = current.next

# ✓ Correct - stop one before
for i in range(position - 1):  # Stops at node before insertion point
    current = current.next
```

### 5. **Modifying List While Iterating**
Changing pointers during traversal can skip nodes or infinite loop.
```python
# ❌ Wrong - skips nodes after deletion
current = ll.head
while current is not None:
    if should_delete(current.data):
        # Deleting changes structure while iterating!
        ll.delete_by_value(current.data)
    current = current.next

# ✓ Correct - collect nodes to delete, then delete
to_delete = []
current = ll.head
while current is not None:
    if should_delete(current.data):
        to_delete.append(current.data)
    current = current.next

for value in to_delete:
    ll.delete_by_value(value)
```

### 6. **Not Detecting Cycles**
In circular or corrupted lists, loops can run forever!
```python
# ❌ Dangerous - infinite loop if cycle exists
def count_nodes(ll):
    count = 0
    current = ll.head
    while current is not None:  # If cycle, this never ends!
        count += 1
        current = current.next
    return count

# ✓ Safer - detect cycles first
def safe_count_nodes(ll):
    if ll.has_cycle():
        raise Exception("Cannot count nodes in cyclic list")
    # ... then count safely
```

## Practice Problems
See the problem directories for hands-on practice with linked lists:
- [Problem 1](./problem-1/problem1.md) - Basic linked list operations
- [Problem 2](./problem-2/problem2.md) - Insertion and deletion
- [Problem 3](./problem-3/problem3.md) - Linked list reversal
- [Problem 4](./problem-4/problem4.md) - Finding middle element
- [Problem 5](./problem-5/problem5.md) - Cycle detection
- [Problem 6](./problem-6/problem6.md) - Merging linked lists

## Additional Resources
- [Visualgo: Linked List Visualization](https://visualgo.net/en/list) - Interactive linked list operations
- [Python Tutor](http://pythontutor.com/) - Step through linked list code visually
- [GeeksforGeeks: Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/) - Comprehensive linked list tutorials
- [Module 00: Foundations](../00-foundations/) - Review Big-O notation and complexity analysis
- [Arrays Module](../arrays/) - Compare with array operations and trade-offs

---

**Next Steps:** Master linked lists, then explore [Stacks](../stacks/) and [Queues](../queues/), which can be efficiently implemented using linked lists!
```

## Common Operations

### Traversal
Visit each node from head to end.

**Time Complexity: O(n)**

```python
def traverse(self):
    current = self.head
    while current:
        print(current.data)
        current = current.next
```

### Insertion at Beginning
**Time Complexity: O(1)**

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### Insertion at End
**Time Complexity: O(n)** - Must traverse to end

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node
```

### Deletion
**Time Complexity: O(n)** - Must find the node

```python
def delete_node(self, key):
    current = self.head
    
    # If head needs to be deleted
    if current and current.data == key:
        self.head = current.next
        return
    
    # Find the node to delete
    prev = None
    while current and current.data != key:
        prev = current
        current = current.next
    
    # If not found
    if not current:
        return
    
    # Unlink the node
    prev.next = current.next
```

### Search
**Time Complexity: O(n)**

```python
def search(self, key):
    current = self.head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False
```

## Linked Lists vs Arrays

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory | Contiguous | Scattered |
| Size | Fixed | Dynamic |
| Access Time | O(1) | O(n) |
| Insert at Start | O(n) | O(1) |
| Insert at End | O(1) | O(n)* |
| Memory Usage | Compact | Extra space for pointers |

\* O(1) if we keep a tail pointer

## Real-World Applications

1. **Music Playlists** - Next/previous song functionality
2. **Browser History** - Back/forward navigation
3. **Undo Functionality** - Sequence of actions
4. **Image Viewer** - Navigate through photos
5. **Blockchain** - Each block links to the next

## Common Techniques

### Two Pointer Technique
Use fast and slow pointers for problems like:
- Finding the middle of a list
- Detecting cycles
- Finding the nth node from the end

### Dummy Node
Use a dummy head node to simplify edge cases in insertion/deletion.

## Practice Problems

Each problem is organized in its own directory containing:
- `problemN.md` - Problem description and examples
- `problemN.py` - Python starter file with function stubs and comments
- `test_problemN.py` - Pytest test file for validation

Navigate to each Problem directory to access the files:

- [Problem 1](./problem-1/problem1.md)
- [Problem 2](./problem-2/problem2.md)
- [Problem 3](./problem-3/problem3.md)
- [Problem 4](./problem-4/problem4.md)
- [Problem 5](./problem-5/problem5.md)
- [Problem 6](./problem-6/problem6.md)

## Next Steps

Once you master linked lists, move on to [Stacks](../stacks/), which can be implemented using linked lists!

---

💡 **Pro Tip**: Draw pictures! Linked list problems are much easier to solve when you visualize the pointer changes on paper first.
