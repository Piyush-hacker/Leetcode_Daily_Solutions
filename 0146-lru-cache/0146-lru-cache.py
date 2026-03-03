class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}  # key -> Node

        # Dummy head/tail to avoid edge-case checks
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove node from the linked list."""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add_to_front(self, node: Node) -> None:
        """Add node right after head (mark as most recently used)."""
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        node = self.mp[key]
        # Move to front (most recently used)
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            # Move to front
            self._remove(node)
            self._add_to_front(node)
            return

        # Insert new
        node = Node(key, value)
        self.mp[key] = node
        self._add_to_front(node)

        # Evict if over capacity
        if len(self.mp) > self.cap:
            lru = self.tail.prev  # least recently used
            self._remove(lru)
            del self.mp[lru.key]