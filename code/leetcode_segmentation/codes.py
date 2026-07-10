import collections
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def divide(a: int, b: int) -> int:
    flag = 1 if b > 0 else -1
    flag = flag if a > 0 else 0 - flag
    a = a if a > 0 else 0 - a
    b = b if b > 0 else 0 - b

    if b == 1:
        res = a
    else:
        res = 0
        while a - b >= 0:
            cur_res, cur_b = binaryCal(a, b)
            res += cur_res
            a -= cur_b

    res = res if flag == 1 else 0 - res
    if res >= 2147483647: res = 2147483647
    if res <= -2147483648: res = -2147483648

    return res

def binaryCal(a: int, b: int) -> (int, int):
    tmp = 1
    while a >= b + b:
        b += b
        tmp += tmp
    return tmp, b

def addBinary(a: str, b: str) -> str:
    res, pre, cur = [], 0, 0
    aCount, bCount = len(a), len(b)

    i, j = aCount - 1, bCount - 1

    while i >= 0 and j >= 0:
        cur += 1 if a[i] == "1" else 0
        cur += 1 if b[j] == "1" else 0
        cur += pre

        pre, cur = cur // 2, cur % 2

        res.append(str(cur))
        cur = 0

        i -= 1
        j -= 1

    while i >= 0:
        cur += 1 if a[i] == "1" else 0
        cur += pre

        pre, cur = cur // 2, cur % 2

        res.append(str(cur))
        cur = 0

        i -= 1

    while j >= 0:
        cur += 1 if b[j] == "1" else 0
        cur += pre

        pre, cur = cur // 2, cur % 2

        res.append(str(cur))
        cur = 0

        j -= 1

    if pre == 1: res.append(str(pre))

    res = res[::-1]
    while res and res[0] == "0": res.pop(0)

    return "".join(res) if res else "0"

def countBits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    if n == 0: return dp
    dp[1] = 1
    if n == 1: return dp

    i, tmp = 2, 4
    while i <= n:
        if i >= tmp:
            tmp += tmp

        dp[i] = dp[i - tmp // 2] + 1 if i - tmp // 2 >= 0 else 1

        i += 1

    return dp

def singleNumber(nums: list[int]) -> int:
    one, two = 0, 0
    for n in nums:
        one = one ^ n & ~ two
        two = two ^ n & ~ one

    return one

def maxProduct_1(words: list[str]) -> int:
    count = len(words)
    mask = [0] * len(words)
    word_count = [0] * len(words)
    for i in range(count):
        word_count[i] = len(words[i])
        for w in words[i]:
            mask[i] |= (1 << ord(w) - ord("a"))

    res = 0
    for i in range(count):
        for j in range(i + 1, count):
            if mask[i] & mask[j] == 0:
                res = max(res, word_count[i] * word_count[j])

    return res

def maxProduct_2(words: list[str]) -> int:
    count = len(words)
    mask = {}
    for i in range(count):
        tmp = 0
        for w in words[i]:
            tmp |= (1 << ord(w) - ord("a"))
        mask[tmp] = max(mask[tmp], len(words[i])) if tmp in mask.keys() else len(words[i])
    res = 0
    for a_k, a_v in mask.items():
        for b_k, b_v in mask.items():
            if not (a_k & b_k):
                res = max(a_v * b_v, res)

    return res

def twoSum(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1

    while i < j and numbers[i] + numbers[j] != target:
        while i < j and numbers[i] + numbers[(j + 1 + i) // 2] > target:
            j = (i + 1 + j) // 2 - 1

        while i < j and numbers[j] + numbers[(j - 1 + i) // 2] < target:
            i = (i + j - 1) // 2 + 1

        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1

    return [i, j]

def threeSum(nums: list[int]) -> list[list[int]]:
    count = len(nums)
    if count < 3: return []

    nums.sort()
    res = []
    for mi in range(count - 2):
        if nums[mi] > 0: break
        elif mi > 0 and nums[mi] == nums[mi - 1]: continue

        mid, ma = mi + 1, count - 1
        while mid < ma:
            while mid > mi + 1 and mid < ma and nums[mid] == nums[mid - 1]: mid += 1
            if mid >= ma: break

            cur =  nums[mi] + nums[mid] + nums[ma]
            if cur == 0:
                res.append([nums[mi], nums[mid], nums[ma]])
                mid += 1
            elif cur > 0:
                ma -= 1
            else:
                mid += 1

    return res

def minSubArrayLen(target: int, nums: list[int]) -> int:
    res, cur, i, j, count = float("+inf"), 0, 0, 0, len(nums)
    while j < count:
        while j < count and cur < target:
            cur += nums[j]
            j += 1

        while i <= j and cur >= target:
            res = min(res, j - i)
            cur -= nums[i]
            i += 1

    return res if res != float("+inf") else 0

def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    res, count = 0, len(nums)
    i, cur = 0, 1
    for j in range(count):
        cur *= nums[j]
        while i <= j and cur >= k:
            cur /= nums[i]
            i += 1

        if i <= j: res += (j - i + 1)

    return res

def subarraySum(nums: list[int], k: int) -> int:
    res, count = 0, len(nums)

    sums, dtmp = 0, {0: 1}
    for i in range(count):
        sums += nums[i]
        res += dtmp.get(sums - k, 0)
        dtmp[sums] = dtmp.get(sums, 0) + 1

    return res

def findMaxLength(nums: list[int]) -> int:
    res, cur, dtmp = 0, 0, {0: -1}
    for i in range(len(nums)):
        cur += nums[i] if nums[i] == 1 else -1

        if cur not in dtmp.keys():
            dtmp[cur] = i

        res = max(res, i - dtmp[cur])
    return res

def pivotIndex(nums: list[int]) -> int:
    sums = [0]
    for n in nums:
        sums.append(sums[-1] + n)

    for i in range(1, len(nums) + 1):
        if sums[i - 1] == sums[-1] - sums[i]: return i - 1
    return -1


class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        row, col = len(matrix) + 1, 1 if not len(matrix) else len(matrix[0]) + 1
        self.sums = [[0] * col]
        for i in range(1, row):
            tmp = [0] * col
            for j in range(1, col):
                tmp[j] = tmp[j - 1] + self.sums[i - 1][j] + matrix[i - 1][j - 1] - self.sums[i - 1][j - 1]
            self.sums.append(tmp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] - self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1] + self.sums[row1][col1]


def checkInclusion(s1: str, s2: str) -> bool:
    ds1 = {}
    for s in s1:
        ds1[s] = ds1.get(s, 0) + 1

    cs1, cs2 = len(s1), len(s2)
    i, j, dtmp = 0, 0, {}
    while j < cs2:
        if s2[j] not in ds1.keys():
            i = j + 1
            dtmp = {}
        else:
            dtmp[s2[j]] = dtmp.get(s2[j], 0) + 1

            cur = dtmp.get(s2[j], 0)
            while i <= j and ds1.get(s2[j], 0) < cur:
                dtmp[s2[i]] = dtmp.get(s2[i], 0) - 1
                cur = dtmp.get(s2[j], 0)
                i += 1

        if j - i + 1 == cs1: return True
        j += 1
    return False

def findAnagrams(s: str, p: str) -> list[int]:
    res = []
    dp = {}
    for i in p:
        dp[i] = dp.get(i, 0) + 1

    cs, cp = len(s), len(p)
    i, j, dtmp = 0, 0, {}

    while j < cs:
        if s[j] not in dp.keys():
            i = j + 1
            dtmp = {}
        else:
            cur = dtmp[s[j]] = dtmp.get(s[j], 0) + 1
            while i <= j and cur > dp.get(s[j], 0):
                dtmp[s[i]] = dtmp.get(s[i], 0) - 1
                cur = dtmp.get(s[j], 0)
                i += 1

        if j - i + 1 == cp:
            res.append(i)

        j += 1

    return res

def lengthOfLongestSubstring(s: str) -> int:
    res, stmp, i, j, count = 0, set(), 0, 0, len(s)
    while j < count:
        while i <= j and s[j] in stmp:
            stmp.remove(s[i])
            i += 1

        stmp.add(s[j])

        res = max(j - i + 1, res)
        j += 1
    return res


def minWindow(s: str, t: str) -> str:
    ttmp = {}
    for i in t:
        ttmp[i] = ttmp.get(i, 0) + 1

    i, j, cs, dtmp = 0, 0, len(s), {}
    res, cres = None, float("+inf")
    while j < cs:
        if s[j] in ttmp.keys():
            dtmp[s[j]] = dtmp.get(s[j], 0) + 1

        if check(dtmp, ttmp):
            while i <= j and (s[i] not in ttmp.keys() or dtmp.get(s[i], 0) > ttmp.get(s[i], 0)):
                dtmp[s[i]] = dtmp.get(s[i], 0) - 1
                i += 1

            if cres > j - i + 1:
                res = s[i: j + 1]
                cres = j - i + 1

            while i <= j and (s[i] not in ttmp.keys() or check(dtmp, ttmp)):
                if s[i] in ttmp.keys():
                    dtmp[s[i]] = dtmp.get(s[i], 0) - 1
                i += 1
        j += 1
    return res if res else ""

def check(ad: dict, bd: dict) -> bool:
    for b in bd.keys():
        if ad.get(b, 0) < bd.get(b, 0):
            return False

    return True

def isPalindrome_1(s: str) -> bool:
    for i in range(len(s)):
        if "A" <= s[i] <= "Z":
            s = s[:i] + chr(ord(s[i]) - ord("A") + ord("a")) + s[i + 1:]

    i, j = 0, len(s) - 1
    while i <= j:
        while i <= j and not ("a" <= s[i] <= "z" or "0" <= s[i] <= "9"): i += 1
        while i <= j and not ("a" <= s[j] <= "z" or "0" <= s[j] <= "9"): j -= 1
        if i <= j and s[i] != s[j]: return False
        i += 1
        j -= 1

    return True

def validPalindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return checkPalindrome(s, i + 1, j) or checkPalindrome(s, i, j - 1)
        i += 1
        j -= 1

    return True

def checkPalindrome(s: str, i: int, j: int) -> bool:
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1

    return True

def countSubstrings_1(s: str) -> int:
    res = 0
    for i in range(len(s)):
        res += checkSubString(s, i, i) + checkSubString(s, i, i + 1)
    return res

def checkSubString(s: str, i: int, j: int) -> int:
    res, count = 0, len(s)
    while i >= 0 and j < count:
        if s[i] == s[j]:
            res += 1
            i -= 1
            j += 1
        else:
            return res
    return res


def countSubstrings_2(s: str) -> int:
    res = 0
    new_s = "#" + "#".join(s) + "#"
    cs, pre_i, pre_right = len(new_s), 0, 0
    dp = [1] * cs
    for i in range(1, cs):
        dp[i] = min(dp[2 * pre_i - i], pre_right - i + 1) if i <= pre_right else 1

        cur_i, cur_j = i - dp[i], dp[i] + i
        while cur_i >= 0 and cur_j < cs:
            if new_s[cur_i] != new_s[cur_j]: break
            cur_i -= 1
            cur_j += 1
        if pre_right < cur_j - 1:
            pre_i, pre_right = i, cur_j - 1

        dp[i] = cur_j - i
        res += dp[i] // 2

    return res

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    new_head = ListNode(-1, head)

    cur = head
    while cur and n:
        cur = cur.next
        n -= 1
    pre = new_head
    while cur:
        pre, cur = pre.next, cur.next
    cur = pre.next
    pre.next = cur.next if cur and cur.next else None

    return new_head.next

def detectCycle(head: ListNode) -> ListNode:
    slow, fast = head, head
    while slow and fast:
        slow = slow.next
        fast = fast.next.next if fast and fast.next else None
        if slow == fast: break
    if not fast or not slow: return None

    slow = head
    while slow and fast:
        if slow == fast: break
        slow = slow.next
        fast = fast.next
    return fast

def getIntersectionNode_1(headA: ListNode, headB: ListNode) -> ListNode:
    a, b = headA, headB
    while a and b:
        if a == b: return a
        a, b = a.next, b.next

    if not a: a = headB
    elif not b: b = headA
    while a and b:
        if a == b: return a
        a, b = a.next, b.next

    if not a: a = headB
    elif not b: b = headA
    while a and b:
        if a == b: return a
        a, b = a.next, b.next

    return None

def getIntersectionNode_2(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB: return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a

def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next: return head
    head, last = reverse(head)
    head.next = None
    return last

def reverse(head: ListNode) -> (ListNode, ListNode):
    if not head or not head.next: return head, head
    cur, last = reverse(head.next)
    cur.next = head
    return head, last

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2: return l1 if l1 else l2

    cur_l1, new_l1 = reverse(l1)
    cur_l2, new_l2 = reverse(l2)
    if cur_l1: cur_l1.next = None
    if cur_l2: cur_l2.next = None

    cur_node = new_head = ListNode(0)
    tmp = 0
    while new_l1 and new_l2:
        cur = new_l1.val + new_l2.val + tmp
        cur_node.next = ListNode(cur % 10)

        tmp = cur // 10
        new_l1, new_l2, cur_node = new_l1.next, new_l2.next, cur_node.next

    new_ = new_l1 if new_l1 else new_l2
    while new_:
        cur = new_.val + tmp
        cur_node.next = ListNode(cur % 10)

        tmp = cur // 10
        new_, cur_node = new_.next, cur_node.next

    while tmp > 0:
        cur_node.next = ListNode(tmp % 10)
        tmp = tmp // 10
        cur_node = cur_node.next

    cur_node, new_head = reverse(new_head.next)
    if cur_node: cur_node.next = None
    return new_head

def reorderList(head: ListNode) -> None:
    if not head or not head.next: return

    stack = []
    cur = head
    while cur:
        stack.append(cur)
        cur = cur.next

    while stack:
        pre = stack.pop(0)
        cur = stack.pop() if stack else None
        tmp = pre.next

        if cur:
            pre.next, cur.next = cur, tmp if cur != tmp else None
        else:
            pre.next = cur

def isPalindrome_2(head: ListNode) -> bool:
    if not head or not head.next: return True
    a, b = pairListnode(head, head)
    return a.val == b.val

def pairListnode(headA: ListNode, headB: ListNode) -> (ListNode, ListNode):
    if not headB or not headB.next: return headA, headB
    curA, curB = pairListnode(headA, headB.next)
    if curA.val == curB.val:
        return curA.next, headB
    else:
        return curA, curB

def flatten(head: 'Node') -> 'Node':
    if not head: return head
    new_head = Node(-1)
    ppre, pre, cur, ccur, stack = None, new_head, head, None, []

    while cur or stack:
        if cur.child:
            if cur.next: stack.append(cur.next)
            ccur = cur.child
            cur.child = None
        else:
            ccur = stack.pop() if not cur.next and stack else cur.next

        pre.prev, pre.next, cur.prev, cur.next = ppre, cur, pre, ccur
        ppre, pre, cur, ccur = pre, cur, ccur, stack.pop() if not cur.next and stack else cur.next

    new_head.next.prev = None
    return new_head.next

def insert(head: 'Node', insertVal: int) -> 'Node':
    new_node = Node(insertVal)
    if not head:
        head = new_node
        head.next = head
        return head
    elif head == head.next:
        head.next, new_node.next = new_node, head
        return head

    pre, cur = head, head.next
    while cur != head and pre.val <= cur.val: pre, cur = cur, cur.next

    max_, min_ = cur.val, pre.val
    if min_ > insertVal > max_:
        while cur.val < insertVal:
            pre, cur = cur, cur.next

    pre.next, new_node.next = new_node, cur

    return head


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._set = {}
        self.nums = []
        self.index = -1

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._set.keys():
            return False
        else:
            self.index += 1
            self.nums.append(val)
            self._set[val] = self.index
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._set.keys():
            return False
        else:
            cur_idx = self._set.get(val)
            self._set[self.nums[self.index]] = cur_idx
            self.nums[cur_idx] = self.nums[self.index]
            self.nums.pop()
            self.index -= 1
            self._set.pop(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)


class BiNode:
    def __init__(self, key, val, prev=None, next=None, child=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class LRUCache:
    def __init__(self, capacity: int):
        self.head = BiNode(-1, -1)
        self.tail = BiNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dkv = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        cur = self.dkv.get(key, None)
        if not cur: return -1
        self.moveHead(cur)
        return cur.val

    def put(self, key: int, value: int) -> None:
        if key not in self.dkv:
            cur = BiNode(key, value)
            self.dkv[key] = cur
            self.addHead(cur)
            self.size += 1

            if self.size > self.capacity:
                remove = self.removetail()
                self.dkv.pop(remove.key)
                self.size -= 1
        else:
            node = self.dkv[key]
            node.val = value
            self.moveHead(node)

    def removetail(self) -> BiNode:
        remove = self.tail.prev
        self.removeNode(remove)
        return remove

    def moveHead(self, node: BiNode) -> None:
        self.removeNode(node)
        self.addHead(node)

    def removeNode(self, node: BiNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def addHead(self, node: BiNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


def isAnagram(s: str, t: str) -> bool:
    sd, td = [0] * 26, [0] * 26
    for i in s:
        sd[ord(i) - ord("a")] += 1
    for j in t:
        td[ord(j) - ord("a")] += 1

    for k in range(26):
        if sd[k] != td[k]: return False

    for i, j in zip(s, t):
        if i != j: return True

    return False

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = {}
    for s in strs:
        ls = list(s)
        quicksortStr(ls, 0, len(ls) - 1)
        ls = "".join(ls)

        if ls in res:
            res[ls].append(s)
        else:
            res[ls] = [s]

    return list(res.values())

def quicksortStr( s: list, i: int, j: int) -> None:
    if i >= j: return
    l, r = i, j
    while l < r:
        while l < r and s[l] <= s[j]: l += 1
        while l < r and s[r] >= s[j]: r -= 1
        s[l], s[r] = s[r], s[l]
    s[l], s[j] = s[j], s[l]

    quicksortStr(s, i, l - 1)
    quicksortStr(s, l, j)

def isAlienSorted(words: list[str], order: str) -> bool:
    if not words or len(words) < 2: return True
    dd = {w: i for i, w in enumerate(order)}
    for i in range(1, len(words)):
        pre, cur = words[i - 1], words[i]
        len_pre, len_cur = len(pre), len(cur)

        idx = 0
        while idx < len_pre and idx < len_cur and dd[pre[idx]] == dd[cur[idx]]: idx += 1

        if (idx == len_cur or idx == len_pre):
            if len_pre > len_cur: return False
        elif dd[pre[idx]] > dd[cur[idx]]: return False

    return True

def findMinDifference(timePoints: list[str]) -> int:
    if not timePoints or len(timePoints) < 2: return 0

    minutes = []
    for time in timePoints:
        hour, minute = time.split(":")
        minutes.append(int(hour) * 60 + int(minute))
    minutes.sort()

    tl, max_time = len(minutes), 60 * 24
    dp = [0] * tl
    for i in range(tl):
        pre, cur = minutes[i - 1], minutes[i]
        mX, mI = max(pre, cur), min(pre, cur)
        diff = min(mX - mI, mI + 1440 - mX)
        dp[i] = diff if i == 0 else min(dp[i - 1], diff)

    return dp[-1]

def evalRPN(tokens: list[str]) -> int:
    stmp = []
    while tokens:
        cur = tokens.pop(0)

        if cur not in "+-*/":
            stmp.append(int(cur))
        else:
            num2 = stmp.pop()
            num1 = stmp.pop()

            stmp.append(cal(num1, num2, cur))
    return stmp[-1]

def cal(num1: int, num2: int, op: str) -> int:
    print(num1, op, num2)
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return int(num1 / num2)

def asteroidCollision_1(asteroids: list[int]) -> list[int]:
    if not asteroids or len(asteroids) < 2: return asteroids
    res = []
    for aster in asteroids:
        if aster < 0:
            if not res or res[-1] < 0:
                res.append(aster)
            else:
                asum = 0
                while res and res[-1] >= 0:
                    asum = res[-1] + aster
                    if asum < 0:
                        res.pop()
                    elif asum == 0:
                        res.pop()
                        break
                    else:
                        break
                if asum < 0: res.append(aster)
        elif aster > 0:
            res.append(aster)
        else:
            if not res or res[-1] <= 0: res.append(aster)

    return res

def asteroidCollision_2(asteroids: list[int]) -> list[int]:
    if not asteroids or len(asteroids) < 2: return asteroids
    res = []
    for aster in asteroids:
        alive = True
        while alive and aster < 0 and res and res[-1] >= 0:
            alive = res[-1] < -aster
            if res[-1] <= -aster: res.pop()

        if alive: res.append(aster)

    return res

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    if not temperatures: return []
    res, max_idx = [0] * len(temperatures), []
    for i in range(len(temperatures) - 1, -1, -1):
        while max_idx and temperatures[max_idx[-1]] <= temperatures[i]: max_idx.pop()
        res[i] = max_idx[-1] - i if max_idx else 0
        max_idx.append(i)

    return res


def largestRectangleArea(heights: list[int]) -> int:
    if not heights: return 0

    min_stack, res = [-1], 0
    for i, hg in enumerate(heights):
        while min_stack[-1] != -1 and heights[min_stack[-1]] > hg:
            height = heights[min_stack.pop()]
            width = i - min_stack[-1] - 1
            res = max(res, height * width)
        min_stack.append(i)

    while min_stack[-1] != -1:
        height = heights[min_stack.pop()]
        width = len(heights) - min_stack[-1] - 1
        res = max(res, height * width)

    return res

def maximalRectangle(matrix: list[str]) -> int:
    if not matrix or not matrix[0]: return 0

    row, col = len(matrix), len(matrix[0])
    heights, res = [0] * col, 0
    for mx in matrix:
        min_stack = [-1]
        for i in range(col):
            heights[i] = heights[i] + 1 if mx[i] == "1" else 0

            while min_stack[-1] != -1 and heights[min_stack[-1]] > heights[i]:
                height = heights[min_stack.pop()]
                width = i - min_stack[-1] - 1
                res = max(res, height * width)

            min_stack.append(i)

        while min_stack[-1] != -1:
            height = heights[min_stack.pop()]
            width = col - min_stack[-1] - 1
            res = max(res, height * width)

    return res


class MovingAverage:
    def __init__(self, size: int):
        self.queue = []
        self.length = 0
        self.size = size
        self.sums = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.length += 1
        self.sums += val

        if self.length > self.size:
            self.length -= 1
            self.sums -= self.queue.pop(0)

        return self.sums / self.length


class RecentCounter:
    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)

        pre = t - 3000
        i, j = 0, len(self.pings) - 1
        while i < j:
            mid = (i + j) // 2
            if self.pings[mid] < pre: i = mid + 1
            else: j = mid

        return len(self.pings) - i


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, v: int) -> int:
        if not self.root:
            self.root = TreeNode(v)
            return v

        n, nex, queue, pre = 0, [], [self.root], []
        while len(queue) >= 2 ** n:
            nex = []
            for i in range(2 ** n):
                if queue[i].left: nex.append(queue[i].left)
                if queue[i].right: nex.append(queue[i].right)

            n += 1
            pre, queue = queue, nex

        cur_num = len(queue) - 1
        if cur_num % 2:
            parent = pre[cur_num // 2 + 1]
            parent.left = TreeNode(v)
        else:
            parent = pre[cur_num // 2]
            parent.right = TreeNode(v)

        return parent.val

    def get_root(self) -> TreeNode:
        return self.root

def largestValues_1(root: TreeNode) -> list[int]:
    if not root: return []

    res, queue = [], [root]

    while queue:
        tmp, max_queue = [], []
        for _ in range(len(queue)):
            cur = queue.pop()

            if cur.left: tmp.append(cur.left)
            if cur.right: tmp.append(cur.right)

            while max_queue and max_queue[-1] < cur.val: max_queue.pop()
            max_queue.append(cur.val)

        res.append(max_queue[0])
        queue = tmp

    return res

def largestValues_2(root: TreeNode) -> list[int]:
    if not root: return []

    res, queue = [], [root]

    while queue:
        tmp, max_ = [], float("-inf")
        for _ in range(len(queue)):
            cur = queue.pop()

            if cur.left: tmp.append(cur.left)
            if cur.right: tmp.append(cur.right)

            max_ = max(max_, cur.val)

        res.append(max_)
        queue = tmp

    return res

def findBottomLeftValue(root: TreeNode) -> int:
    pre, queue = [], [root]

    while queue:
        tmp = []
        for i in range(len(queue)):
            cur = queue[i]
            if cur.left: tmp.append(cur.left)
            if cur.right: tmp.append(cur.right)
        pre, queue = queue, tmp

    return pre[0].val

def rightSideView(root: TreeNode) -> list[int]:
    res = []
    if not root: return res

    queue = [root]
    while queue:
        res.append(queue[-1].val)
        for _ in range(len(queue)):
            cur = queue.pop(0)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
    return res

def pruneTree(root: TreeNode) -> TreeNode:
    num = dfsAdd(root)
    if not root or (not root.val and not num): return None
    return root

def dfsAdd(root: TreeNode) -> int:
    if not root: return 0

    l = dfsAdd(root.left)
    r = dfsAdd(root.right)

    if not l: root.left = None
    if not r: root.right = None

    return l + r + root.val


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return [None]
        return [root.val] + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        self.data = data
        return self.dfsCreate()

    def dfsCreate(self):
        if not self.data: return None
        value = self.data.pop(0)
        root = TreeNode(value) if value != None else None
        if not root: return root
        root.left = self.dfsCreate()
        root.right = self.dfsCreate()
        return root


def sumNumbers(root: TreeNode) -> int:
    if not root: return 0
    child = dfsList(root)
    return sum(map(lambda x: x[-1], child))

def dfsList(root: TreeNode) -> [list[list[int, int]]]:
    if not root:
        return [[0, 0]]
    elif not root.left and not root.right:
        return [[1, root.val]]
    elif not root.left:
        child = dfsList(root.right)
    elif not root.right:
        child = dfsList(root.left)
    else:
        child = dfsList(root.left) + dfsList(root.right)
    for i in range(len(child)):
        child[i][1] += root.val * (10 ** (child[i][0]))
        child[i][0] += 1
    return child


def pathSum(root: TreeNode, targetSum: int) -> int:
    if not root: return 0
    dres = {0: 1}
    return dfsDict(root, targetSum, dres, 0)


def dfsDict(root, target, dtmp, csum):
    if not root: return 0

    csum += root.val
    res = dtmp.get(csum - target, 0)
    dtmp[csum] = dtmp.get(csum, 0) + 1

    res += dfsDict(root.left, target, dtmp, csum)
    if root.left: dtmp[csum + root.left.val] -= 1
    res += dfsDict(root.right, target, dtmp, csum)
    if root.right: dtmp[csum + root.right.val] -= 1

    return res

def maxPathSum(root: TreeNode) -> int:
    _, res = dfsSum(root, float("-inf"))
    return res

def dfsSum(root, res):
    if not root: return 0, res

    lSum, lRes = dfsSum(root.left, res)
    rSum, rRes = dfsSum(root.right, res)

    cSum = lSum + root.val + rSum
    res = max(res, cSum)

    return max(max(lSum, rSum) + root.val, 0), max(res, lRes, rRes)

def increasingBST(root: TreeNode) -> TreeNode:
    newroot = TreeNode(-1)
    _ = dfsNode(root, newroot)
    return newroot.right

def dfsNode(node, root):
    if not node: return root

    root = dfsNode(node.left, root)

    root.right = TreeNode(node.val)
    print(node.val)

    root = dfsNode(node.right, root.right)

    return root

def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    _, res = dfsbool([], root, p)
    return res

def dfsbool(pre: list[int], root: 'TreeNode', p: 'TreeNode') -> [list[int], TreeNode]:
    if not root: return pre, root

    pre, ln = dfsbool(pre, root.left, p)
    if ln: return pre, ln

    if pre and pre[-1] == p.val:
        return pre, root

    pre, rn = dfsbool(pre + [root.val], root.right, p)
    if rn: return pre, rn

    return pre, None

def convertBST(root: TreeNode) -> TreeNode:
    dfs_add(0, root)
    return root

def dfs_add(pre: int, root: TreeNode) -> int:
    if not root: return pre

    pre = dfsAdd(pre, root.right)

    root.val += pre
    pre = root.val

    pre = dfsAdd(pre, root.left)

    return pre


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.left = []
        cur = root

        tmp = []
        while tmp or cur:
            while cur:
                tmp.append(cur)
                cur = cur.left

            cur = tmp.pop()
            self.left.append(cur)

            cur = cur.right

    def next(self) -> int:
        return self.left.pop(0).val

    def hasNext(self) -> bool:
        return self.left != []

def findTarget(root: TreeNode, k: int) -> bool:
    pre, cur = set(), root

    tmp = []
    while tmp or cur:
        while cur:
            tmp.append(cur)
            cur = cur.left

        cur = tmp.pop()
        if k - cur.val in pre:
            return True
        else:
            pre.add(cur.val)

        cur = cur.right
    return False

from sortedcontainers import SortedList
def containsNearbyAlmostDuplicate_1(nums: list[int], k: int, t: int) -> bool:
    win = SortedList()

    for i in range(len(nums)):
        if i > k:
            win.remove(nums[i - k - 1])

        cur = win.bisect_right(nums[i] + t) - win.bisect_left(nums[i] - t)
        if cur > 0: return True

        win.add(nums[i])
    return False

def containsNearbyAlmostDuplicate(nums: list[int], k: int, t: int) -> bool:
    bucket = {}

    for i, num in enumerate(nums):
        bidx = int(num // (t + 1))

        if bidx in bucket or (bidx + 1 in bucket and abs(bucket[bidx + 1] - num) <= t) or (bidx - 1 in bucket and abs(bucket[bidx - 1] - num) <= t):
            return True

        bucket[bidx] = num
        if i > k - 1:
            bucket.pop(int(nums[i - k] // (t + 1)))
    return False


class MyCalendar:
    def __init__(self):
        self.start = []
        self.end = []

    def book(self, start: int, end: int) -> bool:
        if not self.start:
            self.start.append(start)
            self.end.append(end)
            return True

        idx = self.search(start)
        pre_start, pre_end = self.start[idx - 1] if idx > 0 else -1, self.end[idx - 1] if idx > 0 else -1
        nex_start, nex_end = self.start[idx] if idx < len(self.start) else float("+inf"), self.end[idx] if idx < len(
            self.end) else float("+inf")

        if end <= pre_start or (pre_end <= start < nex_start and pre_end <= end <= nex_start) or start >= nex_end:
            self.start.insert(idx, start)
            self.end.insert(idx, end)
            return True

        return False

    def search(self, num: int) -> int:
        if not self.start or self.start[0] > num:
            return 0
        elif self.start[-1] < num:
            return len(self.start)

        i, j = 0, len(self.start) - 1
        mid = (i + j) // 2
        while i < j:
            if self.start[mid] < num:
                i = mid + 1
            elif self.start[mid] > num:
                j = mid
            else:
                break
            mid = (i + j) // 2
        return mid


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.K = k - 1
        self.nums = nums
        self.nums.sort(reverse=True)

    def add(self, val: int) -> int:
        count = len(self.nums)
        if count == 0 or (count < 2 and self.nums[-1] >= val):
            self.nums.append(val)
        else:
            i, j, m = 0, count - 1, (count - 1) // 2
            while i < j:
                if self.nums[m] < val:
                    j = m
                elif self.nums[m] > val:
                    i = m + 1
                else:
                    break
                m = (i + j) // 2

            self.nums.insert(m, val)

        return self.nums[-1 if count < self.K else self.K]


def topKFrequent(nums: list[int], k: int) -> list[int]:
    dtmp = {}
    for num in nums:
        dtmp[num] = dtmp.get(num, 0) + 1

    freq = []
    for key, val in dtmp.items():
        tmp = []
        while freq and freq[-1][-1] < val: tmp.append(freq.pop())

        freq.append([key, val])

        while tmp: freq.append(tmp.pop())

    res = []
    for i in range(min(len(freq), k)):
        res.append(freq[i][0])

    return res

def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    cn, cn1, cn2 = 0, len(nums1), len(nums2)
    res, heap, tmp = [], [[0, 0]], [[0, 0]]

    i, j = heap.pop(0)
    while i < cn1 and j < cn2 and cn < k:
        print(i, j)
        res.append([nums1[i], nums2[j]])
        cn += 1

        if i + 1 < cn1 and [i + 1, j] not in tmp:
            heapAppend(nums1, nums2, heap, i + 1, j)
            tmp.append([i + 1, j])
        if j + 1 < cn2 and [i, j + 1] not in tmp:
            heapAppend(nums1, nums2, heap, i, j + 1)
            tmp.append([i, j + 1])

        i, j = heapPop(nums1, nums2, heap)

    return res

def heapPop(nums1: list[int], nums2: list[int], heap: list[list[int]]):
    if not heap: return len(nums1), len(nums2)
    i, j = heap.pop(0)
    if heap:
        cur = heap.pop()
        heap.insert(0, cur)
        heapDown(nums1, nums2, heap, 0)
    return i, j

def heapAppend(nums1: list[int], nums2: list[int], heap: list[list[int]], i: int, j: int):
    heap.append([i, j])
    heapUp(nums1, nums2, heap, len(heap) - 1)

def heapDown(nums1: list[int], nums2: list[int], heap: list[list[int]], idx: int):
    if idx >= len(heap): return
    left, right = idx * 2 + 1, idx * 2 + 2
    if left < len(heap) and nums1[heap[idx][0]] + nums2[heap[idx][1]] > nums1[heap[left][0]] + nums2[heap[left][1]]:
        heap[idx], heap[left] = heap[left], heap[idx]
        heapDown(nums1, nums2, heap, left)
    if right < len(heap) and nums1[heap[idx][0]] + nums2[heap[idx][1]] > nums1[heap[right][0]] + nums2[heap[right][1]]:
        heap[idx], heap[right] = heap[right], heap[idx]
        heapDown(nums1, nums2, heap, right)

def heapUp(nums1: list[int], nums2: list[int], heap: list[list[int]], idx: int):
    if idx <= 0: return
    parent = (idx - 1) // 2
    if parent >= 0 and nums1[heap[idx][0]] + nums2[heap[idx][1]] < nums1[heap[parent][0]] + nums2[heap[parent][1]]:
        heap[idx], heap[parent] = heap[parent], heap[idx]
        heapUp(nums1, nums2, heap, parent)


class TrieNode:
    def __init__(self):
        self.childs = {}
        self.is_end = False
        self.cnt = 0


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w not in node.childs:
                node.childs[w] = TrieNode()
            node = node.childs[w]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node.childs: return False

            node = node.childs[w]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for p in prefix:
            if p not in node.childs: return False

            node = node.childs[p]

        return True

    def short(self, word: str) -> str:
        res, node = "", self.root
        for w in word:
            if node.is_end: return res
            if w not in node.childs: break
            res += w
            node = node.childs[w]
        return word


def replaceWords(dictionary: list[str], sentence: str) -> str:
    trie = Trie()
    for d in dictionary:
        trie.insert(d)

    res = sentence.split()
    for i in range(len(res)):
        res[i] = trie.short(res[i])

    return " ".join(res)


class MagicDictionary_1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dcount = {}

    def buildDict(self, dictionary: list[str]) -> None:
        for dic in dictionary:
            count = len(dic)
            self.dcount[count] = self.dcount.get(count, []) + [dic]

    def search(self, searchWord: str) -> bool:
        count = len(searchWord)
        if count not in self.dcount: return False

        dicts = self.dcount[count]

        for dic in dicts:
            times = 0
            for i in range(count):
                if dic[i] != searchWord[i]: times += 1
            if times == 1: return True
        return False


class MagicDictionary_2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.neighbors = {}

    def buildDict(self, dictionary: list[str]) -> None:
        for dic in dictionary:
            self.words.add(dic)
            for neighbor in self.getNeighbors(dic):
                self.neighbors[neighbor] = self.neighbors.get(neighbor, 0) + 1

    def getNeighbors(self, words: str) -> list[str]:
        lwords, neighbor = list(words), []
        for i in range(len(lwords)):
            tmp = lwords[i]
            lwords[i] = "*"
            neighbor.append("".join(lwords))
            lwords[i] = tmp
        return neighbor

    def search(self, searchWord: str) -> bool:
        for neighbor in self.getNeighbors(searchWord):
            nc = self.neighbors.get(neighbor, 0)
            if nc > 1 or (nc == 1 and searchWord not in self.words): return True
        return False


def minimumLengthEncoding(words: list[str]) -> int:
    words = set(words)
    root, cnt = TrieNode(), 0

    # insert
    for word in words:
        node = root
        for w in word[::-1]:
            if w not in node.childs:
                node.childs[w] = TrieNode()
                node.cnt += 1
            node = node.childs[w]

        node.cnt += 1

    # search
    for word in words:
        i, node = len(word) - 1, root

        while node and i >= 0 and word[i] in node.childs:
            node = node.childs[word[i]]
            i -= 1

        if node.cnt == 1: cnt += len(word) + 1

    return cnt


class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        pre = self.d.get(key, 0)
        self.d[key] = val
        for k in key:
            if k not in node.childs:
                node.childs[k] = TrieNode()
            node.cnt += val - pre
            node = node.childs[k]

        node.cnt += val - pre

    def sum(self, prefix: str) -> int:
        node = self.root

        for p in prefix:
            if p not in node.childs: return 0
            node = node.childs[p]
        return node.cnt


def findMaximumXOR(nums: list[int]) -> int:
    high_bit = max(nums).bit_length() - 1
    res, bit = 0, 0
    for i in range(high_bit, -1, -1):
        bit |= 1 << i

        new_res = res | (1 << i)
        stmp = set()
        for num in nums:
            num &= bit
            if num ^ new_res in stmp:
                res = new_res
                break
            stmp.add(num)

    return res

def searchInsert(nums: list[int], target: int) -> int:
    if not nums: return 0

    i, j = 0, len(nums) - 1
    if nums[i] > target: return 0
    if nums[j] < target: return j + 1

    m = (i + j) // 2
    while i < j:
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            break
        m = (i + j) // 2

    return m + 1 if nums[m] < target else m


def peakIndexInMountainArray_1(arr: list[int]) -> int:
    i = 0
    while arr[i] < arr[i + 1]: i += 1
    return i

def peakIndexInMountainArray_2(arr: list[int]) -> int:
    i, j, res = 1, len(arr) - 2, 0
    m = (i + j) // 2

    while i <= j:
        if arr[m] > arr[m + 1]:
            res = m
            j = m - 1
        else:
            i = m + 1
        m = (i + j) // 2

    return res

def singleNonDuplicate_1(nums: list[int]) -> int:
    count = len(nums)

    for i in range(count):
        pre, cur, nex = nums[i - 1] if i > 0 else None, nums[i], nums[i + 1] if i < count - 1 else None
        if pre is not None and pre == cur:
            continue
        elif nex is not None and cur == nex:
            continue
        else:
            return nums[i]

def singleNonDuplicate_2(nums: list[int]) -> int:
    i, j = 0, len(nums) - 1
    while i < j:
        m = (i + j) // 2
        if nums[m] == nums[m + 1]:
            if m % 2:
                j = m - 1
            else:
                i = m + 2
        elif nums[m] == nums[m - 1]:
            if m % 2:
                i = m + 1
            else:
                j = m - 2
        else:
            return nums[m]

    return nums[i]


class PickIndex:
    def __init__(self, w: list[int]):
        self.wsum = []
        for n in w:
            self.wsum.append(self.wsum[-1] + n if self.wsum else n)

        self.sums = self.wsum[-1]

        print(self.wsum)

    def pickIndex(self) -> int:
        num = random.randint(1, self.sums)

        return self.binary_left(num)

    def binary_left(self, num: int) -> int:
        if not self.wsum: return -1
        if num < self.wsum[0]: return 0
        if num > self.wsum[len(self.wsum) - 1]: return len(self.wsum)

        i, j = 0, len(self.wsum) - 1
        while i < j:
            m = (i + j) // 2
            if self.wsum[m] < num:
                i = m + 1
            else:
                j = m

        return i

def mySqrt(x: int) -> int:
    i, j = 0, x
    while i < j:
        m = (i + j) // 2
        cur = m * m
        if x <= cur:
            j = m
        else:
            i = m + 1

    return i if i * i == x else i - 1

def minEatingSpeed(piles: list[int], h: int) -> int:
    i, j = 1, max(piles)

    while i < j:
        m = (i + j) // 2
        if check_k(piles, m) > h:
            i = m + 1
        else:
            j = m

    return i

def check_k(self, piles: list[int], k: int) -> int:
    res = 0
    for pile in piles:
        res += pile // k + 1 if pile % k else pile // k
    return res

def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])

    res = []
    for i, interval in enumerate(intervals):
        if i == 0:
            res.append(interval)
            continue

        ps, pe, cs, ce = res[-1][0], res[-1][-1], interval[0], interval[-1]

        if ps <= cs <= pe and ce > pe:
            res[-1][-1] = ce
        elif cs > pe:
            res.append(interval)

    return res

def relativeSortArray_1(arr1: list[int], arr2: list[int]) -> list[int]:
    arr1.sort()
    res = []
    for a2 in arr2:
        tmp = []
        for a1 in arr1:
            if a1 == a2: res.append(a1)
            else: tmp.append(a1)
        arr1 = tmp
    return res + arr1

def relativeSortArray_2(arr1: list[int], arr2: list[int]) -> list[int]:
    da1 = {}
    for a1 in arr1:
        da1[a1] = da1.get(a1, 0) + 1

    res = []
    for a2 in arr2:
        res.extend([a2] * da1[a2])
        da1.pop(a2)

    for i in range(1001):
        if i in da1: res.extend([i] * da1[i])

    return res

def findKthLargest(nums: list[int], k: int) -> int:
    heap = []

    for num in nums:
        addheap(heap, num)

    res = heap[0]
    while heap and k:
        res = popheap(heap)
        k -= 1

    return res

def popheap(heap: list[int]) -> int:
    res = heap.pop(0)
    if heap:
        heap.insert(0, heap.pop())
        down(heap, 0)

    return res

def addheap(heap: list[int], num: int) -> None:
    heap.append(num)
    up(heap, len(heap) - 1)

def up(heap: list[int], idx: int) -> None:
    if idx <= 0: return

    parent = (idx - 1) // 2
    if heap[parent] < heap[idx]:
        heap[parent], heap[idx] = heap[idx], heap[parent]
        up(heap, parent)

def down(heap: list[int], idx: int) -> None:
    count = len(heap)
    if idx >= count - 1: return
    l, r = idx * 2 + 1, idx * 2 + 2
    if l < count and heap[l] > heap[idx]:
        heap[l], heap[idx] = heap[idx], heap[l]
        down(heap, l)
    if r < count and heap[r] > heap[idx]:
        heap[r], heap[idx] = heap[idx], heap[r]
        down(heap, r)

def sortList_1(head: ListNode) -> ListNode:
    if not head or not head.next: return head
    res, node = [], head
    while node:
        if not res or res[-1].val < node.val:
            res.append(node)
        elif res[0].val > node.val:
            res.insert(0, node)
        else:
            i, j = 0, len(res) - 1
            while i < j:
                m = (i + j) // 2
                if res[m].val < node.val:
                    i = m + 1
                else:
                    j = m
            res.insert(i, node)
            print(i)

        node = node.next

    node = head = res.pop(0)
    while res:
        node.next = res.pop(0)
        node = node.next
    node.next = None

    return head

def sortList_2(head: ListNode) -> ListNode:
    if not head or not head.next: return head

    left, right = cutList(head)

    return mergeList(left, right)

def cutList(head: ListNode) -> (ListNode, ListNode):
    if not head or not head.next: return head, head
    fast, slow, pre = head, head, None
    while fast: fast, slow, pre = fast.next.next if fast.next else None, slow.next, slow
    pre.next = None
    return head, slow

def mergeList(left: ListNode, right: ListNode):
    if left == right: return left

    ll, lr = cutList(left)
    rl, rr = cutList(right)
    left = mergeList(ll, lr)
    right = mergeList(rl, rr)

    head = node = ListNode(float("-inf"))
    while left and right:
        if left.val < right.val:
            node.next = left
            left = left.next
        else:
            node.next = right
            right = right.next
        node = node.next

    if left: node.next = left
    if right: node.next = right
    return head.next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    lists = merge_list(lists)
    return lists[0] if lists else None

def merge_list(lists: list[ListNode]) -> list[ListNode]:
    if len(lists) < 2: return lists
    i, j = 0, len(lists) - 1
    res = []
    while i < j:
        left, right = lists[i], lists[j]
        node = head = ListNode(float("-inf"))
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next

        if left: node.next = left
        if right: node.next = right
        res.append(head.next)
        i += 1
        j -= 1

    if i == j: res.append(lists[i])

    return merge_list(res)

def subsets(nums: list[int]) -> list[list[int]]:
    res = [[]]
    for num in nums:
        res = numsOrder(num, res)

    return res

def numsOrder(num: int, res: list[list[int]]) -> list[list[int]]:
    for i in range(len(res)):
        res.append(res[i] + [num])
    return res

def combine(n: int, k: int) -> list[list[int]]:
    return numsCombin([[i] for i in range(1, n + 1)], n, k - 1)

def numsCombin(c: list[list[int]], n: int, k: int) -> list[list[int]]:
    if k == 0: return c

    res = []
    for i in c:
        for num in range(i[-1] + 1, n + 1):
            res.append(i + [num])

    return numsCombin(res, n, k - 1)

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort(reverse=True)
    return findTarget(candidates, [], [], target)

def findTarget(nums: list[int], res: list[list[int]], conds: list[int], target: int) -> list[list[int]]:
    if target < nums[-1]: return res
    for idx in range(len(nums)):
        cur_target = target - nums[idx]
        if cur_target == 0:
            res.append(conds + [nums[idx]])
        elif cur_target > 0:
            res = findTarget(nums[idx:], res, conds + [nums[idx]], cur_target)

    return res

def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort(reverse=True)
    print(candidates)
    return find_target(candidates, [], [], target)

def find_target(nums: list[int], res: list[list[int]], conds: list[int], target: int) -> list[list[int]]:
    if not nums or target < nums[-1]: return res

    count = len(nums)
    for idx in range(count):
        if idx > 0 and nums[idx] == nums[idx - 1]: continue
        cur_target = target - nums[idx]

        if cur_target == 0:
            res.append(conds + [nums[idx]])
        elif cur_target > 0:
            res = find_target(nums[idx + 1:] if idx < count - 1 else [], res, conds + [nums[idx]], cur_target)

    return res

def permute(nums: list[int]) -> list[list[int]]:
    return nums_order(nums, [], [])

def nums_order(nums: list[int], res: list[list[int]], conds: list[int]) -> list[list[int]]:
    if not nums: return res + [conds]

    count = len(nums)
    for idx in range(count):
        if idx == 0:
            res = nums_order(nums[idx + 1:], res, conds + [nums[idx]])
        elif idx == count - 1:
            res = nums_order(nums[:idx], res, conds + [nums[idx]])
        else:
            res = nums_order(nums[:idx] + nums[idx + 1:], res, conds + [nums[idx]])

    return res

def permuteUnique(nums: list[int]) -> list[list[int]]:
    nums.sort()

    return nums_order_union(nums, [], [])

def nums_order_union(nums: list[int], res: list[list[int]], conds: list[int]):
    if not nums: return res + [conds]

    count = len(nums)
    for idx in range(count):
        if idx > 0 and nums[idx] == nums[idx - 1]: continue
        if idx == 0:
            res = nums_order_union(nums[idx + 1:], res, conds + [nums[idx]])
        elif idx == count - 1:
            res = nums_order_union(nums[:idx], res, conds + [nums[idx]])
        else:
            res = nums_order_union(nums[:idx] + nums[idx + 1:], res, conds + [nums[idx]])

    return res

def generateParenthesis(n: int) -> list[str]:
    return parenthesesOrder(n, 0, 0, [], "")

def parenthesesOrder(n: int, front: int, behind: int, res: list[str], conds: str) -> list[str]:
    if front + behind == 2 * n: return res + [conds]

    if front < n:
        res = parenthesesOrder(n, front + 1, behind, res, conds + "(")
    if behind < front:
        res = parenthesesOrder(n, front, behind + 1, res, conds + ")")

    return res

def partition(s: str) -> list[list[str]]:
    count = len(s)
    dp = [[True] * count for _ in range(count)]

    for i in range(count - 1, -1, -1):
        for j in range(i + 1, count):
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

    return str_dfs(dp, s, 0, count, [], [])

def str_dfs(dp: list[list[bool]], s: str, i: int, count: int, res: list[list[str]], stack: list[str]) -> list[
    list[str]]:
    print(i, count, stack, "res: ", res)
    if i == count: return res + [res + [stack.copy()]]

    for j in range(i, count):
        if dp[i][j]:
            stack.append(s[i: j + 1])
            res = str_dfs(dp, s, j + 1, count, res, stack)
            stack.pop()

    return res

def restoreIpAddresses(s: str) -> list[str]:
    count = len(s)

    return address_dfs(s, 0, count, [], [])

def address_dfs(string: str, i: int, count: int, res: list[str], stack: list[str]):
    if i == count: return res + [".".join(stack)] if len(stack) == 4 else res
    if len(stack) == 4: return res

    if string[i] == "0":
        stack.append(string[i])
        res = address_dfs(string, i + 1, count, res, stack)
        stack.pop()
    else:
        for j in range(i, min(i + 3, count)):
            cur = int(string[i: j + 1])
            if 0 <= cur <= 255:
                stack.append(string[i: j + 1])
                res = address_dfs(string, j + 1, count, res, stack)
                stack.pop()

    return res

def minCostClimbingStairs(cost: list[int]) -> int:
    count = len(cost)
    dp = [0] * (count + 1)

    for i in range(2, count + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i  -2])

    return dp[-1]

def rob(nums: list[int]) -> int:
    count = len(nums)
    if count == 1: return nums[-1]

    dp = [0] * (count + 1)
    dp[1] = nums[0]

    for i in range(2, count + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

    return dp[-1]

def rob2(nums: list[int]) -> int:
    count = len(nums)
    if count < 3: return max(nums)

    dp1, dp2 = [0] * count, [0] * count
    dp1[1], dp2[1] = nums[0], nums[1]

    for i in range(2, count):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 1])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
    print(dp1, dp2)
    return max(dp1[-1], dp2[-1])

def minCost(costs: list[list[int]]) -> int:
    red, blue, green = 0, 0, 0

    for cr, cb, cg in costs:
        red, blue, green = min(blue + cr, green + cr), min(red + cb, green + cb), min(red + cg, blue + cg)

    return min(red, blue, green)

def minFlipsMonoIncr_1(s: str) -> int:
    dtmp = {}
    for i in s:
        dtmp[i] = dtmp.get(i, 0) + 1
    return flipCount(dtmp, 0, s)

def flipCount(d: dict, preCount: int, s: str) -> int:

    i, count = 0, len(s)
    while i < count and s[i] == "0":
        d[s[i]] -= 1
        i += 1
    if i >= count: return preCount

    flipcount = d.get("0", 0) + preCount

    preCount += 1
    if i < count: d[s[i]] -= 1

    return min(flipcount + preCount, flipCount(d, preCount, s[i + 1:]))

def minFlipsMonoIncr_2(s: str) -> int:
    count = len(s)
    dp0, dp1 = [0] * count, [0] * count
    if s[0] == "0":
        dp1[0] = 1
    else:
        dp0[0] = 1

    for i in range(1, count):
        dp0[i] = dp0[i - 1] + 1 if s[i] == "1" else dp0[i - 1]
        dp1[i] = min(dp0[i - 1], dp1[i - 1] + 1 if s[i] == "0" else dp1[i - 1])

    return min(dp0[-1], dp1[-1])

def lenLongestFibSubseq(arr: list[int]) -> int:
    res, count = 0, len(arr)

    arr_idx = {arr[i]: i for i in range(count)}
    dp = [[0] * count for _ in range(count)]
    for i in range(2, count):
        for j in range(i):
            pre = arr_idx.get(arr[i] - arr[j], -1)
            if pre != -1 and pre < j:
                dp[j][i] = max(dp[pre][j] + 1, 3)
                res = max(res, dp[j][i])
    return res

def minCut(s: str) -> int:
    count = len(s)

    dp = [[True] * count for _ in range(count)]

    for i in range(count - 1, -1, -1):
        for j in range(i + 1, count):
            dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

    res_dp = [float("+inf")] * count
    for i in range(count):
        if dp[0][i]:
            res_dp[i] = 0
        else:
            for j in range(i):
                if dp[j + 1][i]:
                    res_dp[i] = min(res_dp[i], res_dp[j] + 1)

    return res_dp[-1]

def longestCommonSubsequence(text1: str, text2: str) -> int:
    count1, count2 = len(text1) + 1, len(text2) + 1
    dp = [[0] * count2 for _ in range(count1)]

    for i in range(1, count1):
        for j in range(1, count2):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    c1, c2, c3 = len(s1), len(s2), len(s3)
    if c1 + c2 != c3: return False

    dp = [[False] * (c2 + 1) for _ in range(c1 + 1)]
    dp[0][0] = True
    for i in range(1, c2 + 1):
        if s2[i - 1] == s3[i - 1]:
            dp[0][i] = dp[0][i - 1]
    for j in range(1, c1 + 1):
        if s1[j - 1] == s3[j - 1]:
            dp[j][0] = dp[j - 1][0]

    for i in range(1, c1 + 1):
        for j in range(1, c2 + 1):
            if s1[i - 1] == s3[i + j - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif s1[i - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i - 1][j]
            elif s2[j - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j - 1]

    return dp[-1][-1]


def numDistinct(s: str, t: str) -> int:
    cs, ct = len(s), len(t)
    if cs < ct: return 0

    dp = [[0] * (ct + 1) for _ in range(cs + 1)]
    for i in range(cs + 1):
        dp[i][ct] = 1

    for i in range(cs - 1, -1, -1):
        for j in range(ct - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]

    return dp[0][0]

def uniquePaths(m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[-1][-1]


def minPathSum(grid: list[list[int]]) -> int:
    if not grid or not grid[0]: return 0

    cr, cc = len(grid), len(grid[0])
    dp = [[0] * cc for _ in range(cr)]

    for i in range(cr):
        for j in range(cc):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

    return dp[-1][-1]

def minimumTotal(triangle: list[list[int]]) -> int:
    if not triangle: return 0

    count = len(triangle)
    res, dp = float("+inf"), [[0] * (i + 1) for i in range(count)]
    for i in range(count):
        for j in range(i + 1):
            if i == 0 and j == 0:
                dp[i][j] = triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

            if i == count - 1:
                res = min(res, dp[i][j])
    return res

def canPartition(nums: list[int]) -> bool:
    count = len(nums)
    if count < 2: return False

    sums = sum(nums)
    if sums % 2: return False

    target, max_num = sums // 2, max(nums)
    if max_num > target: return False

    dp = [[False] * (target + 1) for _ in range(count)]
    for i in range(count):
        dp[i][0] = True
    dp[0][nums[0]] = True

    for i in range(1, count):
        num = nums[i]
        for j in range(1, target + 1):
            if j >= num:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][target]

def findTargetSumWays(nums: list[int], target: int) -> int:
    sums, count = sum(nums), len(nums)
    if sums - target < 0 or (sums - target) % 2: return 0

    nt = (sums - target) // 2
    dp = [[0] * (nt + 1) for _ in range(count + 1)]
    dp[0][0] = 1
    for i in range(1, count + 1):
        num = nums[i - 1]
        for j in range(nt + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - num]) if j >= num else dp[i - 1][j]

    return dp[-1][nt]

def coinChange(coins: list[int], amount: int) -> int:
    count = len(coins)
    dp = [[float("+inf")] * (amount + 1) for _ in range(count + 1)]
    dp[0][0] = 0
    for i in range(1, count + 1):
        num = coins[i - 1]
        for j in range(amount + 1):
            if j >= num:
                dp[i][j] = min(dp[i][j - num] + 1, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][amount] if dp[-1][amount] != float("+inf") else -1

def combinationSum4(nums: list[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]

    return dp[-1]

def maxAreaOfIsland(grid: list[list[int]]) -> int:
    rc, cc = len(grid), len(grid[0])
    res = 0
    for i in range(rc):
        for j in range(cc):
            cur, queue = 0, [[i, j]]
            while queue:
                row, col = queue.pop(0)
                if 0 <= row < rc and 0 <= col < cc and grid[row][col]:
                    cur += 1
                    grid[row][col] = 0
                    for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        queue.append([x + row, y + col])
            res = max(res, cur)
    return res

def isBipartite(graph: list[list[int]]) -> bool:
    nums = len(graph)
    for i in range(nums):
        dp = [0] * nums
        if dp[i] == 0 and not dfs_graph(graph, dp, i, 1):
            return False
    return True

def dfs_graph(graph, dp, idx, color):
    dp[idx] = color
    for cur in graph[idx]:
        if dp[cur] == 0:
            return dfs_graph(graph, dp, cur, dp[idx] * -1)
        if dp[idx] == dp[cur]:
            return False
    return True

def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    row, col = len(mat), len(mat[0])
    dp = [[float("+inf")] * col for _ in range(row)]
    stack, visited = [], set()
    for i in range(row):
        for j in range(col):
            if not mat[i][j]:
                stack.append([i, j, 0])
    while stack:
        cr, cc, cur = stack.pop(0)
        visited.add((cr, cc))
        dp[cr][cc] = min(dp[cr][cc], cur)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= cr + dx < row and 0 <= cc + dy < col and mat[cr + dx][cc + dy] == 1 and (cr + dx,
                                                                                             cc + dy) not in visited:
                stack.append([cr + dx, cc + dy, cur + 1])
    return dp

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    nums = len(beginWord)
    if endWord not in wordList: return 0

    idx, dtmp, edges = 0, {}, {}
    for word in set([beginWord, endWord] + wordList):
        dtmp[word] = idx
        idx += 1
        for j in range(nums):
            w = word[: j] + "*" + word[j + 1:]
            if w not in dtmp:
                dtmp[w] = idx
                idx += 1
            edges[dtmp[word]] = edges.get(dtmp[word], []) + [dtmp[w]]
            edges[dtmp[w]] = edges.get(dtmp[w], []) + [dtmp[word]]

    res, stack, end, visited = 0, [dtmp[beginWord]], dtmp[endWord], set()
    while stack:
        for _ in range(len(stack)):
            node = stack.pop(0)
            visited.add(node)

            if node == end:
                return res // 2 + 1

            for edge in edges.get(node, []):
                if edge not in visited:
                    stack.append(edge)
        res += 1

    return 0

def openLock(deadends: list[str], target: str) -> int:
    if "0000" == target: return 0
    if "0000" in deadends: return -1

    known, status, step = set(deadends), collections.deque(["0000"]), 0
    known.add("0000")

    change = {
        "0": ["1", "9"],
        "1": ["0", "2"],
        "2": ["1", "3"],
        "3": ["2", "4"],
        "4": ["3", "5"],
        "5": ["4", "6"],
        "6": ["5", "7"],
        "7": ["6", "8"],
        "8": ["7", "9"],
        "9": ["8", "0"],
    }

    while status:
        step += 1
        for _ in range(len(status)):
            cur = status.popleft()
            for i in range(4):
                for j in change[cur[i]]:
                    nex = cur[: i] + j + cur[i + 1:]
                    if nex == target:
                        return step
                    elif nex not in known:
                        status.append(nex)
                        known.add(nex)
    return -1

def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    nums = len(graph)

    res, queue = [], collections.deque()
    queue.append([[0], set()])

    while queue:
        node, known = queue.popleft()
        for nex in graph[node[-1]]:
            if nex not in known:
                node.append(nex)
                known.add(nex)
                if nex == nums - 1:
                    res.append(node.copy())
                else:
                    queue.append([node.copy(), known.copy()])
                node.pop()
                known.discard(nex)
    return res


def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    edges = {}
    for i, (s, e) in enumerate(equations):
        if s not in edges:
            edges[s] = {s: 1}
        if e not in edges:
            edges[e] = {e: 1}

        edges[s].update({e: values[i]})
        edges[e].update({s: 1 / values[i]})

    res = []
    for query in queries:
        res.append(self.bfs_query(edges, query))

    return res


def bfs_query(self, edge, query):
    s, e = query
    if s not in edge or e not in edge: return -1

    queue, known = collections.deque(), set()
    queue.append([s, 1])
    while queue:
        nd, res = queue.popleft()
        if nd == e: return res
        known.add(nd)
        for k, v in edge.get(nd, {}).items():
            if k not in known:
                queue.append([k, res * v])

    return -1

def longestIncreasingPath(matrix: list[list[int]]) -> int:
    row, col = len(matrix), len(matrix[0])
    res, dp = 1, [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            dp[i][j] = dfs_maxPath(matrix, dp, i, j, row, col)
            res = max(res, dp[i][j])
    return res

def dfs_maxPath(matrix, dp, i, j, r, c):
    if dp[i][j] != 0: return dp[i][j]

    res = 1
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        x, y = i + dx, j + dy
        if 0 <= x < r and 0 <= y < c and matrix[x][y] < matrix[i][j]:
            res = max(res, dfs_maxPath(matrix, dp, x, y, r, c) + 1)

    return res

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    edges, search = {i: [] for i in range(numCourses)}, [0] * numCourses

    for e, s in prerequisites:
        edges[e].append(s)

    queue, res = collections.deque(list(edges.keys())), []
    while queue:
        cur = queue.popleft()
        if search[cur] == 0:
            flag, res = dfs_search(edges, search, cur, res)
            if not flag: return []

    return res

def dfs_search(edges, search, node, res):
    flag, search[node] = True, 1

    for nex in edges.get(node, []):
        if search[nex] == 2:
            continue
        elif search[nex] == 1:
            return False, []
        else:
            cur_flag, res = dfs_search(edges, search, nex, res)
            flag &= cur_flag

    search[node] = 2
    res.append(node)

    return flag, res

def alienOrder(words: list[str]) -> str:
    if len(words) == 1: return words[-1]

    edges, d, s = {}, [0] * 26, set()

    for cur in words: s = s.union(set(cur))

    for a, b in zip(words, words[1:]):
        for ca, cb in zip(a, b):
            if ca != cb:
                edges[ca] = edges.get(ca, []) + [cb]
                d[ord(cb) - ord("a")] += 1
                break
        else:
            if len(a) > len(b):
                return ""

    start = [k for k in s if d[ord(k) - ord("a")] == 0]
    for cur in start:
        for nex in edges.get(cur, []):
            d[v := ord(nex) - ord("a")] -= 1
            if not d[v]:
                start.append(nex)
    return "".join(start) if len(start) == len(s) else ""

def sequenceReconstruction(nums: list[int], sequences: list[list[int]]) -> bool:
    graph, indeg = {num: [] for num in nums}, {num: 0 for num in nums}
    for sequence in sequences:
        for s, e in zip(sequence, sequence[1:]):
            graph[s].append(e)
            indeg[e] += 1

    path = collections.deque([k for k, v in indeg.items() if v == 0])
    count = len(path)
    while path:
        if len(path) > 1: return False
        cur = path.popleft()
        for nex in graph.get(cur, []):
            indeg[nex] -= 1
            if not indeg[nex]:
                path.append(nex)
                count += 1
    return count == len(indeg)

def findCircleNum(isConnected: list[list[int]]) -> int:
    count = len(isConnected)
    rank, res = [0] * count, 0

    for i in range(count):
        if dfs_city(isConnected, rank, i, count):
            res += 1

    return res

def dfs_city(isConnected, rank, idx, count):
    if rank[idx]: return False

    rank[idx] = 1
    res = True
    for j in range(count):
        if j != idx and isConnected[idx][j] == 1:
            res |= dfs_city(isConnected, rank, j, count)

    return res

def numSimilarGroups(strs: list[str]) -> int:
    count = len(strs)
    nums = list(range(count))

    for i in range(count):
        for j in range(i + 1, count):
            ii, ji = dfs_find(nums, i), dfs_find(nums, j)
            if ii == ji: continue
            if check_str(strs[i], strs[j]):
                nums[ii] = ji

    return sum([1 for i in range(count) if nums[i] == i])

def dfs_find(nums, idx):
    if nums[idx] == idx: return idx
    nums[idx] = dfs_find(nums, nums[idx])
    return nums[idx]

def check_str(sa, sb):
    if len(sa) != len(sb): return False

    res = 0
    for a, b in zip(sa, sb):
        if a != b: res += 1

    return True if not res or res == 2 else False

def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    rank, graph = list(range(len(edges) + 1)), {}

    for s, e in edges:
        graph[s] = graph.get(s, []) + [e]

    for s, e in edges:
        sc = dfs_edge(rank, s)
        ec = dfs_edge(rank, e)
        if sc == ec: return [s, e]
        else:
            rank[sc] = ec

def dfs_edge(graph, start):
    if graph[start] == start: return start

    graph[start] = dfs_edge(graph, graph[start])

    return graph[start]

def longestConsecutive(nums: list[int]) -> int:
    graph, indeg = {}, {}

    for num in nums:
        if num not in indeg:
            indeg[num] = 0
            graph[num] = []
            if num - 1 in graph:
                graph[num - 1].append(num)
                indeg[num] += 1
            if num + 1 in graph:
                graph[num].append(num + 1)
                indeg[num + 1] += 1

    starts, res = [k for k, v in indeg.items() if v == 0], 0
    while starts:
        path, idx = [starts.pop(0)], 0
        while child := graph.get(path[idx], None):
            for nex in child:
                indeg[nex] -= 1
                if not indeg[nex]:
                    path.append(nex)
            idx += 1
        res = max(res, len(path))

    return res
