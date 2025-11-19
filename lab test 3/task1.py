# -------------------------
# Binary Search Tree in Python
# -------------------------

# Node structure
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# BST class
class BST:
    def __init__(self):
        self.root = None

    # Insert operation
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    # Inorder Traversal (Left, Root, Right)
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)

    # Search operation
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)


# -------------------------
# Demonstration
# -------------------------

# Create BST object
bst = BST()

# Insert sample values
values = [40, 20, 60, 10, 30, 50, 70]
print("Inserting values:", values)
for v in values:
    bst.insert(v)

# Inorder Traversal
print("Inorder Traversal:", bst.inorder())

# Search for elements
print("Search 30:", bst.search(30))   # Should return True
print("Search 90:", bst.search(90))   # Should return False
