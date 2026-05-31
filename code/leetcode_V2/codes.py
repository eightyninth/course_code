class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def findRepeatDocument(documents: list[int]) -> int:
    alone = set()

    for i in documents:
        if i not in alone:
            alone.add(i)
        else:
            return i

    return -1

def findTargetIn2DPlants(plants: list[list[int]], target: int) -> bool:
    if not len(plants) or not len(plants[0]): return False
    res = False
    for plant in plants:
        res = res or binary_search(plant, target)
    return res

def binary_search(plant: list[int], target: int) -> bool:
    left, right = 0, len(plant) - 1
    while left <= right:
        mid = (left + right) // 2
        if plant[mid] > target:
            right = mid - 1
        elif plant[mid] < target:
            left = mid + 1
        else:
            return True
    return False

def pathEncryption(path: str) -> str:
    cur, items = "", []

    for p in path:
        if p != ".":
            cur += p
        else:
            items.append(cur)
            cur = ""
    items.append(cur)
    return " ".join(items)

def reverseBookList_1(head):
    if not head: return []
    res = reverseBookList_1(head.next)
    return res + [head.val]

def reverseBookList_2(head):
    if not head: return []
    pre, cur = None, head
    while cur:
        nex = cur.next
        cur.next = pre
        pre, cur = cur, nex

    res = []
    while pre:
        res.append(pre.val)
        pre = pre.next

    return res

def deduceTree(preorder: list[int], inorder: list[int]):
    if not inorder: return None

    root = TreeNode(preorder.pop(0))

    left = []
    while inorder and inorder[0] != root.val: left.append(inorder.pop(0))
    if inorder: inorder.pop(0)

    root.left = deduceTree(preorder, left)
    root.right = deduceTree(preorder, inorder)

    return root


class CQueue:

    def __init__(self):

        self._in = []
        self._out = []

    def appendTail(self, value: int) -> None:
        self._in.append(value)

    def deleteHead(self) -> int:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        return self._out.pop() if self._out else -1


def fib(n: int) -> int:
    if n == 0: return 0
    pre, cur = 0, 1
    while n > 1:
        pre, cur = cur, int((cur + pre) % (1e9 + 7))
        n -= 1

    return cur

def trainWays(num: int) -> int:
    if num <= 1: return 1
    pre, cur = 1, 1
    while num > 1:
        pre, cur = cur, int((pre + cur) % (1e9 + 7))
        num -= 1
    return cur

def inventoryManagement_1(stock: list[int]) -> int:
    if len(stock) <= 1: return stock[0]

    cur = 1
    while len(stock) > cur and stock[cur - 1] <= stock[cur]:
        cur += 1

    if len(stock) <= cur:
        return stock[0]
    elif stock[cur - 1] <= stock[cur]:
        return stock[cur - 1]
    else:
        return stock[cur]

def inventoryManagement_2(stock: list[int]) -> int:
    l, r = 0, len(stock) - 1
    while l < r:
        m = (l + r) // 2
        if stock[m] < stock[r]:
            r = m
        elif stock[m] > stock[r]:
            l = m + 1
        else:
            r -= 1
    return stock[l]


def wordPuzzle(grid: list[list[str]], target: str) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if letter(i, j, 0, [], grid, target):
                return True

    return False

def letter(x, y, idx, route, grid, target):
    if idx >= len(target): return True

    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and [x, y] not in route:
        if grid[x][y] != target[idx]: return False

        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for x_d, y_d in direct:
            route.append([x, y])
            x_cur, y_cur = x + x_d, y + y_d
            if letter(x_cur, y_cur, idx + 1, route, grid, target):
                return True
            route.pop()

    return False

def wardrobeFinishing_1(m: int, n: int, cnt: int) -> int:
    return dfs(0, 0, m, n, cnt, set())

def dfs(i: int, j: int, m: int, n: int, cnt: int, count: set) -> int:
    if i < 0 or i >= m or j < 0 or j >= n or digit(i) + digit(j) > cnt or (i, j) in count: return 0

    count.add((i, j))
    return dfs(i + 1, j, m, n, cnt, count) + dfs(i, j + 1, m, n, cnt, count) + 1

def digit(x: int) -> int:
    res = 0
    while x > 0:
        tmp = x % 10
        x, res = x // 10, res + tmp

    return res

def wardrobeFinishing_2(m: int, n: int, cnt: int) -> int:
    queue, visited, res = [[0, 0]], set(), 0
    direct = [[0, 1], [1, 0]]

    while queue:
        i, j = queue.pop(0)
        if i >= m or j >= n or digit(i) + digit(j) > cnt or (i, j) in visited: continue
        res += 1
        visited.add((i, j))

        for i_d, j_d in direct:
            i_cur, j_cur = i + i_d, j + j_d
            queue.append([i_cur, j_cur])

    return res

def cuttingBamboo_1(bamboo_len: int) -> int:
    dp = [0, 0, 1]
    for i in range(3, bamboo_len + 1):
        max_ = 1
        for j in range(2, i):
            max_ = max(max_, (i - j) * j, dp[i - j] * j)
        dp.append(max_)

    return dp[-1]


def cuttingBamboo_2(bamboo_len: int) -> int:
    a, b, res = bamboo_len // 3, bamboo_len % 3, 1
    if bamboo_len <= 3:
        res = bamboo_len - 1
    elif b == 0:
        res = reminder(3, a, 1e9 + 7)
    elif b == 1:
        res = reminder(3, a - 1, 1e9 + 7) * 4 % (1e9 + 7)
    else:
        res = reminder(3, a, 1e9 + 7) * 2 % (1e9 + 7)

    return int(res)

def reminder(a: int, x: int, p: int) -> int:
    res = 1
    while x:
        res = res * a % p
        x -= 1
    return res

def hammingWeight(n: int) -> int:
    res = 0
    while n:
        if n & 1: res += 1
        n = n >> 1

    return res

def myPow(x: float, n: int) -> float:
    if x == 0 and n == 0:
        return 0
    elif x == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return x

    res = myPow(x if n > 0 else 1 / x, n // 2 if n > 0 else (- n) // 2)
    res = res * res
    if n % 2 and n > 0:
        res = res * x
    elif n % 2 and n < 0:
        res = res / x

    return res

def countNumbers(cnt: int) -> list[int]:
    if cnt < 1: return []
    i, j, res = 1, 10, []
    while cnt:
        for k in range(i, j):
            res.append(k)
        i, j = j, j * 10
        cnt -= 1

    return res

def deleteNode(head: ListNode, val: int) -> ListNode:
    if not head: return head

    new_head = ListNode(-1, head)
    pre, cur = new_head, new_head.next
    while cur and cur.val != val:
        pre, cur = cur, cur.next

    if cur: pre.next = cur.next

    return new_head.next

def articleMatch(s: str, p: str) -> bool:
    row, column = len(s), len(p)
    dp = [[False for _ in range(column + 1)] for _ in range(row + 1)]

    dp[0][0] = True
    for k in range(1, column + 1):
        if p[k - 1] == "*":
            dp[0][k] = dp[0][k - 2]

    for i in range(1, row + 1):
        for j in range(1, column + 1):
            # 情况1 p[j - 1] 为 "*"
            if p[j - 1] == "*":
                dp[i][j] =  dp[i][j - 2]
                if s[i - 1] == p[j - 2] or p[j  -2] == ".": dp[i][j] |= dp[i - 1][j]
            # 情况1 p[j- 1] 为 "."
            # 情况2 p[j - 1] 为 具体字符, 且p[j - 1] == s[i - 1]
            elif p[j - 1] == "." or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[-1][-1]

def validNumber(s: str) -> bool:
    dp = [
        {" ": 0, ".": 4, "s": 1, "d": 2},
        {".": 4, "d": 2},
        {"d": 2, ".": 3, "e": 5, " ": 8},
        {"d": 3, "e": 5, " ": 8},
        {"d": 3},
        {"s": 6, "d": 7},
        {"d": 7},
        {"d": 7, " ": 8},
        {" ": 8}
    ]

    p = 0
    for c in s:
        if "0" <= c <= "9":
            t = "d"
        elif c == "+" or c == "-":
            t = "s"
        elif c == "e" or c == "E":
            t = "e"
        elif c == "." or c == " ":
            t = c
        else:
            t = "?"
        if t not in dp[p]: return False
        p = dp[p][t]

    return p in (2, 3, 7, 8)

def trainingPlan_1(actions: list[int]) -> list[int]:
    i, j = 0, len(actions) - 1
    while i < j:
        while i < j and actions[i] % 2: i += 1
        while i < j and not actions[j] % 2: j -= 1
        actions[i], actions[j] = actions[j], actions[i]

    return actions

def trainingPlan_2(head: ListNode, cnt: int) -> ListNode:
    node, _ = node_dfs(head, cnt)
    return node

def node_dfs(self, head: ListNode, cnt: int) -> (ListNode, int):
    if not head: return None, 0
    node, cur = self.node_dfs(head.next, cnt)
    cur += 1
    return head if cur == cnt else node, cur

def trainingPlan_3(head: ListNode) -> ListNode:
    if not head: return head
    pre, cur = None, head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre, cur = cur, tmp
    return pre

def trainningPlan_4(l1: ListNode, l2: ListNode) -> ListNode:
    new_head = ListNode(-1)
    res = new_head

    while l1 and l2:
        if l1.val < l2.val:
            new_head.next = l1
            new_head, l1 = new_head.next, l1.next
        else:
            new_head.next = l2
            new_head, l2 = new_head.next, l2.next

    while l1:
        new_head.next = l1
        new_head, l1 = new_head.next, l1.next

    while l2:
        new_head.next = l2
        new_head, l2 = new_head.next, l2.next

    return res.next

def isSubStructure(A: TreeNode, B: TreeNode) -> bool:

    return bool(A and B) and (
                dfs_tree(A, B) or isSubStructure(A.left, B) or isSubStructure(A.right, B))

def dfs_tree(A: TreeNode, B: TreeNode) -> bool:
    if not B: return True
    if not A or A.val != B.val: return False

    return dfs_tree(A.left, B.left) and dfs_tree(A.right, B.right)

def flipTree(root: TreeNode) -> TreeNode:
    # 后序遍历
    if not root: return root
    root.right, root.left = flipTree(root.left), flipTree(root.right)
    return root

def checkSymmetricTree(root: TreeNode) -> bool:
    return not root or dfs_tree_2(root.left, root.right)

def dfs_tree_2(a: TreeNode, b: TreeNode) -> bool:
    if (a and not b) or (not a and b):
        return False
    elif not a and not b:
        return True
    return a.val == b.val and dfs_tree_2(a.left, b.right) and dfs_tree_2(a.right, b.left)

def spiralArray(array: list[list[int]]) -> list[int]:
    if not array or not array[0]: return []

    r, c, r_e, c_e, res = 0, 0, len(array) - 1, len(array[0]) - 1, []

    while True:
        # 向右
        for i in range(c, c_e + 1): res.append(array[r][i])
        r += 1
        if r > r_e: break
        # 向下
        for i in range(r, r_e + 1): res.append(array[i][c_e])
        c_e -= 1
        if c > c_e: break
        # 向左
        for i in range(c_e, c - 1, -1): res.append(array[r_e][i])
        r_e -= 1
        if r > r_e: break
        # 向上
        for i in range(r_e, r - 1, -1): res.append(array[i][c])
        c += 1
        if c > c_e: break

    return res


class MinStack_1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_ = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if self.min_:
            tmp = []
            while self.min_ and self.min_[-1] < x: tmp.append(self.min_.pop())
            self.min_.append(x)
            while tmp: self.min_.append(tmp.pop())
        else:
            self.min_.append(x)

    def pop(self) -> None:
        x = self.stack.pop()

        tmp = []
        while self.min_ and self.min_[-1] != x: tmp.append(self.min_.pop())
        self.min_.pop()
        while tmp: self.min_.append(tmp.pop())

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]


class MinStack_2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_ = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.min_ or self.min_[-1] >= x: self.min_.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if self.min_[-1] == x: self.min_.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]

def validateBookSequences_1(putIn: list[int], takeOut: list[int]) -> bool:
    if not putIn: return True
    j, stack = 0, []
    for i in putIn:
        if i != takeOut[j]:
            stack.append(i)
        else:
            j += 1
            while j < len(takeOut) and stack and stack[-1] == takeOut[j]:
                stack.pop()
                j += 1

    return False if stack else True

def decorateRecord_1(root: TreeNode) -> list[int]:
    if not root: return []
    res, queue = [], [root]

    while queue:
        cur = queue.pop(0)

        res.append(cur.val)

        if cur.left: queue.append(cur.left)
        if cur.right: queue.append(cur.right)

    return res

def decorateRecord_2(root: TreeNode) -> list[list[int]]:
    if not root: return []

    res, queue = [], [[root]]

    while queue:
        cur_queue, next_queue, cur_res = queue.pop(0), [], []
        while cur_queue:
            cur = cur_queue.pop(0)
            cur_res.append(cur.val)
            if cur.left: next_queue.append(cur.left)
            if cur.right: next_queue.append(cur.right)
        if next_queue: queue.append(next_queue)
        res.append(cur_res)

    return res

def decorateRecord_3(root: TreeNode) -> list[list[int]]:
    if not root: return []

    res, queue, flag = [], [root], 1
    while queue:
        cur_res = []
        for _ in range(len(queue)):
            cur = queue.pop(0)
            cur_res.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)

        if flag == 1:
            res.append(cur_res)
        else:
            res.append(cur_res[::-1])

        flag *= -1
    return res

def decorateRecord_4(root: TreeNode) -> list[list[int]]:
    if not root: return []

    res, queue = [], [root]
    while queue:
        cur_res = []
        for _ in range(len(queue)):
            cur = queue.pop(0)
            if len(res) % 2:
                cur_res.insert(0, cur.val)
            else:
                cur_res.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)

        res.append(cur_res)

    return res

def verifyTreeOrder_1(postorder: list[int]) -> bool:
    return postTree_1(postorder, 0, len(postorder) - 1)

def postTree_1(postorder: list[int], i: int, j: int) -> bool:
    if i >= j: return True

    root = postorder[j]
    k = j - 1
    while k >= i and postorder[j] < postorder[k]: k -= 1

    for l in range(i, k + 1):
        if postorder[j] < postorder[l]:
            return False

    for r in range(k + 1, j):
        if postorder[r] < postorder[j]:
            return False

    return postTree_1(postorder, i, k) and postTree_1(postorder, k + 1, j - 1)

def verifyTreeOrder_2(postorder: list[int]) -> bool:
    return postTree_2(postorder, 0, len(postorder) - 1)

def postTree_2(postorder: list[int], i: int, j: int) -> bool:
    if i >= j: return True

    l = i
    while postorder[l] < postorder[j]: l += 1
    r = l
    while postorder[r] > postorder[j]: r += 1

    return r == j and postTree_2(postorder, i, l - 1) and postTree_2(postorder, l, j - 1)

def verifyTreeOrder_3(postorder: list[int]) -> bool:
    root, stack = float("+inf"), []

    for i in range(len(postorder) - 1, -1, -1):
        if postorder[i] > root: return False

        while stack and postorder[i] < stack[-1]:
            root = stack.pop()

        stack.append(postorder[i])

    return True


def pathTarget(root: TreeNode, target: int) -> list[list[int]]:
    if not root:
        return []
    elif not root.left and not root.right:
        return [] if root.val != target else [[root.val]]

    target -= root.val
    left = pathTarget(root.left, target)
    right = pathTarget(root.right, target)

    res = []
    if left:
        for l in left: res.append([root.val] + l)
    if right:
        for r in right: res.append([root.val] + r)
    return res

def copyRandomList_1(head: 'Node') -> 'Node':
    if not head: return head
    num, cur_node = 0, head
    new_head = cur = Node(-1, head, None)

    while cur_node:
        tmp = Node(cur_node.val)
        cur.next = tmp
        cur, cur_node = cur.next, cur_node.next
        num += 1

    cur = new_head.next
    while head:
        tmp, i = head.random, 0
        while tmp:
            tmp = tmp.next
            i += 1
        random, i = new_head.next, num - i
        while i > 0:
            random = random.next
            i -= 1
        cur.random = random
        cur, head = cur.next, head.next

    return new_head.next

def copyRandomList_2(head: 'Node') -> 'Node':
    if not head: return head
    node_dict, cur_node = {}, head

    while cur_node:
        node_dict[cur_node] = Node(cur_node.val)
        cur_node = cur_node.next

    cur = head
    while cur:
        node_dict[cur].next, node_dict[cur].random = node_dict.get(cur.next), node_dict.get(cur.random)
        cur = cur.next

    return node_dict[head]

def treeToDoublyList_1(root: 'TreeNode') -> 'TreeNode':
    if not root: return root
    # 中序遍历
    res = midOrder_1(root)

    cur = new_head = Node(-1)
    for node in res:
        cur.right, node.left = node, cur
        cur = cur.right
    new_head.right.left, cur.right = cur, new_head.right
    return new_head.right

def midOrder_1(root: 'TreeNode') -> 'TreeNode':
    if not root:
        return []
    elif not root.left and not root.right:
        return [root]

    return midOrder_1(root.left) + [root] + midOrder_1(root.right)

pre, head = None, None
def treeToDoublyList_2(root: 'TreeNode') -> 'TreeNode':
    global pre, head
    if not root: return root

    # 中序遍历
    midOrder_2(root)

    head.left, pre.right = pre, head
    return head

def midOrder_2(root: 'TreeNode') -> None:
    global pre, head
    if not root: return
    midOrder_2(root.left)
    if pre:
        pre.right, root.left = root, pre
    else:
        head = root
    pre = root
    midOrder_2(root.right)


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return "[]"
        res_list, stack = [], [root]
        while stack:
            cur = stack.pop(0)
            if cur != "null":
                res_list.append(str(cur.val))
                stack.append(cur.left if cur.left else "null")
                stack.append(cur.right if cur.right else "null")
            else:
                res_list.append(cur)

        while res_list and res_list[-1] == "null": res_list.pop()

        return "[" + ",".join(res_list) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data[1: -1]: return
        data = data[1:-1].split(",")

        head = TreeNode(int(data.pop(0)))
        stack = [head]

        while stack:
            cur = stack.pop(0)

            # 无子树
            if not data: break
            left = data.pop(0)
            if left != "null":
                cur.left = TreeNode(int(left))
                stack.append(cur.left)
            else:
                cur.left = None

            # 无右子树
            if not data: break
            right = data.pop(0)
            if right != "null":
                cur.right = TreeNode(int(right))
                stack.append(cur.right)
            else:
                cur.right = None

        return head


def goodsOrder(goods: str) -> list[str]:
    if len(goods) == 1: return [goods]

    hset, res = set(), []
    for i, c in enumerate(goods):
        if c not in hset:
            cur_res = goodsOrder(goods[: i] + goods[i + 1:])
            hset.add(c)
            if cur_res:
                for cur in cur_res:
                    res.append(c + cur)
            else:
                res.append(c)

    return res

def inventoryManagement_3(stock: list[int]) -> int:
    num, d = len(stock) // 2, {}
    for i in stock:
        d[i] = d.get(i, 0) + 1

    for k, v in d.items():
        if v > num:
            return k

def inventoryManagement_4(stock: list[int], cnt: int) -> list[int]:
    quickSort(stock, 0, len(stock) - 1)
    return stock[0: cnt]

def quickSort(stock: list[int], i: int, j: int):
    if j - i < 1: return

    m, n = i, j
    while n > m:
        while n > m and stock[m] <= stock[j]: m += 1
        while n > m and stock[n] >= stock[j]: n -= 1
        stock[n], stock[m] = stock[m], stock[n]

    stock[j], stock[n] = stock[n], stock[j]
    quickSort(stock, i, n - 1)
    quickSort(stock, n, j)

def inventoryManagement_5(stock: list[int], cnt: int) -> list[int]:
    if cnt == 0: return []

    heap = RootHeap(stock, max_=cnt)

    return heap.heap


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 较小部分放大顶堆, 较大部分放小顶堆
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        max_, min_ = self.min_heap[0] if self.min_heap else float("+inf"), self.max_heap[0] if self.min_heap else float(
            "-inf")

        if min_ <= num <= max_ or num <= min_:
            self.max_heap.append(num)
            self.max_sort_up(len(self.max_heap) - 1)
        else:
            self.min_heap.append(num)
            self.min_sort_up(len(self.min_heap) - 1)

        max_num, min_num = len(self.max_heap), len(self.min_heap)
        tmp_num = abs(max_num - min_num)

        if max_num > min_num:
            while self.max_heap and tmp_num > 1:
                cur = self.max_heap.pop(0)
                self.min_heap.append(cur)
                self.min_sort_up(len(self.min_heap) - 1)

                if self.max_heap:
                    down = self.max_heap.pop()
                    self.max_heap.insert(0, down)
                    self.max_sort_down(0)
                tmp_num -= 1

        else:
            while self.min_heap and tmp_num > 1:
                cur = self.min_heap.pop(0)
                self.max_heap.append(cur)
                self.max_sort_up(len(self.max_heap) - 1)

                if self.min_heap:
                    down = self.min_heap.pop()
                    self.min_heap.insert(0, down)
                    self.min_sort_down(0)
                tmp_num -= 1

    def max_sort_up(self, idx: int) -> None:
        parent = (idx - 1) // 2

        if parent >= 0 and self.max_heap[parent] < self.max_heap[idx]:
            self.max_heap[parent], self.max_heap[idx] = self.max_heap[idx], self.max_heap[parent]
            self.max_sort_up(parent)

    def min_sort_up(self, idx: int) -> None:
        parent = (idx - 1) // 2

        if parent >= 0 and self.min_heap[parent] > self.min_heap[idx]:
            self.min_heap[parent], self.min_heap[idx] = self.min_heap[idx], self.min_heap[parent]
            self.min_sort_up(parent)

    def max_sort_down(self, idx: int):
        num = len(self.max_heap)
        if idx >= num: return

        cur, left, right = idx, 2 * idx + 1, 2 * idx + 2
        if left < num and self.max_heap[left] > self.max_heap[cur]:
            cur = left
        if right < num and self.max_heap[right] > self.max_heap[cur]:
            cur = right
        if idx != cur:
            self.max_heap[cur], self.max_heap[idx] = self.max_heap[idx], self.max_heap[cur]
            self.max_sort_down(cur)

    def min_sort_down(self, idx: int):
        num = len(self.min_heap)
        if idx >= num: return

        cur, left, right = idx, 2 * idx + 1, 2 * idx + 2
        if left < num and self.min_heap[left] < self.min_heap[cur]:
            cur = left
        if right < num and self.min_heap[right] < self.min_heap[cur]:
            cur = right
        if idx != cur:
            self.min_heap[cur], self.min_heap[idx] = self.min_heap[idx], self.min_heap[cur]
            self.min_sort_down(cur)

    def findMedian(self) -> float:
        max_num, min_num = len(self.max_heap), len(self.min_heap)
        if max_num == min_num:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        elif max_num > min_num:
            return self.max_heap[0]
        else:
            return self.min_heap[0]

class RootHeap:
    def __init__(self, int_list: list[int], max_: int):
        self.heap = []
        self.max_ = max_ + 1
        for i in int_list:
            self.add(i)

    def add(self, num: int):
        self.heap.append(num)
        self.sort_up(len(self.heap) - 1)
        if self.max_ == len(self.heap):
            self.pop()

    def pop(self) -> int:
        if not self.heap: return -1
        res = self.heap.pop(0)

        if self.heap:
            cur = self.heap.pop()
            self.heap.insert(0, cur)
            self.sort_down(0)
        return res

    def sort_down(self, idx: int):
        nums = len(self.heap)
        if idx >= nums: return

        cur, left, right = idx, idx * 2 + 1, idx * 2 + 2
        if left < nums and self.heap[left] > self.heap[cur]:
            cur = left
        if right < nums and self.heap[right] > self.heap[cur]:
            cur = right
        if cur != idx:
            self.heap[cur], self.heap[idx] = self.heap[idx], self.heap[cur]
            self.sort_down(cur)

    def sort_up(self, idx: int):
        cur = (idx - 1) // 2

        if cur >= 0 and self.heap[cur] < self.heap[idx]:
            self.heap[idx], self.heap[cur] = self.heap[cur], self.heap[idx]
            self.sort_up(cur)

def maxSales(self, sales: list[int]) -> int:
    dp, res = [], float("-inf")

    for s in sales:
        if not dp or dp[-1] < 0:
            dp.append(s)
        else:
            dp.append(s + dp[-1])
        res = max(res, dp[-1])
    return res

def digitOneInNumber(num: int) -> int:
    digit, res = 1, 0
    high, cur, low = num // 10, num % 10, 0
    while high != 0 or cur != 0:
        if cur == 0:
            res += digit * high
        elif cur == 1:
            res += digit * high + low + 1
        else:
            res += digit * (high + 1)

        low += cur * digit
        cur = high % 10
        high //= 10
        digit *= 10

    return res

def findKthNumber_1(k: int) -> int:
    digit, cur, i = 1, 1, 1
    while cur + 9 * digit * i <= k:
        cur += 9 * digit * i
        digit *= 10
        i += 1

    tmp, res = digit, []
    while tmp != 0:
        res.append(tmp % 10)
        tmp //= 10

    j = len(res) - 1
    while j >= 0 and digit != 0 and cur <= k:
        while res[j] < 10 and cur + i * digit <= k:
            cur += i * digit
            res[j] += 1
        j -= 1
        digit //= 10

    j = len(res) - 1
    while j >= 0 and cur < k:
        cur += 1
        j -= 1
    return res[j]

def findKthNumber(k: int) -> int:
    digit, start, count = 1, 1, 9
    while k > count:
        k -= count
        start *= 10
        digit += 1
        count = 9 * start * digit

    num = start + (k - 1) // digit
    return int(str(num)[(k - 1) % digit])

def crackPassword(password: list[int]) -> str:
    if not password: return ""
    password = [str(p) for p in password]
    quickSortStr(password, 0, len(password) - 1)
    return "".join(password)

def quickSortStr(password: list[str], i: int, j: int) -> None:
    if i >= j: return

    m, n = i, j
    while m < n:
        while m < n and password[m] + password[j] <= password[j] + password[m]: m += 1
        while m < n and password[n] + password[j] >= password[j] + password[n]: n -= 1
        password[m], password[n] = password[n], password[m]

    password[j], password[n] = password[n], password[j]
    quickSortStr(password, i, n - 1)
    quickSortStr(password, n, j)

def crackNumber_1(ciphertext: int) -> int:
    ciphertext = str(ciphertext)
    if not ciphertext: return 0
    return dfsStr(ciphertext)

def dfsStr(ciphertext: str) -> int:
    if not ciphertext: return 1

    nums = len(ciphertext)
    res = dfsStr(ciphertext[1:])
    if nums > 1 and "10" <= ciphertext[:2] <= "25":
        res += dfsStr(ciphertext[2:])

    return res

def crackNumber_2(ciphertext: int) -> int:
    ciphertext = str(ciphertext)
    if not ciphertext: return 0
    f_i_2, f_i_1 = 1, 1
    for i in range(1, len(ciphertext)):
        f_i = f_i_1 + f_i_2 if "10" <= ciphertext[i - 1: i + 1] <= "25" else f_i_1
        f_i_2, f_i_1 = f_i_1, f_i

    return f_i_1

def jewelleryValue(frame: list[list[int]]) -> int:
    if not frame or not frame[0]: return 0

    row, colnum = len(frame), len(frame[0])
    dp = [[0] * colnum] * row
    dp[0][0] = frame[0][0]

    for i in range(row):
        for j in range(colnum):
            up = dp[i - 1][j] if i > 0 else 0
            left = dp[i][j - 1] if j > 0 else 0

            dp[i][j] = frame[i][j] + max(up, left)

    return dp[-1][-1]

def dismantlingAction_1(arr: str) -> int:
    count = len(arr)
    if count <= 1: return count

    i, j, tmp, res = 0, 0, set(), 1
    while j < count:
        while i < j and arr[j] in tmp:
            tmp.remove(arr[i])
            i += 1
        res = max(res, j - i + 1)
        tmp.add(arr[j])
        j += 1

    return res

def nthUglyNumber_1(n: int) -> int:
    if n <= 1: return 1

    dp, heap = [], [1]

    while n > 0:
        cur = heap.pop(0)
        if heap:
            tail = heap.pop()
            heap.insert(0, tail)
            sort_down(heap, 0)

        dp.append(cur)
        n -= 1

        for x in [2, 3, 5]:
            if cur * x not in heap:
                heap.append(cur * x)
                sort_up(heap, len(heap) - 1)
    return dp[-1]

def sort_up(heap: list[int], idx: int) -> None:
    if idx < 0: return

    parent = (idx - 1) // 2
    if parent >= 0 and heap[parent] > heap[idx]:
        heap[parent], heap[idx] = heap[idx], heap[parent]
        sort_up(heap, parent)

def sort_down(heap: list[int], idx: int) -> None:
    num = len(heap)
    if idx >= num: return

    cur, left, right = idx, idx * 2 + 1, idx * 2 + 2
    if num > left and heap[cur] > heap[left]:
        cur = left
    if num > right and heap[cur] > heap[right]:
        cur = right

    if cur != idx:
        heap[cur], heap[idx] = heap[idx], heap[cur]
        sort_down(heap, cur)

def nthUglyNumber_2(n: int) -> int:
    if n <= 1: return 1

    dp = [1]
    a, b, c = 0, 0, 0
    while n > 1:
        cur = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
        dp.append(cur)
        if dp[a] * 2 == cur: a += 1
        if dp[b] * 3 == cur: b += 1
        if dp[c] * 5 == cur: c += 1
        n -= 1
    return dp[-1]

def dismantlingAction_2(arr: str) -> str:
    stack, str_set = [], set()

    for a in arr:
        if a not in str_set:
            stack.append(a)
            str_set.add(a)
        else:
            tmp = []
            while stack and stack[-1] != a: tmp.append(stack.pop())
            if stack: stack.pop()
            while tmp: stack.append(tmp.pop())
    return stack[0] if stack else " "

def reversePairs_1(record: list[int]) -> int:
    if len(record) < 2: return 0
    return mergeSort(record, 0, len(record) - 1)

def mergeSort(record: list[int], i: int, j: int) -> int:
    if i >= j: return 0

    mid = (i + j) // 2
    res = mergeSort(record, i, mid) + mergeSort(record, mid + 1, j)

    m, n, tmp = i, mid + 1, [0] * len(record)
    tmp[i: j + 1] = record[i: j + 1]
    for k in range(i, j + 1):
        if m == mid + 1:
            record[k] = tmp[n]
            n += 1
        elif n == j + 1 or tmp[m] <= tmp[n]:
            record[k] = tmp[m]
            m += 1
        else:
            record[k] = tmp[n]
            n += 1
            res += mid - m + 1

    return res

def reversePairs_2(record: list[int]) -> int:
    if len(record) < 2: return 0

    ltmp, res = [record[0]], 0
    for i in range(1, len(record)):
        m, n, k = 0, i - 1, (i - 1) // 2
        while m < n:
            if ltmp[k] < record[i]:
                n = k - 1
            elif ltmp[k] > record[i]:
                m = k + 1
            else:
                n -= 1
            k = (m + n) // 2

        if ltmp[m] <= record[i]:
            ltmp.insert(m, record[i])
            res += m
        else:
            ltmp.insert(m + 1, record[i])
            res += m + 1

    return res

def getIntersectionNode_1(headA: ListNode, headB: ListNode) -> ListNode:
    numA, numB, curA, curB = 0, 0, headA, headB
    while curA:
        curA = curA.next
        numA += 1
    while curB:
        curB = curB.next
        numB += 1

    curA, curB = headA, headB
    if numA > numB:
        while curA and numA > numB:
            curA  = curA.next
            numA -= 1
    elif numA < numB:
        while curB and numA < numB:
            curB  = curB.next
            numB -= 1

    while curA and curB and curA != curB:
        curA = curA.next
        curB = curB.next
    return curA

def getIntersectionNode_2(headA: ListNode, headB: ListNode) -> ListNode:
    curA, curB = headA, headB

    while curA != curB:
        curA = curA.next if curA else headB
        curB = curB.next if curB else headA

    return curA

def countTarget(scores: list[int], target: int) -> int:
    i, j, m = 0, len(scores) - 1, (len(scores) - 1) // 2
    while i < j and (scores[i] != target or scores[j] != target):
        if scores[m] > target:
            j = m - 1
        elif scores[m] < target:
            i = m + 1
        else:
            if scores[j] == target:
                i += 1
            else:
                j -= 1
        m = (i + j) // 2

    return j - i + 1 if j > i or (j == i and scores[i] == target) else 0

def takeAttendance(records: list[int]) -> int:
    i, j, m = 0, len(records) - 1, (len(records) - 1) // 2
    while i <= j:
        if records[m] != m:
            j = m - 1
        else:
            i = m + 1
        m = (i + j) // 2

    return i

def findTargetNode(root: TreeNode, cnt: int) -> int:
    _, res = dfs_rcl(root, cnt)
    return res

def dfs_rcl(root: TreeNode, cnt: int):
    # 右根左遍历
    if not root: return cnt, -1
    cur, rres = dfs_rcl(root.right, cnt)
    if rres != -1: return cur, rres

    cur -= 1
    if cur == 0: return 0, root.val

    cur, lres = dfs_rcl(root.left, cur)

    return cur, lres

def calculateDepth(root: TreeNode) -> int:
    if not root: return 0
    dp, count = [[root]], 0
    while dp:
        cur_level, tmp = dp.pop(), []
        count += 1
        while cur_level:
            cur = cur_level.pop()
            if cur.left != None: tmp.append(cur.left)
            if cur.right != None: tmp.append(cur.right)
        if tmp: dp.append(tmp)

    return count

def isBalanced_1(root: TreeNode) -> bool:
    if not root: return True
    left = treeLevel(root.left)
    right = treeLevel(root.right)

    return abs(left - right) < 2 and isBalanced_1(root.left) and isBalanced_1(root.right)

def treeLevel(root: TreeNode) -> int:
    if not root: return 0
    return max(treeLevel(root.left), treeLevel(root.right)) + 1

def isBalanced_2(root: TreeNode) -> bool:

    return dfs_rlc(root) != -1

def dfs_rlc(root: TreeNode) -> int:
    if not root: return 0

    left = dfs_rlc(root.left)
    if left == -1: return -1
    right = dfs_rlc(root.right)
    if right == -1: return -1

    return max(left, right) + 1 if abs(left - right) < 2 else -1

def sockCollocation(sockets: list[int]) -> list[int]:
    a, b, m, n = 0, 0, 0, 1
    for s in sockets:
        m ^= s

    while m & n == 0:
        n <<= 1

    for s in sockets:
        if s & n == 0:
            a ^= s
        else:
            b ^= s

    return a, b

def trainingPlan_4(actions: list[int]) -> int:
    one, two = 0, 0
    for a in actions:
        one = one ^ a & ~two
        two = two ^ a & ~one
    return one

def fileCombination_1(target: int) -> list[list[int]]:
    res, dp, i, j, count = [], list(range(1, (target + 1)// 2 + 1)), 0, 0, 0
    while j < len(dp):
        while j < len(dp) and count < target:
            count += dp[j]
            j += 1
        while i < j and count > target:
            count -= dp[i]
            i += 1
        if count == target:
            res.append(dp[i: j])
        if j < len(dp):
            count += dp[j]
            j += 1
    while i < j and count > target:
        count -= dp[i]
        i += 1
    if count == target:
        res.append(dp[i: j])
    return res

def fileCombination_2(target: int) -> list[list[int]]:
    res, dp, i, j, count = [], [1, 2], 0, 1, 3
    while i < j:
        if count == target:
            res.append(dp[i: j + 1])
        if count >= target:
            count -= dp[i]
            i += 1
        else:
            j += 1
            count += j + 1
            dp.append(j + 1)
    return res

def twoSum_1(price: list[int], target: int) -> list[int]:
    i, j = 0, len(price) - 1
    while i < j and price[i] + price[j] != target:
        if price[i] + price[j] < target:
            i += 1
        elif price[i] + price[j] > target:
            j -= 1

    return [price[i], price[j]] if i != j and price[i] + price[j] == target else []

def reverseMessage(message: str) -> str:
    i, j, res = 0, 0, []
    for k in range(len(message)):
        if message[k] != " ":
            j += 1
        else:
            while i < j and message[i] == " ":
                i += 1

            if i < j:
                res.append(message[i: j])

            i = j = k + 1

    if i < j:
        res.append(message[i: j])
    return " ".join(res[::-1])

def dynamicPassword(password: str, target: int) -> str:
    return password[target:] + password[:target]

def maxAltitude_1(heights: list[int], limit: int) -> list[int]:
    i, j, count, stack, res = 0, 0, len(heights), [], []

    while j < count:
        tmp = []
        while stack and stack[-1] > heights[j]: tmp.append(stack.pop())
        stack.append(heights[j])
        while tmp: stack.append(tmp.pop())

        if j - i + 1 == limit:
            res.append(stack[-1])
            tmp = []
            while stack and stack[-1] != heights[i]: tmp.append(stack.pop())
            if stack: stack.pop()
            while tmp: stack.append(tmp.pop())

            i += 1

        j += 1

    return res

def maxAltitude_2(heights: list[int], limit: int) -> list[int]:
    i, j, count, queue, res = 0, 0, len(heights), [], []

    while j < count:
        while queue and queue[-1] < heights[j]: queue.pop()
        queue.append(heights[j])

        if j - i + 1 == limit:
            res.append(queue[0])
            if queue[0] == heights[i]:
                queue.pop(0)
            i += 1

        j += 1

    return res


class Checkout:

    def __init__(self):
        self.queue = []
        self.max_queue = []

    def get_max(self) -> int:
        return self.max_queue[0] if self.max_queue else -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        while self.max_queue and self.max_queue[-1] < value: self.max_queue.pop()
        self.max_queue.append(value)

    def remove(self) -> int:
        if not self.queue: return -1

        cur = self.queue.pop(0)
        if cur == self.max_queue[0]:
            self.max_queue.pop(0)

        return cur

def statisticsProbability(self, num: int) -> list[float]:
    dp = [1 / 6] * 6
    for n in range(2, num + 1):
        tmp = [0] * (5 * n + 1)
        for j in range(len(dp)):
            for k in range(6):
                tmp[j + k] += dp[j] / 6
        dp = tmp
    return dp

def checkDynasty_1(places: list[int]) -> bool:
    quickSort(places, 0, len(places) - 1)
    i, count, tmp = 0, len(places), 0
    while i < count and places[i] == 0:
        i += 1
        tmp += 1

    j = i + 1
    while j < count:
        cur = places[j] - 1
        if places[i] > cur: return False
        while cur != places[i] and tmp != 0:
            cur -= 1
            tmp -= 1
        if cur != places[i] and tmp == 0: return False
        i += 1
        j += 1

    return True

def checkDynasty_2(places: list[int]) -> bool:
    dtmp, max_, min_ = set(), float("-inf"), float("+inf")
    for p in places:
        if p != 0:
            if p in dtmp: return False
            dtmp.add(p)
            if p > max_: max_ = p
            if p < min_: min_ = p
    return max_ - min_ < 5

def iceBreakingGame_1(num: int, target: int) -> int:
    ltmp, i = list(range(num)), 0

    while num > 1:
        i = (i + target - 1) % len(ltmp)
        ltmp.pop(i)
        num -= 1

    return ltmp[0]

def iceBreakingGame_2(num: int, target: int) -> int:
    res = 0
    for i in range(2, num + 1):
        res = (res + target) % i
    return res

def bestTiming(prices: list[int]) -> int:
    count = len(prices)
    if count < 2: return 0

    res, min_ = 0, prices[0]
    for i in range(1, count):
        res = max(res, prices[i] - min_)
        min_ = min(prices[i], min_)

    return res

def mechanicalAccumulator(target: int) -> int:
    return target and (target + mechanicalAccumulator(target - 1))

def encryptionCalculate(dataA: int, dataB: int) -> int:
    x = 0xffffffff
    dataA, dataB = dataA & x, dataB & x
    while dataB != 0:
        dataA, dataB = dataA ^ dataB, (dataA & dataB) << 1 & x

    return dataA if dataA <= 0x7fffffff else ~(dataA ^ x)

def statisticalResult(arrayA: list[int]) -> list[int]:
    res, tmp = [1] * len(arrayA), 1
    for i in range(1, len(arrayA)):
        res[i] *= res[i - 1] * arrayA[i - 1]
    for i in range(len(arrayA) - 2, -1, -1):
        tmp *= arrayA[i + 1]
        res[i] *= tmp

    return res

def myAtoi_1(s: str) -> int:

    res, flag = 0, 0
    for i in s:
        if i == "+" or i == "-":
            if flag == 0:
                flag = 1 if i == "+" else -1
            else:
                break
        elif "0" <= i <= "9":
            if flag == 0: flag = 1
            res = res * 10 + int(i)
        elif i != " " and flag == 0:
            break
        elif (i > "9" or i < "0") and flag != 0:
            break

    res = res * flag if flag != 0 else res
    if res >= 2 ** 31 - 1:
        res = 2 ** 31 - 1
    elif res <= - 2 ** 31:
        res = - 2 ** 31
    return res

def myAtoi_2(s: str) -> int:
    i, res, count, flag = 0, 0, len(s), 0

    # 删除首部空格
    while i < count and s[i] == " ": i += 1
    if i >= count: return res

    # 判断首个遇到的字符
    if s[i] in "+-":
        flag = 1 if s[i] == "+" else -1
        i += 1
    elif "0" <= s[i] <= "9":
        flag == 1
    else:
        return res

    while i < count and "0" <= s[i] <= "9":
        res = res * 10 + ord(s[i]) - ord("0")
        i += 1

    res = res * flag if flag != 0 else res
    if res >= 2 ** 31 - 1:
        res = 2 ** 31 - 1
    elif res <= - 2 ** 31:
        res = - 2 ** 31
    return res

def lowestCommonAncestor_1(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    pT, qT = dfs_root(root, p), dfs_root(root, q)

    pCount, qCount, i, res = len(pT), len(qT), 0, None

    while i < pCount and i < qCount and pT[i] == qT[i]:
        res = pT[i]
        i += 1

    return res

def dfs_root(root: 'TreeNode', target: "TreeNode") -> list["TreeNode"]:
    if not root: return []
    elif root == target: return [root]

    left = dfs_root(root.left, target)
    right = dfs_root(root.right, target)

    res = left if not right else right
    return [root] + res if res else []

def lowestCommonAncestor_2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or not p or not q: return root

    while root:
        if root.val < p.val and root.val < q.val: root = root.right
        elif root.val > p.val and root.val > q.val: root = root.left
        else: break

    return root

def lowestCommonAncestor_3(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or not p or not q: return None
    elif (p and p == root)or (q and q== root): return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right: return root
    elif left: return left
    elif right: return right
    else: return None

if __name__ == "__main__":
    print(maxAltitude([14,2,27,-5,28,13,39], 3))