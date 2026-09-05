# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
Binary Search Trees were explained to me, as well as how they can be searched and inserted into through recursion. Also, I was told how the left and right sides of the BST depend on the value of each of its nodes. Through recursion, I understood how the program interacts with each part of the tree.
3. What challenges did you encounter, and how did you overcome them?
The problem I faced was dealing with the program working properly if the tree is empty or if the value to be inserted is already present in the tree. I tackled these problems through the inclusion of conditionals that check whether the node is empty and do not allow duplicates to be added to the tree.
5. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
The structure in which data is stored can greatly affect the speed at which the operations are carried out. Searching for a value in a BST is quicker than in an unsorted array since it is able to tell in which direction it needs to proceed instead of comparing all values. A balanced BST will be able to achieve a search time of O(log n) on average compared to O(n) for an unsorted list.
