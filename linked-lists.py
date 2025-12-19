class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def reorderList(head: ListNode) -> None:
    length = 0
    slow_pointer = head
    fast_pointer = head
    while fast_pointer is not None:
        length += 1
        if length % 2 == 0:
            slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
    rev_head = slow_pointer
    new_node = ListNode(val = rev_head.val, next = None)
    node = rev_head
    while node.next is not None:
        prev = new_node
        node = node.next
        new_node = ListNode(val = node.val, next = prev)
    rev_head = new_node
    finger1 = head
    finger2 = rev_head
    prev = None
    for i in range(length):
        if i % 2 == 0:
            if prev is not None:
                prev.next = finger1
                prev = finger1
                finger1 = finger1.next
            else:
                prev = finger1
                first = finger1
                finger1 = finger1.next
        else:
            prev.next = finger2
            prev = finger2
            finger2 = finger2.next
    prev.next = None
    return None

def copyRandomList(head: 'Node') -> 'Node':
    node = head
    built = {}
    while node is not None:
        built[node] = None
        node = node.next
    return deep_copy(head, built)

def deep_copy(node, built):
    if node is None:
        return None
    node_copy = Node(node.val)
    built[node] = node_copy
    if node.next is not None:
        if built[node.next] is None:
            node_copy.next = deep_copy(node.next, built)
        else:
            node_copy.next = built[node.next]
    if node.random is not None:
        if built[node.random] is None:
            node_copy.random = deep_copy(node.random, built)
        else:
            node_copy.random = built[node.random]
    return node_copy

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    #reverse lists
    rev1 = reverseList(l1)
    rev2 = reverseList(l2)
    remainder = 0
    prev = None
    #start with smallest digit and build up new list
    while rev1 is not None or rev2 is not None or remainder != 0:
        if rev1 is not None:
            val1 = rev1.val
        else:
            val1 = 0
        if rev2 is not None:
            val2 = rev2.val
        else:
            val2 = 0
        num = val1 + val2 + remainder
        remainder = num // 10
        new_node = ListNode(val = (num % 10), next = None)
        if prev is None:
            first = new_node
            prev = new_node
        else:
            prev.next = new_node
            prev = new_node
        if rev1 is not None:
            rev1 = rev1.next
        if rev2 is not None:
            rev2 = rev2.next
    return reverseList(first)


def reverseList(head: ListNode) -> ListNode:
    if head is None:
        return None
    else:
        new_node = ListNode(val = head.val, next = None)
        node = head
        while node.next is not None:
            prev = new_node
            node = node.next
            new_node = ListNode(val = node.val, next = prev)
        return new_node

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    node = head
    actual_prev = None
    prev = None
    while node is not None:
        if no_more_reversing(node, k):
            if prev is not None:
                prev.next = node
            break
        prev = node
        node, first = reverseSubList(node, k)
        if actual_prev is not None:
            actual_prev.next = first
        else:
            head = first
        actual_prev = prev
    return head


def reverseSubList(node: ListNode, stop: int) -> ListNode:
    if node is None:
        return None
    else:
        count = 1
        prev = None
        while node is not None and count <= stop:
            count += 1
            next = node.next
            node.next = prev
            prev = node
            node = next
        return node, prev

def no_more_reversing(node: ListNode, stop: int) -> bool:
    if node is None:
        return True
    count = 1
    while count <= stop:
        if node is None:
            return True
        else:
            count += 1
            node = node.next
    return False

f = ListNode(6)
e = ListNode(5, f)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)


print(reverseKGroup(a, 3))

