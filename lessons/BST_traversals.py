"""MY OWN IMPLEMENTATION OF PRE-IN-POST-ORDER TRAVERSALS (recur + iter).

                F
            B       G
        A     D        I
            C   E    H

pre-order:      F, B, A, D, C, E, G, I, H
in-order:       A, B, C, D, E, F, G, H, I
post-order:     A, C, E, D, B, H, I, G, F
"""

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ################ RECURSIVE #################
# ################ PREORDER #################

def recursive_preorder(root):
    """PREORDER RECURSIVE."""
    if not root:
        return None

    def helper(node):
        if node is None:
            return
        nonlocal traversal
        traversal.append(node.val)
        helper(node.left)
        helper(node.right)

    traversal = []
    helper(root)
    return traversal


def preorder(root):
    """PREORDER RECURSIVE."""
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


# ################ RECURSIVE #################
# ################ POSTORDER #################


def recursive_postorder(root):
    """POSTORDER RECURSIVE."""
    if not root:
        return None

    def helper(node):
        if node is None:
            return
        nonlocal traversal
        helper(node.left)
        helper(node.right)
        traversal.append(node.val)

    traversal = []
    helper(root)
    return traversal


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []


# ################ RECURSIVE #################
# ################ INORDER #################


def recursive_inorder(root):
    """INORDER RECURSIVE."""
    if not root:
        return None

    def helper(node):
        if node is None:
            return
        nonlocal traversal
        helper(node.left)           # <--
        traversal.append(node.val)  # #  |--- reverse to have decreasing order
        helper(node.right)          # <--

    traversal = []
    helper(root)
    return traversal


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


# ################ ITERATIVE #################
# ################ PREORDER #################


def iterative_preorder(root):
    """INORDER ITERATIVE. requires 1 stack + 1 queue."""
    if not root:
        return []
    stack = [root]
    traversal = deque()
    while stack:
        node = stack.pop()
        traversal.appendleft(node.val)  # !!
        if node.right:                # pust Right child first to make sure
            stack.append(node.right)  # that left subtree is processed 1st
        if node.left:
            stack.append(node.left)

    return traversal  # pop for normal order // popleft for reversed order


# ################ ITERATIVE #################
# ################ POSTORDER #################


def iterative_postorder(root):
    """POSTORDER ITERATIVE. requires 1 stack + 1 queue."""
    if not root:
        return []
    stack = [root]
    traversal = deque()  # could use 2nd stack instead of queue: traversal = []
    while stack:
        node = stack.pop()
        traversal.append(node.val)  # !!!!
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return traversal  # pop for normal order // popleft for reversed order


def iterative_postorder2(root):
    """POSTORDER ITERATIVE. using 1 stack only.
    https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
    """
    if not root:
        return []
    stack = []
    node = root
    # traversal = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left = depths.get(node.left, 0)     # REMEMBER 2nd arg = value to be returned
                right = depths.get(node.right, 0)   # if key not found (instead returning None)
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True


def iterative_postorder2(root):
    """POSTORDER ITERATIVE. Alternative.
    https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
    """
    if not root:
        return []
    stack = []
    node = root
    traversal = []
    while stack or node:  # ORIGINALLY WHILE TRUE WITH A BREAK IF STACK EMPTY

        while node:  # Push node's right child and then node to stack
            if node.right:
                stack.append(node.right)
            stack.append(node)
            node = node.left  # Push node's right child and then node to stack

        node = stack.pop()  # Pop an item from stack and set it as node
        if node.right and node.right == stack[-1]:  # ensure right child is processed 1st
            node = stack.pop()  # Remove right child from stack
            stack.append(node)  # Push node back to stack
            node = node.right  # change node so right child is processed next
        else:
            traversal.append(node.val)
            node = None

    return traversal


# ################ ITERATIVE #################
# ################ INORDER #################


def iterative_inorder(root):
    """INORDER ITERATIVE. USING STACK"""
    stack = []
    traversal = []
    node = root
    while node is not None or stack != []:  # [ALT] while node or stack:
        while node is not None:             # [ALT] while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        traversal.append(node)
        node = node.right

    return traversal


def iterative_inorder_bis(root):
    """INORDER ITERATIVE. USING DEQUE"""
    stack = []
    traversal = deque()
    node = root
    while node is not None or stack != []:  # [ALT] while node or stack:
        # travel to each node's left child until leaf
        while node is not None:             # [ALT] while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        traversal.appendleft(node)
        node = node.right

    return reversed(traversal)


def iterative_inorder2(root):
    """INORDER ITERATIVE. ONE LOOP ONLY (SEEMS BIT SLOWER)"""
    stack = []
    traversal = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            tmp_node = stack.pop()
            traversal.append(tmp_node)
            node = tmp_node.right

    return traversal


def inorderTraversal_iter2bis(root):
    """USING SINGLE LOOP WiTH DEQUE"""
    stack = []
    traversal = deque()
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            tmp_node = stack.pop()
            traversal.appendleft(tmp_node.val)
            node = tmp_node.right

    return reversed(traversal)


# ################ ITERATIVE #################
# ################ LEVEL TRAVERSAL  #################

def iterative_lvl_traversal(root):
    """INORDER ITERATIVE. using stack."""
    stack = [root]
    traversal = []
    for node in stack:
        if node:
            traversal.append(node.val)
            stack += node.left, node.right
    return(traversal)


def iterative_lvl_traversal(root):
    """INORDER ITERATIVE. using queue"""
        queue = deque()
        queue.append(root)
        traversal = []
        while queue:
            node = queue.popleft()
            if node:
                traversal.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return(traversal)



a = deque()
a += 1, 2, 3
a

# ################ MORRIS TRAVERSAL #################
# ################ PREORDER #################

# https://www.geeksforgeeks.org/morris-traversal-for-preorder/

# ################ MORRIS TRAVERSAL #################
# ################ IN ORDER #################

# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
