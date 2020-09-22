class MyLinkedList(object):
    class Node(object):
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
    def print_linked_list(self):
        print("----")
        temp = self.head
        if self.head is not None:
            while temp is not None:
                print(temp.val)
                temp = temp.next
        print("----")
    
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        temp = self.head
        node = None
        count = 0
        while temp is not None and count < index:
            count += 1
            # if count == index:
            #     node = temp
            #     break
            temp = temp.next
        if temp is None:
            ret_val = -1
            
        else:
            ret_val = temp.val
        print(ret_val)
        return ret_val
            
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = self.Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        # self.print_linked_list()
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = self.Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                # print(temp.val)
                temp = temp.next
            temp.next = new_node 
        # self.print_linked_list()
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        temp = self.head
        prev = None
        counter = 0
        new_node = self.Node(val)
        if self.head is None:
            self.head = new_node
            return
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        while temp is not None and counter < index:
            counter += 1
            prev = temp
            temp = temp.next
            # print(prev.val, temp.val)
        if temp is not None:
            new_node.next = temp
            prev.next = new_node
            return
        if temp is None:
            prev.next = new_node
            return
        # self.print_linked_list()
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        counter = 0
        temp = self.head
        prev = None
        while temp is not None and counter <index:
            counter += 1
            prev = temp
            temp = temp.next
        if temp is not None:
            prev.next = temp.next
            del temp # clear out the memory
        # self.print_linked_list()
    
    def delete_from_end(self, n):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head
        for i in range(n):
            fast = fast.next
        
        if fast is None:
            self.head = self.head.next
            # self.print_linked_list()
            return 
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        # self.print_linked_list()
    
    def reversed_linked_list(self):
        temp = self.head
        prev = None
        if self.head is None or self.head.next is None:
            return self.head
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.print_linked_list()
        self.head = prev
    
    def delete_element_from_list(self, value):
        if self.head is None:
            return None
        prev = None
        current = self.head
        while current is not None and current.val == value:
            current = current.next
            self.head = current

        while current is not None:
            if current.val == value:
                if prev is not None:
                    prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
    
    def odd_event_linked_list(self):
        if self.head is None or self.head.next is None or self.head.next.next is None:
            return self.head
        length = 0
        tail = self.head
        while tail.next is not None:
            length += 1
            tail = tail.next
        no_of_steps = int(length) / 2 + 1 if length % 2 ==0 else int(length / 2)
        current = self.head
        while no_of_steps:
            no_of_steps -= 1
            tail.next =  current.next 
            current.next = current.next.next
            current = current.next
            tail.next.next = None
            tail = tail.next
    
    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return True
        stack = []
        temp = self.head
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        print(stack)
        temp = self.head
        while temp is not None and len(stack) != 0:
            if temp.val != stack.pop():
                return False
            temp = temp.next
        return True
    
    def roate_by_place(self, place):
        """
            1 2 3 4 5       
        """
        if self.head is None or place == 0:
            return self.head
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = self.head
        # now the list is a circular list
        current = self.head
        for i in range(place - 1):
            current = current.next
        self.head = current.next
        current.next = None
    
    def reverse_linked_list_recursive(self, head):
        "Returns the head of the reversed linked list"
        if head is None or head.next is None:
            return head
        
        p = self.reverse_linked_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return p
        

    def remove_duplicates(self):
        """
            Put the visites nodes in a list.
            If node has been visited then skip that row 
        """
        if self.head is None:
            return self.head
        visited_nodes = []
        prev = None
        current = self.head
        while current is not None:
            if current.val in visited_nodes:
                if prev is not None:
                    prev.next = current.next
            else:
                visited_nodes.append(current.val)
            prev = current
            current = current.next
    



            
    

# Your MyLinkedList object will be instantiated and called as such:
# 
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtTail(3)
obj.addAtTail(4)
obj.addAtTail(5)
# obj.addAtHead(0)
# obj.addAtTail(1)
# obj.addAtTail(2)
# obj.roate_by_place(1)
# obj.remove_duplicates()
obj.print_linked_list()
reversed_head = obj.reverse_linked_list_recursive(obj.head)
while reversed_head is not None:
    print(reversed_head.val)
    reversed_head = reversed_head.next
print("Done")
