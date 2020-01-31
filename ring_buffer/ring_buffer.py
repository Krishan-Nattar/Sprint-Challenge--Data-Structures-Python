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

        # Loop through each item in the DLL and append that value to list_buffer_contents
        current = self.storage.head # Start current off at the beginning of the list
        while current: # Check if node exists
            list_buffer_contents.append(current.value) # Append value to list
            current = current.next # Move to next node

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # Set max capacity
        self.storage = [None] * capacity # Instantiate with a list set to the length of max capacity
        self.current = None # This will track the current value via an [index] of self.storage

    def append(self, item):
        if self.current != None: # If self.current == None, then we haven't appended ANYTHING yet. So this checks if we already have at least one item appended
            if self.current + 1 == self.capacity: # Checks to see if self.current is at the end of the list. If it is, we switch it to the beginning.
                self.current = 0
            else:
                self.current += 1 # If self.current is NOT at the end of the list, we move the index up one spot.
        else:
            self.current = 0 # If we have not appended ANY item to storage, we instantiate self.current to the first index [0]
        
        self.storage[self.current] = item

    def get(self):
        return [x for x in self.storage if x] # Return a list of everything in self.storage, excluding 'None'
