from __future__ import annotations
from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class LinkedStack(Generic[T]):
    """LIFO Stack implementation using a singly linked list for storage."""
    #--------------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element: T, next: Optional['LinkedStack._Node']):      # initialize node's fields
            self._element: T = element             # reference to user's element
            self._next: Optional['LinkedStack._Node'] = next                   # reference to next node

    #----------------------------stack methods-----------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head: Optional[LinkedStack._Node] = None                       # reference to the head node
        self._size: int = 0                          # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __iter__(self) -> Iterator[T]:
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next

    def __repr__(self) -> str:
        return f"LinkedStack([{', '.join(repr(x) for x in self)}])"

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e: T):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self) -> T:
        """Return (but do no remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._head._element              # top of stack is at head of list

    def pop(self) -> T:
        """Remove and return the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        assert self._head is not None
        answer = self._head._element
        self._head = self._head._next           # bypass the former top node
        self._size -= 1
        return answer


class LinkedQueue(Generic[T]):
    """FIFO Queue implementation using a singly linked list for storage."""
    #--------------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element: T, next: Optional['LinkedQueue._Node']):      # initialize node's fields
            self._element: T = element             # reference to user's element
            self._next: Optional['LinkedQueue._Node'] = next                   # reference to next node

    #----------------------------queue methods-----------------------------
    def __init__(self):
        """Create an empty queue."""
        self._head: Optional[LinkedQueue._Node] = None                       # reference to the head node
        self._tail: Optional[LinkedQueue._Node] = None                       # reference to the tail node
        self._size: int = 0                          # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __iter__(self) -> Iterator[T]:
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next

    def __repr__(self) -> str:
        return f"LinkedQueue([{', '.join(repr(x) for x in self)}])"

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def enqueue(self, e: T):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            self._head = newest                 # special case: previously empty
        else:
            assert self._tail is not None
            self._tail._next = newest           # update reference to tail node
        self._tail = newest
        self._size += 1

    def first(self) -> T:
        """Return (but do no remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('queue is empty.')
        assert self._head is not None
        return self._head._element              # front aligned with head of list

    def dequeue(self) -> T:
        """Remove and return the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('queue is empty.')
        assert self._head is not None
        answer = self._head._element
        self._head = self._head._next           # bypass the former front node
        self._size -= 1
        if self.is_empty():                     # special case as queue is empty
            self._tail = None                   # removed head had been tail
        return answer


class CircularQueue(Generic[T]):
    """Queue implementation using a circularly linked list for storage."""
    #--------------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element: T, next: Optional['CircularQueue._Node']):      # initialize node's fields
            self._element: T = element             # reference to user's element
            self._next: Optional['CircularQueue._Node'] = next                   # reference to next node

    #----------------------------queue methods-----------------------------
    def __init__(self):
        """Create an empty queue."""
        self._tail: Optional[CircularQueue._Node] = None                       # reference to the tail node
        self._size: int = 0                          # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __iter__(self) -> Iterator[T]:
        if self.is_empty():
            return
        assert self._tail is not None
        cur = self._tail._next  # head
        for _ in range(self._size):
            assert cur is not None
            yield cur._element
            cur = cur._next

    def __repr__(self) -> str:
        return f"CircularQueue([{', '.join(repr(x) for x in self)}])"

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self) -> T:
        """Return (but do no remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('queue is empty.')
        head = self._tail._next
        assert head is not None
        return head._element              # front aligned with head of list

    def enqueue(self, e: T):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            newest._next = newest               # initialize circularly
        else:
            newest._next = self._tail._next     # new node points to head
            self._tail._next = newest           # old tails points to new node
        self._size += 1
        self._tail = newest                     # new node becomes the tail

    def dequeue(self) -> T:
        """Remove and return the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('queue is empty.')
        assert self._tail is not None
        oldhead = self._tail._next
        assert oldhead is not None
        if self._size == 1:                     # removing only element
            self._tail = None                   # queue becomes empty
        else:
            self._tail._next = oldhead._next    # bypass the old head
        self._size -= 1
        return oldhead._element

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next       # old head becomes new tail


# ========================== MAIN DE PRUEBAS ==========================

def _test_linked_stack():
    print("\n== LinkedStack ==")
    s = LinkedStack[int]()
    print("is_empty:", s.is_empty())
    for x in (1, 2, 3):
        s.push(x)
        print("push", x, "->", s)
    print("len:", len(s), "top:", s.top())
    while s:
        print("pop ->", s.pop(), "; now:", s)
    try:
        s.pop()
    except Empty as e:
        print("Empty OK:", e)

def _test_linked_queue():
    print("\n== LinkedQueue ==")
    q = LinkedQueue[str]()
    print("is_empty:", q.is_empty())
    for w in ("a", "b", "c"):
        q.enqueue(w)
        print("enqueue", w, "->", q)
    print("len:", len(q), "first:", q.first())
    while q:
        print("dequeue ->", q.dequeue(), "; now:", q)
    try:
        q.first()
    except Empty as e:
        print("Empty OK:", e)

def _test_circular_queue():
    print("\n== CircularQueue ==")
    cq = CircularQueue[int]()
    for x in (10, 20, 30):
        cq.enqueue(x)
        print("enqueue", x, "->", cq)
    print("first:", cq.first())
    cq.rotate()
    print("rotate ->", cq, "first:", cq.first())
    print("dequeue:", cq.dequeue(), "->", cq)
    cq.rotate()
    print("rotate ->", cq)
    while cq:
        print("dequeue ->", cq.dequeue(), "; now:", cq)
    try:
        cq.dequeue()
    except Empty as e:
        print("Empty OK:", e)

if __name__ == "__main__":
    _test_linked_stack()
    _test_linked_queue()
    _test_circular_queue()
