class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
            
    def append(self, data):
        new_node = self.Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_head_node = self.Node(data)
        new_head_node.next = self.head
        self.head = new_head_node
        if self.tail is None:
            self.tail = new_head_node

    def insert(self, insert_index, data):
        insert_item = self.Node(data)
        current = self.head
        if self.tail is None:
            self.tail = insert_item
        
        if insert_index == 0:
            insert_item.next = self.head
            self.head = insert_item
            return

        if insert_index < 0:
            insert_index = insert_index + len(self) + 1
            if insert_index < 0:
                print("Index Out Of Bounds!")
                return
        
        iter_index = 0
        while (current is not None) and (iter_index < insert_index):
            if iter_index == insert_index-1:
                insert_item.next = current.next
                current.next = insert_item
                if insert_item.next is None:
                    self.tail = insert_item
                return
            iter_index += 1
            current = current.next
        print("Index Out Of Bounds!")

    def delete(self, del_index):
        current = self.head

        if del_index == 0:
            self.head = current.next if current is not None else None
            if self.head is None:
                self.tail = None
            return

        elif del_index < 0:
            del_index = del_index + len(self)
            if del_index < 0:
                print("Index Out Of Bounds!")
                return

        iter_index = 0
        while (current is not None) and (iter_index < del_index):
            if iter_index == del_index-1:
                if current.next is None:
                    print("Index Out OF Bounds!")
                    return
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                if self.head is None:
                    self.tail = None
                return
            iter_index += 1
            current = current.next

        print("Index Out Of Bounds!")

    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False

    def __str__(self):
        current = self.head
        str_list = []
        while current is not None:
            str_list.append(f"|{current.data}|")
            current = current.next
        str_list.append("|None|")
        return "->".join(str_list)

    def __len__(self):
        lenu = 0
        current = self.head
        while current is not None:
            lenu += 1
            current = current.next
        return lenu


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
print(ll)
ll.insert(0,'o')
print(ll)
ll.insert(2,7)
print(ll)
ll.insert(5,'o')
print(ll)
ll.insert(-1,9)
print(ll)
print()
ll.delete(3)
print(ll)
ll.delete(0)
print(ll)
ll.delete(4)
print(ll)
ll.delete(-1)
print(ll)
print()
ll.delete(5)
print(ll)
ll.delete(0)
ll.delete(0)
ll.delete(0)
print(ll)
ll.delete(0)
print(ll)
ll.delete(-1)
ll.delete(2)
print(ll)