

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addNode(self, node):
        print('addnode')
        self.next = node

    def printList(self):
        print('printList')
        while (self.next != None):
            print(self.val)
            self = self.next
        if (self.next == None):
            print(self.val)

def addTwoNumbers(l1, l2 ,carryIn = 0):
    val = l1.val + l2.val + carryIn
    carryIn = val // 10
    ret = ListNode(val % 10 ) 
    
    if (l1.next != None or l2.next != None or carryIn != 0):
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        ret.next = addTwoNumbers(l1.next,l2.next,carryIn)
    return ret



l1 = ListNode(15)
newNode = ListNode(20)
l1.addNode(newNode)

l2 = ListNode(15)
newNode = ListNode(20)
l2.addNode(newNode)

res = addTwoNumbers(l1, l2)
res.printList()