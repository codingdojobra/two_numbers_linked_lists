# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
    def __eq__(self, other):
        if other != None:
            return self.val == other.val and self.next == other.next
        
    def __add__(self, other):
        return self.val + other.val
        
def add_nodes(a: ListNode, b: ListNode):
    new = ListNode(a + b)
    print(new.val)
    

# (2 -> 4 -> 3) + (5 -> 6 -> 4)
# 7 -> 0 -> 8

numeroa = ListNode(3)
numerob = ListNode(4, numeroa)
numeroc = ListNode(2, numerob)

numerod = ListNode(4)
numeroe = ListNode(6, numerod)
numerof = ListNode(5, numeroe)


add_nodes(numeroc, numerof)

# assert numero7 == numero7b

# 7 -> 0 -> 8 -> None


#     def __eq__(self, other):
#     return self.a == other.a and self.b == other.b and self.c == other.c


'''
class No:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_node(no_atual, value):   
    while no_atual.next != None:        
        if no_atual.val == value:
            no_anterior.next = no_atual.next
            # delete(no_atual)
            return None
       
        # print(no_atual.val)
        no_anterior = no_atual
        no_atual = no_atual.next


node1 = No(5)
head = node1
node2 = No(8)
node1.next = node2
node3 = No(9)
node2.next = node3

print(head.val)
print(node1.next.val)
delete_node(head, 8)
print(node1.next.val)
print(head.val)

#The given node will not be the tail and it will always be a valid node of the linked list.

# proximo = head.next
# print(proximo)
# print(node2)
'''
