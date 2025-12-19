# Module 1: Arrays - Answer Key

**Total Points:** 100

---

## Part 1: Multiple Choice Questions (40 points, 4 points each)

### Question 1: **B**
- **Answer: B) O(1) access time by index**
- Explanation: The main advantage of arrays is constant-time random access using indices.

### Question 2: **B**
- **Answer: B) 9**
- Explanation: In a zero-indexed array of size 10, indices range from 0 to 9.

### Question 3: **C**
- **Answer: C) O(n)**
- Explanation: Inserting at the beginning requires shifting all n elements to the right.

### Question 4: **B**
- **Answer: B) Contiguous memory locations**
- Explanation: Arrays store elements in consecutive memory addresses.

### Question 5: **A**
- **Answer: A) O(1)**
- Explanation: Accessing any element by index is constant time, regardless of position.

### Question 6: **C**
- **Answer: C) Random access by index**
- Explanation: Arrays excel at direct access but are slow for insertions/deletions.

### Question 7: **B**
- **Answer: B) 12**
- Explanation: 3 rows × 4 columns = 12 total elements.

### Question 8: **C**
- **Answer: C) O(n)**
- Explanation: Creating an array of size n requires O(n) space.

### Question 9: **B**
- **Answer: B) Finding pairs or processing arrays from both ends**
- Explanation: Two pointers efficiently process arrays from multiple positions simultaneously.

### Question 10: **C**
- **Answer: C) O(n)**
- Explanation: Must check all n elements to find the maximum in an unsorted array.

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11 (10 points)
**Answer:**
- What does this function do? **Calculates the product of all elements except the one at index i**
- Time Complexity: **O(n²)**
- Space Complexity: **O(n)**
- Explanation: The outer loop runs n times, and for each iteration, the inner loop also runs n times, giving O(n²). The result array uses O(n) space.

### Question 12 (10 points)
**Answer:**
- Output: **[5, 4, 3, 2, 1]**
- What does this algorithm do? **Reverses the array in-place**
- Time Complexity: **O(n)**
- Explanation: The two pointers meet in the middle after n/2 swaps, which is O(n).

### Question 13 (10 points)
**Answer:**
- Bug: **Uses assignment operator `=` instead of comparison operator `==`**
- Fixed code: `if arr[i] == target:` (line 4)
- Explanation: The single equals sign tries to assign target to arr[i], which causes a syntax error. Should use `==` for comparison.

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14 (15 points)
**Sample Answer:**
Static arrays have a fixed size determined at creation and cannot grow or shrink. Dynamic arrays (like Python lists) can resize automatically when needed. When a dynamic array reaches capacity, it typically allocates a new, larger array (often double the size), copies all elements to the new location, and frees the old array. This resizing operation is O(n) but happens infrequently, making the amortized cost of append operations O(1). Understanding this is important because it explains why appending to a list is usually fast but occasionally slow, and why dynamic arrays use more memory than their current element count suggests. This trade-off between flexibility and occasional performance hits is crucial for choosing the right data structure.

### Question 15 (15 points)
**Sample Answer:**
Yes, an array (or Python list) is excellent for this photo gallery application. Accessing images by position is O(1), which is perfect for "show image 5" operations. Adding images to the end is O(1) amortized time complexity for dynamic arrays. However, there are limitations: inserting images in the middle would be O(n) as it requires shifting elements, and deleting images (except from the end) would also be O(n). For the stated requirements, arrays are ideal. Key operations: access by index O(1), append to end O(1) amortized, insert in middle O(n), delete O(n). If users frequently reorganize photos, a linked list might be worth considering, but for position-based access and append operations, arrays are the optimal choice.

---

**End of Answer Key**
