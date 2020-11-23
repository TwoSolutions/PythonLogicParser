class Node:
    def __init__(self, node, left=None, right=None):
        self.left = left
        self.right = right
        self.node = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right
