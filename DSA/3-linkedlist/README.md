### Summary
Today, we implement a linked list in Python, exploring various operations, their complexities, and a related exercise for hands-on practice.


### Linked Lists

A linked list consists of nodes with some sort of data, and a pointer, or link, to the next node.
A singly linked list.
#### single linked lists

<img src="https://www.w3schools.com/dsa/img_linkedlists_singly.svg">

#### doubly linked lists

<img src="https://www.w3schools.com/dsa/img_linkedlists_doubly_wvalues.svg">
A big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays. Another nice thing with linked lists is that when adding or removing nodes, the rest of the nodes in the list do not have to be shifted.

[`FOR MORE INFO`](https://www.w3schools.com/dsa/dsa_theory_linkedlists.php)

### Highlights
- 📚 Implementing linked lists in Python.
- 📈 Understanding array limitations and linked list advantages.
- 🔄 Demonstrating insertion and deletion operations.
- 🔍 Exploring Big O complexities for various operations.
- 🧩 Introducing doubly linked lists and their benefits.
- 🛠️ Hands-on exercise to reinforce learning.
- 🔗 Accessing code and solutions on GitHub.

### Key Insights
- 💡 **Dynamic Arrays vs. Linked Lists**: While dynamic arrays require contiguous memory and can lead to inefficient insertions, linked lists use nodes with pointers, allowing easier and efficient insertions and deletions. 
- ⚖️ **Efficiency of Operations**: Linked lists offer O(1) time complexity for insertions and deletions at the beginning, compared to O(n) for arrays. However, traversing linked lists remains O(n).
- 🔄 **Doubly Linked Lists**: These allow traversal in both directions, providing more flexibility than singly linked lists, which only allow forward traversal.
- 📊 **Array Access Speed**: Arrays provide O(1) access time for indexed elements, while linked lists require O(n) time to access elements by index due to their pointer-based structure.
- 🛠️ **Hands-on Practice Importance**: Engaging with coding exercises is crucial for mastering linked lists and understanding their implementation deeply.
- 🔍 **Memory Management**: Python handles memory management automatically, reducing the complexity when dealing with linked list structures compared to languages like C++.
- 🌐 **Code Accessibility**: The tutorial emphasizes the importance of reviewing code examples on GitHub to enhance understanding and application of concepts learned.
