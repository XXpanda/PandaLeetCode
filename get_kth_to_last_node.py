# coding=utf-8


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def kth_to_last(head, n):  # 直观的解法, 先遍历一遍链表, 计数, 然后算出倒数第k个结点
    if not head:
        return head
    head_len = 1
    temp = head
    while head.next:
        head_len += 1
        head = head.next
    k = head_len - n + 1
    i = 1
    while 1:
        if i == k:
            return temp.val
        temp = temp.next
        i += 1


def kth_to_last_improved(head, n):  #改善后的解法, 用两个指针同时跑  两个间距为n,当第一个跑到表尾,另一个即为所求结点
    if not head:
        return head
    head1 = head
    i = 1
    while head1.next and head.next:
        head = head.next
        if i >= n:
            head1 = head1.next
        i += 1
    return head1.val


if __name__ == '__main__':
    temp1 = ListNode(0)
    temp2 = ListNode(0)
    a1 = [6,8,8,10,15,16,19]
    a2 = [2,2,13,16]
    i = 0
    l1 = temp1
    while i < len(a1):
        temp1.next = ListNode(a1[i])
        temp1 = temp1.next
        i += 1
    j = 0
    l2 = temp2
    while j < len(a2):
        temp2.next = ListNode(a2[j])
        temp2 = temp2.next
        j += 1
    print kth_to_last_improved(l1, 7)



