class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

'''
We choose a set() because it provides O(1) average time complexity for both lookups (if num in seen) and insertions (seen.add(num)).
Here is why a set outperforms other data structures for this specific task:

1. Fast Lookups vs. Lists

• With a set(): Python uses a hash table behind the scenes. Checking if an item exists takes constant time (O(1)), regardless of how many items are already in the set.
• With a list(): Checking if an item exists requires Python to scan the entire list from left to right. This takes linear time (O(n)). Inside your for loop, using a list would slow the entire algorithm down to O(n²).

2. Built for Uniqueness

A set is mathematically designed to hold only unique elements. It is the most semantically correct structure to use when your only goal is to track whether you have seen an item before.

3. Comparison of Alternatives

Data Structure	Lookup Time	Insertion Time	Overall Algorithm Time
set() (Hash Table)	O(1)	O(1)	O(n) — Fastest
list() (Array)	O(n)	O(1)	O(n²) — Too Slow
'''
