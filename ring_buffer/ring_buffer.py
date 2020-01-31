from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # If there is nothing in the DLL yet, add the first item and instantiate current to head.
        if self.current == None:
            self.storage.add_to_tail(item) # This could also be add_to_head(item), but for consistency with the whole project I left it as add_to_tail
            self.current = self.storage.head
            return
        
        # If we have reached the maximum items in our DLL:
        if len(self.storage) >= self.capacity:
            # If current is NOT the tail, we change the current to the next node and also update it's value
            if self.current != self.storage.tail:
                self.current.next.value = item
                self.current = self.current.next
            
            # If current IS the tail, we change it to head and update the value
            else:
                self.current = self.storage.head
                self.current.value = item
        # If we have not reached the limit in our DLL, we simply add the new node to the tail and set current to the newly updated node (the tail).
        else:
            self.storage.add_to_tail(item)
            self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        # if self.storage.head:
        current = self.storage.head
        while current:
            if current.value:
                list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
