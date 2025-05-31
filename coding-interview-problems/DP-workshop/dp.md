## DP workshop note

### Concept
- Level
- Choice 
- Check 
- Move


**How to apply move concept to the code?**

```python
def rec(level):
    for (all choice):
        if check(valid choice):
            move(choice)
```

Whenever a counting problem BASE Case will be 0 or 1.


#### Pruning vs Base case

- Base case : A base case is a condition under which the recursion stops.
- Pruning case: When a branch is abandoned early to save work.