
---

# Arrays in Data Structures

## Table of Contents

- [What is an Array?](#what-is-an-array)
- [Types of Arrays](#types-of-arrays)
  - [One-dimensional Arrays](#one-dimensional-arrays)
  - [Multi-dimensional Arrays](#multi-dimensional-arrays)
- [Big O Analysis of Arrays](#big-o-analysis-of-arrays)
  - [Time Complexity](#time-complexity)
  - [Space Complexity](#space-complexity)
- [Static vs. Dynamic Arrays](#static-vs-dynamic-arrays)
  - [Static Arrays](#static-arrays)
  - [Dynamic Arrays](#dynamic-arrays)

## What is an Array?

An array is a data structure that stores a fixed-size sequential collection of elements of the same type. Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

Arrays are commonly used because they are easy to implement and efficient for accessing and modifying elements.

## Types of Arrays

### One-dimensional Arrays

A one-dimensional array is a simple list of elements where each element can be accessed by a single index. For example:

```python
arr = [1, 2, 3, 4, 5]
```

### Multi-dimensional Arrays

A multi-dimensional array is an array of arrays, where each element is itself an array. The most common form is a two-dimensional array (matrix), but arrays can have more dimensions. For example, a 2D array can be represented as:

```python
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## Big O Analysis of Arrays

### Time Complexity

- **Access**: O(1) - Direct access to any element in the array by its index.

  **Example**: 
  ```python
  arr = [10, 20, 30, 40, 50]
  print(arr[2])  # O(1) - Accessing the third element directly (Output: 30)
  ```

- **Search**: O(n) - In the worst case, you may need to search through the entire array.

  **Example**:
  ```python
  arr = [10, 20, 30, 40, 50]
  target = 40
  for i in arr:
      if i == target:
          print("Found!")  # O(n) - May need to check each element until the target is found
  ```

- **Insertion**:
  - **At the end**: O(1) if the array has space; O(n) if resizing is needed.
  
    **Example** (Dynamic Array):
    ```python
    arr = [1, 2, 3, 4]
    arr.append(5)  # O(1) - Fast unless the array resizes (Output: [1, 2, 3, 4, 5])
    ```

  - **At the beginning or middle**: O(n) due to the need to shift elements.
  
    **Example**:
    ```python
    arr = [10, 20, 30, 40, 50]
    arr.insert(2, 25)  # O(n) - Elements after index 2 need to be shifted (Output: [10, 20, 25, 30, 40, 50])
    ```

- **Deletion**:
  - **At the end**: O(1) - Removing the last element is efficient.
  
    **Example**:
    ```python
    arr = [10, 20, 30, 40, 50]
    arr.pop()  # O(1) - Removing the last element (Output: [10, 20, 30, 40])
    ```

  - **At the beginning or middle**: O(n) due to shifting elements.
  
    **Example**:
    ```python
    arr = [10, 20, 30, 40, 50]
    arr.pop(2)  # O(n) - Elements after index 2 need to be shifted left (Output: [10, 20, 40, 50])
    ```

### Space Complexity

- **Static Array**: O(n) - Space is allocated based on the defined size of the array.

  **Example** (Simulated Static Array):
  ```python
  arr = [0] * 100  # O(n) - Allocates space for 100 elements, all initialized to 0
  ```

- **Dynamic Array**: O(n) - Space is allocated dynamically, and may involve resizing.

  **Example** (Dynamic Array):
  ```python
  arr = []
  for i in range(100):
      arr.append(i)  # O(n) - The array grows dynamically as elements are added
  ```

## Static vs. Dynamic Arrays

### Static Arrays

A static array has a fixed size, meaning the size of the array is determined at the time of its creation and cannot be changed. These arrays are allocated in contiguous memory locations, making them fast for indexing but less flexible when the size needs to be adjusted.

**Advantages:**
- Simple and fast access to elements.
- No overhead for resizing the array.

**Disadvantages:**
- Inflexible size; can't adjust if you need more or less space.
- Memory waste if the array is underutilized.

**Example** (Simulating Static Array in Python):
```python
arr = [0] * 5  # Static array with fixed size 5
arr[0] = 1
arr[1] = 2
arr[2] = 3
arr[3] = 4
arr[4] = 5
print(arr)  # Output: [1, 2, 3, 4, 5]
```

### Dynamic Arrays

A dynamic array allows for resizing as elements are added or removed. It starts with an initial capacity, and if that capacity is exceeded, the array creates a larger array, copies the elements, and then adds the new element.

**Advantages:**
- Flexible size, which can grow or shrink as needed.
- Better memory utilization as the array grows dynamically.

**Disadvantages:**
- Slower insertion due to the possibility of resizing.
- Overhead of copying elements during resizing.

**Example**:
```python
arr = []
arr.append(10)  # Dynamic array, adds element 10
arr.append(20)  # Automatically resizes if necessary
arr.append(30)
print(arr)  # Output: [10, 20, 30]
```

---
