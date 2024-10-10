
### Traingle Based Question:

https://leetcode.com/problems/valid-triangle-number/description/

https://leetcode.com/problems/triangle/description/

### Dominos Questions:

https://www.hackerearth.com/problem/algorithm/dominoes-1/

![image](https://github.com/user-attachments/assets/b99661e1-d15e-4158-873d-8f9d5a5c4e57)


## Backtracking  

**Backtracking** is a _general algorithmic technique_ used to solve problems _incrementally_ by _trying out different possibilities_ and _discarding those that don't meet the conditions_.

It is particularly useful for problems involving _searching through a set of possibilities,_ like puzzles, mazes, permutations, combinations, and constraint satisfaction problems.

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
