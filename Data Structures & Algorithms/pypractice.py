# ============================================================
# PROBLEM 1: Valid Brackets
# Time Complexity:  O(n) — single pass through the string
# Space Complexity: O(n) — stack holds at most n characters
# ============================================================

def is_valid(s):
    stack = []
    matching = {
        "[": "]",
        "{": "}",
        "(": ")"
    }
    for char in s:
        if char in "{[(":
            stack.append(char)
        else:
            if not stack or matching[stack[-1]] != char:  # fixed: inner ifs were unreachable due to wrong indentation
                return False
            stack.pop()
    return len(stack) == 0

def test_is_valid():
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("{[]}") == True
    assert is_valid("") == True
    assert is_valid("([)]") == False
    print("test_is_valid passed")


# ============================================================
# PROBLEM 2: Min Stack
# Time Complexity:  O(1) for all operations (push, pop, top, get_min)
# Space Complexity: O(n) — two stacks storing up to n elements
# ============================================================

class Min_stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

def test_min_stack():
    ms = Min_stack()
    ms.push(3)
    ms.push(5)
    assert ms.get_min() == 3
    ms.push(1)
    assert ms.get_min() == 1
    ms.pop()
    assert ms.get_min() == 3
    assert ms.top() == 5
    print("test_min_stack passed")


# ============================================================
# PROBLEM 3: Daily Temperatures
# Time Complexity:  O(n) — each element pushed/popped at most once
# Space Complexity: O(n) — result array and monotonic stack
# ============================================================

def warm_tem(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for curr_day, curr_tem in enumerate(temperatures):
        while stack and curr_tem > temperatures[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = curr_day - prev_day
        stack.append(curr_day)

    return result  # fixed: was indented inside the for loop

def test_warm_tem():
    assert warm_tem([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert warm_tem([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert warm_tem([30, 60, 90]) == [1, 1, 0]
    print("test_warm_tem passed")


# ============================================================
# PROBLEM 4: Evaluate Reverse Polish Notation
# Time Complexity:  O(n) — single pass through tokens
# Space Complexity: O(n) — stack holds up to n/2 operands
# ============================================================

def res_exp(tokens):
    stack = []
    for tok in tokens:
        if tok not in {"+", "-", "/", "*"}:
            stack.append(int(tok))
            continue
        b = stack.pop()
        a = stack.pop()
        if tok == "+":
            stack.append(a + b)
        if tok == "-":
            stack.append(a - b)       # fixed: was b - a
        if tok == "*":
            stack.append(a * b)
        if tok == "/":
            stack.append(int(a / b))  # fixed: was b / a; int() truncates toward zero per RPN spec

    return stack[-1]

def test_res_exp():
    assert res_exp(["2", "1", "+", "3", "*"]) == 9
    assert res_exp(["4", "13", "5", "/", "+"]) == 6
    assert res_exp(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    print("test_res_exp passed")


# ============================================================
# PROBLEM 5: Add Two Numbers (Linked List)
# Time Complexity:  O(max(m, n)) — traverse both lists once; m, n are their lengths
# Space Complexity: O(max(m, n)) — result list is at most max(m, n) + 1 nodes
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class add2linklist:
    def solution(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

    def make_list(self, nums):
        dummy = ListNode(0)
        cur = dummy
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next


ll = add2linklist()
l1 = ll.make_list([2, 4, 3])
l2 = ll.make_list([5, 6, 4])

result = ll.solution(l1, l2)

node = result
while node:
    print(node.val, end=" -> ")
    node = node.next



# ============================================================
# PROBLEM 6: Longest Substring Without Repeating Characters
# Time Complexity:  O(n) — each character added and removed from set at most once
# Space Complexity: O(min(n, m)) — set holds at most min(n, charset_size) chars
# ============================================================

def max_leng(s):
    left = 0
    max_len = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:        # fixed: missing colon
            seen.remove(s[left])       # fixed: was s[left) — mismatched bracket
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

def test_max_leng():
    assert max_leng("abcabcbb") == 3
    assert max_leng("bbbbb") == 1
    assert max_leng("pwwkew") == 3
    assert max_leng("") == 0
    print("test_max_leng passed")


# ============================================================
# PROBLEM 7: Maximum Sum Subarray of Size K
# Time Complexity:  O(n) — single pass using sliding window
# Space Complexity: O(1) — only a few scalar variables
# ============================================================

def max_sum(nums, k):
    if k > len(nums) or k < 0:  # fixed: was k < len(nums) — wrong guard condition
        return -1

    wind_sum = sum(nums[:k])
    maxS = wind_sum

    for right in range(k, len(nums)):
        wind_sum += nums[right]
        wind_sum -= nums[right - k]
        maxS = max(maxS, wind_sum)

    return maxS

def test_max_sum():
    assert max_sum([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum([2, 3, 4, 1, 5], 2) == 7
    assert max_sum([1, 2, 3], 5) == -1
    assert max_sum([1, 2], -1) == -1
    print("test_max_sum passed")


# ============================================================
# PROBLEM 8: Longest Repeating Character Replacement
# Time Complexity:  O(n) — single pass with sliding window
# Space Complexity: O(1) — counts dict has at most 26 keys (uppercase letters)
# ============================================================

def longRepcharSolu(s, k):
    max_freq = 0
    left = 0
    counts = {}

    for right in range(len(s)):       # fixed: missing colon
        char = s[right]
        counts[char] = counts.get(char, 0) + 1
        max_freq = max(max_freq, counts[char])

        if (right - left + 1) - max_freq > k:  # fixed: missing colon
            counts[s[left]] -= 1
            left += 1

    return len(s) - left

def test_longRepcharSolu():
    assert longRepcharSolu("ABAB", 2) == 4
    assert longRepcharSolu("AABACBD", 1) == 4
    assert longRepcharSolu("AAAA", 0) == 4
    assert longRepcharSolu("ABCD", 1) == 2
    print("test_longRepcharSolu passed")


# ============================================================
# PROBLEM 9: Longest Palindromic Substring
# Time Complexity:  O(n²) — expand around each of the 2n-1 centers
# Space Complexity: O(1) — only index variables, no extra data structures
# ============================================================

class Solution1:
    def longpal(self, s: str) -> str:
        if not s:                        # fixed: missing colon
            return ""
        start, end = 0, 0               # fixed: was start=end=0,0 (unpacks as tuple)

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:  # fixed: missing colon
                left -= 1
                right += 1
            return right - left - 1     # fixed: was right - left + 1 (off by 2; after loop, palindrome is s[left+1:right])

        for i in range(len(s)):
            l1 = expand_around_center(i, i)      # odd-length palindrome
            l2 = expand_around_center(i, i + 1)  # even-length palindrome
            max_len = max(l1, l2)

            if max_len > (end - start + 1):      # fixed: was extra ')' and missing ':'
                start = i - (max_len - 1) // 2  # fixed: was i - (max_len - 1) — missing // 2
                end = i + max_len // 2

        return s[start:end + 1]                  # fixed: was s[start:end+1 — missing ']'

def test_longpal():
    sol = Solution1()
    assert sol.longpal("babad") in ("bab", "aba")
    assert sol.longpal("cbbd") == "bb"
    assert sol.longpal("a") == "a"
    assert sol.longpal("ac") in ("a", "c")
    assert sol.longpal("racecar") == "racecar"
    print("test_longpal passed")



# ============================================================
# PROBLEM 10: Zigzag Conversion
# Time Complexity:  O(n) — single pass through the string
# Space Complexity: O(n) — rows list stores all characters
# ============================================================

def convertzigzag(s: str, numrows: int) -> str:
    if numrows <= 1 or numrows >= len(s):  # fixed: 0 → <=1 to also handle single-row case
        return s
    rows = [""] * numrows
    current_row = 0
    going_down = False
    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == (numrows - 1):  # fixed: was = (assignment) instead of ==, and missing colon
            going_down = not going_down
        current_row += 1 if going_down else -1
    return "".join(rows)

def test_convertzigzag():
    assert convertzigzag("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convertzigzag("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convertzigzag("A", 1) == "A"
    assert convertzigzag("AB", 1) == "AB"
    print("test_convertzigzag passed")


# ============================================================
# PROBLEM 11: Reverse Integer
# Time Complexity:  O(log x) — iterates over each digit of x
# Space Complexity: O(1) — only scalar variables
# ============================================================

import math

def reverseint(x: int) -> int:
    int_max = 2147483647
    int_min = -2147483648
    res = 0
    while x != 0:
        digit = int(math.fmod(x, 10))
        x = int(x / 10)                                          # fixed: was x/10 (float), need int truncation toward zero
        if res > int_max // 10 or (res == int_max // 10 and digit > 7):   # fixed: was int_max/10 (float compare); used //
            return 0
        if res < int_min // 10 or (res == int_min // 10 and digit < -8):  # fixed: same issue
            return 0
        res = res * 10 + digit
    return res

def test_reverseint():
    assert reverseint(123) == 321
    assert reverseint(-123) == -321
    assert reverseint(120) == 21
    assert reverseint(0) == 0
    assert reverseint(1534236469) == 0  # overflow → 0
    print("test_reverseint passed")


# ============================================================
# PROBLEM 12: Palindrome Number
# Time Complexity:  O(log x) — iterates over each digit
# Space Complexity: O(1) — only scalar variables
# ============================================================

def isPalind(x: int) -> bool:
    if x < 0:
        return False                  # fixed: was 'false' (lowercase, undefined)
    org = x
    rev_num = 0
    while x != 0:
        rev_num = (rev_num * 10) + (x % 10)
        x //= 10                      # fixed: was x/=10 (float division breaks the loop)
    return org == rev_num

def test_isPalind():
    assert isPalind(121) == True
    assert isPalind(-121) == False
    assert isPalind(10) == False
    assert isPalind(0) == True
    assert isPalind(1221) == True
    print("test_isPalind passed")


# ============================================================
# PROBLEM 13: Container With Most Water
# Time Complexity:  O(n) — single pass with two pointers
# Space Complexity: O(1) — only scalar variables
# ============================================================

def max_water(height: list) -> int:
    left = 0
    right = len(height) - 1
    max_w = 0
    while left < right:               # fixed: missing colon
        cur_height = min(height[left], height[right])
        width = right - left
        current_water = width * cur_height
        max_w = max(max_w, current_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_w

def test_max_water():
    assert max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_water([1, 1]) == 1
    assert max_water([4, 3, 2, 1, 4]) == 16
    print("test_max_water passed")


# ============================================================
# PROBLEM 14: Breadth First Search (BFS)
# Time Complexity:  O(V + E) — visits every vertex and edge once
# Space Complexity: O(V) — visited set and queue hold at most V nodes
# ============================================================

from collections import deque

def bfs(graph, node):
    visited = set()
    queue = deque()
    visited.add(node)
    queue.append(node)
    while queue:
        s = queue.popleft()           # fixed: was queue.pop() which gives LIFO (DFS), not BFS
        for n in graph[s]:            # fixed: missing colon
            if n not in visited:      # fixed: was 'if not in visited' — missing variable name n
                visited.add(n)
                queue.append(n)
    return visited

def test_bfs():
    graph = [[1, 2], [2, 3], [3, 4], [], []]
    assert bfs(graph, 0) == {0, 1, 2, 3, 4}
    graph2 = [[1], [0, 2], [1], []]
    assert bfs(graph2, 3) == {3}
    print("test_bfs passed")


# ============================================================
# PROBLEM 15: Depth First Search (DFS)
# Time Complexity:  O(V + E) — visits every vertex and edge once
# Space Complexity: O(V) — visited set and stack hold at most V nodes
# ============================================================

def dfs(graph, node):
    visited = set()
    stack = []
    stack.append(node)
    visited.add(node)
    while stack:
        s = stack.pop()
        for n in reversed(graph[s]):  # fixed: missing colon
            if n not in visited:
                visited.add(n)
                stack.append(n)
    return visited

def test_dfs():
    graph = [[1, 2], [2, 3], [3, 4], [], []]
    assert dfs(graph, 0) == {0, 1, 2, 3, 4}
    graph2 = [[1], [0, 2], [1], []]
    assert dfs(graph2, 3) == {3}
    print("test_dfs passed")


# ============================================================
# PROBLEM 16: Two Sum
# Time Complexity:  O(n) — single pass using hash map
# Space Complexity: O(n) — hash map stores up to n elements
# ============================================================

def twoSum(nums, target):
    seen = {}
    for index, num in enumerate(nums):  # fixed: missing colon
        val = target - num
        if val in seen:
            return [seen[val], index]
        seen[num] = index

def test_twoSum():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
    print("test_twoSum passed")


# ============================================================
# PROBLEM 17: Top K Frequent Elements
# Time Complexity:  O(n log n) — dominated by sorting the frequency dict
# Space Complexity: O(n) — frequency dictionary stores up to n entries
# ============================================================

def topKFreq(nums, k):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    sorted_num = sorted(frequency, key=frequency.get, reverse=True)
    return sorted_num[:k]

def test_topKFreq():
    assert topKFreq([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert topKFreq([1], 1) == [1]
    assert topKFreq([2, 2, 2, 4], 1) == [2]
    print("test_topKFreq passed")


# ============================================================
# PROBLEM 18: Anagram Check
# Time Complexity:  O(n) — two passes through strings of length n
# Space Complexity: O(1) — dict has at most 26 keys (lowercase letters)
# ============================================================

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in t:
        if char not in counts:        # fixed: was 'if char not in t' — should check counts dict, not string t
            return False
        counts[char] -= 1
        if counts[char] < 0:
            return False
    return True

def test_is_anagram():
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("dab", "bad") == True
    assert is_anagram("a", "ab") == False
    print("test_is_anagram passed")


# ============================================================
# PROBLEM 19: Trie Implementation
# insert/search/starts_with Time Complexity: O(m) — m = length of word
# Space Complexity: O(m * n) — m avg word length, n = number of words
# ============================================================

class TrieNode:
    def __init__(self):
        self.children = {}            # fixed: was //dictionary (JS-style comment)
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

def test_trie():
    t = Trie()
    t.insert("cat")
    t.insert("car")
    t.insert("cabrae")
    assert t.search("cat") == True
    assert t.search("ca") == False       # not a full word
    assert t.starts_with("ca") == True
    assert t.starts_with("dog") == False
    assert t.search("car") == True
    print("test_trie passed")


# ============================================================
# PROBLEM 20: Number of Islands
# Time Complexity:  O(m * n) — each cell visited at most once
# Space Complexity: O(m * n) — recursion stack depth in worst case
# ============================================================

class IslandSolution:
    def numIslands(self, grid: list) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  #island sinking to show we visited
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count

def test_numIslands():
    sol = IslandSolution()
    grid1 = [["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]
    assert sol.numIslands(grid1) == 3

    grid2 = [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]]
    assert sol.numIslands(grid2) == 1

    grid3 = [["1","0"],["0","1"]]
    assert sol.numIslands(grid3) == 2
    print("test_numIslands passed")

#PROBLEM 21:Orange Rotting problem
#Time:O(m*n)
#Space:O(m*n)

from collections import deque
class Solution:
    def orangeRotting(self,grid:list[list[int]]):
        empty,fresh,rotten=0,1,2
        m,n=len(grid),len(grid[0])
        num_fresh=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==rotten:
                    q.append((i,j))
                elif grid[i][j]==fresh:
                    num_fresh+=1

        if num_fresh==0:
            return 0

        num_minutes=-1
        while q:
            q_size=len(q)
            num_minutes+=1
            for _ in range(q_size):
                i,j=q.popleft()
                for r,c in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]==fresh:
                        grid[r][c]=rotten
                        num_fresh-=1
                        q.append((r,c))

        if num_fresh==0:
            return num_minutes
        else:
            return -1

s=Solution()
print(s.orangeRotting([[2,1,1],[1,1,0],[0,1,1]]))

#PROBLEM 22:Balanced Tree node
#Time: O(n)
#space: O(h)
from typing import Optional

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution():
    def isBalanced(self,root:Optional[TreeNode]):
        balance=[True]
        def height(root):
            if not root:
                return 0

            left_height=height(root.left)
            if balance[0] is False:
                return 0
            right_height=height(root.right)
            if abs(left_height-right_height)>1:
                balance[0]=[False]
                return 0

            return 1+max(left_height,right_height)

        height(root)
        return balance[0]

root = TreeNode(1)
root.right = TreeNode(3)

root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

# 2. Test the solution
tester = Solution()
print(f"Is balanced? {tester.isBalanced(root)}")

# 1. Create the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# 2. Test the solution
tester = Solution()
print(f"Is balanced? {tester.isBalanced(root)}")  # Expected Output: True

#PROBLEM 23:Course scheduler
#time: O(N+E)
#space:O(N+E) course scheduler
from collections import defaultdict

class Solution():
    def canFinish(self,numcourses,prereq:list[list[int]]):
        g=defaultdict(list)
        #courses=prereq
        for a,b in prereq:
            g[a].append(b)

        UNVISITED=0
        VISITING=1
        VISITED=2
        states=[UNVISITED]* numcourses
        def dfs(node):
            state=states[node]
            if state==VISITED: return True
            elif state==VISITING: return False
            states[node]=VISITING
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node]=VISITED
            return True

        for i in range(numcourses):
            if not dfs(i):
                return False

        return True
test=Solution()
testpre=[[1,0],[0,1]]
result=test.canFinish(2,testpre)
print(result)


#Time: O(H+V)
#space :O(H+V)
#PROBLEM 24:Lowest common ancestor
class TreeNode():
  def __init__(self,val=0,right=None,left=None):
      self.val=val
      self.right=right
      self.left=left

class Solution():
    def lca(self,root:'TreeNode',p:'TreeNode',q:'TreeNode'):
        if not root or root==p or root==q:
            return root
        left = self.lca(root.left,p,q)
        right = self.lca(root.right,p,q)

        if left or right:
            return root

        return left if left else right
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(7)
root.left.right = TreeNode(4)

p=root.left.left
q=root.right.right
sol=Solution()
result=sol.lca(root,p,q)
print(result.val)


#===============
#PROBLEM 25:rotated sorted array search-Search in Rotated Sorted Array.
#nums = [4, 5, 6, 7, 0, 1, 2]
#target = 0
def search(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid] == target:
            return mid
        if nums[left]<=nums[mid]:
            if nums[left]<=target<nums[mid]:
                right=mid-1
            else:
                left=mid+1

        else:
            if nums[mid]<target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
    return -1
print(search([4,5,6,7,0,1,2,3],4))




#PROBLEM 26:=======KOKO eating bananas===========
#time:O(n * log(max(piles))
#space: O(n)
from math import ceil
class koko():
    def sol(self,piles:list[int],h):
        def k_works(k):
            hours=0
            for n in piles:
                hours+=ceil(n/k)
            return hours<=h

        l=1
        r=max(piles)
        while l<r:
            k=(l+r)//2
            if k_works(k):
                r=k
            else :
                l=k+1
        return r

#================
# PROBLEM 27 vowel in substring of given length k [abciiiddd]
def vowelsubstr(s, k):
    vowel = {"a", "e", "i", "o", "u"}
    left = 0
    counter = 0
    max_c = 0
    for ch in s[:k]:
        if ch in vowel:
            counter += 1

    max_c = counter
    # print(max_c)
    for n in range(k, len(s)):
        if s[n] in vowel:
            counter += 1
        if s[left] in vowel:
            counter -= 1
        left += 1
        max_c = max(max_c, counter)
    return max_c


print(vowelsubstr("aabiid", 3))

#================
# PROBLEM 28 Binary Tree Level Order Traversal
#Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).
#time:O(n)
#space: O(n)

from collections import deque

class TreeNode():
  def __init__(self, val=0,left=None,right=None):
    self.val=val
    self.left=left
    self.right=right

class Solution():
  def nodereversal(self,root):
    if not root:
      return []
    result=[]
    queue=deque([root])
    while queue:
      current=[]
      level=len(queue)
      for _ in range(level):
        node=queue.popleft()
        current.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)

      result.append(current)
    return result



# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    test_is_valid()
    test_min_stack()
    test_warm_tem()
    test_res_exp()

    test_max_leng()
    test_max_sum()
    test_longRepcharSolu()
    test_longpal()
    test_convertzigzag()
    test_reverseint()
    test_isPalind()
    test_max_water()
    test_bfs()
    test_dfs()
    test_twoSum()
    test_topKFreq()
    test_is_anagram()
    test_trie()
    test_numIslands()
    print("\nAll 20 tests passed!")
