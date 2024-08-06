## Time Complexity and Space Complexity

### Time Complexity

**Time Complexity** is about how long an algorithm takes to run as the input size grows. We use Big O notation to describe it.

Think of it like this:

- **O(1)**: Takes the same time no matter how big the input is.
- **O(log n)**: Time grows slowly as the input grows. Think of repeatedly cutting a phone book in half to find a name.
- **O(n)**: Time grows directly with the input size. Checking every item in a list.
- **O(n log n)**: A bit more than linear but not too bad. Sorting items efficiently.
- **O(n^2)**: Time grows rapidly with input size. Checking every pair of items in a list.
- **O(2^n)**: Time doubles with each addition to the input size. Very slow for large inputs.
- **O(n!)**: Time grows extremely fast. Arranging a deck of cards in every possible way.

### Space Complexity

**Space Complexity** is about how much memory an algorithm uses as the input size grows.

Think of it like this:

- **O(1)**: Uses the same amount of memory no matter how big the input is.
- **O(n)**: Memory use grows directly with the input size. Storing items in a list.
- **O(n^2)**: Memory use grows rapidly with input size. Creating a grid of items.

### Logarithmic Time Complexity

To understand why the time complexity of certain algorithms is O(log n), let's derive the logarithmic equation, particularly in the context of binary search.

In binary search, we repeatedly divide the input size by 2 until we find the target element.

If we start with $`n`$ elements, the number of times we can divide $`n`$ by 2 until we get down to 1 element is the number of steps required by the binary search. This is expressed as:

$`[ \frac{n}{2^k} = 1 ]`$

Where $`k`$ is the number of steps.

Solving for $`k`$:

$`[ n = 2^k ]`$

Taking the logarithm (base 2) of both sides:

$`[ \log_2(n) = k ]`$

So, the number of steps $`k`$ is $`\log_2(n)`$.

Thus, the time complexity of binary search is O(log n).

### Examples

#### Linear Search

- **Time**: O(n) - Checking each item in a list.
- **Space**: O(1) - Uses a tiny amount of extra memory.

#### Merge Sort

- **Time**: O(n log n) - Efficiently sorts a list.
- **Space**: O(n) - Needs extra space for sorting.

#### Binary Search

- **Time**: O(log n) - Quickly finds an item in a sorted list.
- **Space**: O(1) - Uses a tiny amount of extra memory.

Understanding these concepts helps you choose the right algorithm for your problem, ensuring it runs fast and uses memory efficiently.
