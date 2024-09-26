https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/ ✨

https://leetcode.com/problemset/  ✨

https://www.hackerearth.com/problem/algorithm/dominoes-1/

![image](https://github.com/user-attachments/assets/b99661e1-d15e-4158-873d-8f9d5a5c4e57)


## Backtracking  

Q. What is Backtracking?

Ans: **Backtracking** is a _general algorithmic technique_ used to solve problems _incrementally_ by _trying out different possibilities_ and _discarding those that don't meet the conditions_.

It is particularly useful for problems involving _searching through a set of possibilities,_ like puzzles, mazes, permutations, combinations, and constraint satisfaction problems.

Q. What is the template for Backtracking? Generate basic pseudocode.

Ans:
```python
def backtrack(solution):
    # Base case: If the current solution is complete, return the solution
    if solution is complete:
        return solution

    # Explore all possible choices
    for choice in all possible choices:
        # Make the choice
        make the choice
        
        # Check if the choice is valid (satisfies constraints)
        if is_valid(choice):
            # Recurse to explore further with the current choice
            backtrack(solution)
        
        # Undo the choice (backtrack)
        undo the choice

```
Q. Provide a summary of Backtracking.

Ans:  
Summary:

- **Backtracking** is a recursive algorithmic technique to solve problems incrementally, trying out all possible solutions and pruning paths that don’t lead to a valid solution.
- It’s useful for exploring all possible configurations in a search space but stops exploring a path once it realizes that it can't lead to a solution, thus saving time

### Solving a Maze

Imagine you're trying to solve a maze. Starting at the entrance, you can move in multiple directions (up, down, left, right) at each step. With backtracking, you do the following:

1. Move in one direction.
2. If you reach a dead end or hit a wall, **backtrack** (return to the previous step) and try a different direction.
3. If you reach the exit, you've found the solution.
4. If you've tried all paths and none work, there's no solution.


## 2\. DFS

Q. What is DFS?

Ans: **Depth-First Search (DFS)** is an algorithm for traversing or searching through tree or graph data structures.

The idea is to start at a root node and explore as far as possible along each branch before backtracking.

Q. What is the time and space complexity?  
Ans:

**Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.

**Space Complexity**: O(V), due to the storage required for the queue and the visited list.

## 3\. BFS

Q. What is BFS

Breadth-First Search (BFS) is an algorithm for traversing or searching a graph or tree level by level.

Starting from a given node, it explores all neighboring nodes before moving to nodes at the next level.

Q. What data structure does it use?  
Ans: BFS uses a queue to ensure that nodes are processed in the order they are discovered.

Q. What is the time and space complexity

Ans:

**Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.

**Space Complexity**: O(V), due to the storage required for the queue and the visited list.

### BFS (Using Deque) Code
```python
from collections import deque

def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Initialize queue with the starting node
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")  # Process the current node (e.g., print it)

        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')  # Start BFS from node 'A'

```
## 4\. Deque (From Python Collections)
### Definition

Q. What is Deque?

Ans:

- A **Deque** (short for "Double-Ended Queue") is a data structure that allows _insertion and deletion of elements from both ends_—front and rear.
- It is a more versatile form of a queue where elements can be added or removed from either the front (left) or the back (right).
- In Python, the deque is part of the collections module and is _optimized for fast O(1) append and pop operations_ from both ends, unlike lists which have O(n) complexity for such operations at the beginning.

Q. What are the key operations?

### Key Operations

1. **append(item)**: Adds item to the right (end).
2. **appendleft(item)**: Adds item to the left (front).
3. **pop()**: Removes and returns the rightmost element.
4. **popleft()**: Removes and returns the leftmost element.

``` python
from collections import deque

# Create a deque
d = deque([1, 2, 3])

# Append elements to both ends
d.append(4)       # Adds to the right
d.appendleft(0)   # Adds to the left

print(d)          # Output: deque([0, 1, 2, 3, 4])

# Pop elements from both ends
d.pop()           # Removes from the right
d.popleft()       # Removes from the left

print(d)          # Output: deque([1, 2, 3])


```
