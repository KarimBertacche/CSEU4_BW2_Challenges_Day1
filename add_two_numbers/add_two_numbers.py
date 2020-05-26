"""
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }


 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
"""

class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None

def addTwoNumbers(l1, l2):
    # initialize a nums str for list 1
    numsStr1 = ""
    # initialize a nums str for list 2
    numsStr2 = ""

    # while there is a value in list 1
    while l1:
        # assign at each iteration the first value and add the next before for both lists
        numsStr1 = str(l1.val) + numsStr1
        numsStr2 = str(l2.val) + numsStr2
        # go the next num in the list for the next iteration for both lists
        l1 = l1.next
        l2 = l2.next

    # sum up both list nums reversed after turning them back into integers
    numsTot = str(int(numsStr1) + int(numsStr2))

    # grab the last number in the total of the two lists
    numsTot = numsTot[::-1]

    # create a new list node with the first entry within the head of the total 
    newList = ListNode(int(numsTot[0]))
    # assign the list head to a variable
    listHead = newList

    # for each entry excluding the head
    for num in numsTot[1:]:
        # create a new node by reversing the connection to the next to itself
        newList.next = ListNode(num)
        # and assign the next value to the list for the next iteration
        newList = newList.next

    # return the reverse list node
    return listHead

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

while result: 
    print(result.val)
    result = result.next