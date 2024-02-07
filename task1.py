class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def middle_get(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_sort_list(head):
    if not head or not head.next:
        return head

    middle = middle_get(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_list(head)
    right = merge_sort_list(next_to_middle)

    return merge_two_lists(left, right)


def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    tail.next = l1 or l2

    return dummy.next


def print_list(name, head):
    print(f"{name}:")

    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

    print()


if __name__ == "__main__":
    l1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(2)

    l1.next = node2
    node2.next = node3

    print_list("l1", l1)

    l1_reversed = reverse_list(l1)
    print_list("l1_reversed", l1_reversed)

    l1_sorted = merge_sort_list(l1_reversed)
    print_list("l1_sorted", l1_sorted)

    l2 = ListNode(4)
    node5 = ListNode(2)
    node6 = ListNode(5)

    l2.next = node5
    node5.next = node6

    print_list("l2", l2)

    l2_sorted = merge_sort_list(l2)
    print_list("l2_sorted", l2_sorted)

    l3_merged = merge_two_lists(l1_sorted, l2_sorted)
    print_list("l3_merged", l3_merged)
