# Day 2: Hash Maps & Dictionaries

## 📝 Problem Solved
**Problem:** [Valid Anagram (LeetCode 242)](https://leetcode.com/problems/valid-anagram/)
- **Difficulty:** Easy
- **Goal:** Determine if two strings use the exact same characters with the exact same frequency.

## 💡 What I Learned
Today I focused on the **Frequency Counter Pattern** and using Python Dictionaries efficiently.

1. **Hash Maps (Dictionaries):**
   - **Resource:** [W3Schools Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
   - Unlike Sets (which only store keys), Dictionaries store **Key-Value pairs**.
   - Perfect for counting items: `Key = Item`, `Value = Count`.
   - **Lookups:** Still $O(1)$ (Instant).

2. **The `.get()` Trick:**
   - Avoiding `KeyError` when a key doesn't exist yet.
   - Syntax: `count = my_dict.get(char, 0)` (Returns 0 if not found).

3. **Time Complexity Analysis:**
   - **Sorting Method:** Sorting both strings takes $O(n \log n)$ (Slow).
   - **Hash Map Method:** Counting characters takes $O(n)$ (Fast).



## 💻 The Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimization: If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        cs = {}
        ts = {}
        
        # Count frequency of characters in s
        for x in s:
            cs[x] = cs.get(x, 0) + 1
            
        # Count frequency of characters in t
        for x in t:
            ts[x] = ts.get(x, 0) + 1
            
        # Compare the two dictionaries
        return cs == ts