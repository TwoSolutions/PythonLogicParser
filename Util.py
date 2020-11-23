# Print nodes at a given level
def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.node, end=" ")
    elif level > 1:
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)


""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


# Iterative method to do level order traversal
# line by line
def print_level_order(root):
    # Base case
    if root is None:
        return
    # Create an empty queue for level order traversal
    q = [root]

    # Enqueue root and initialize height

    while q:

        # nodeCount (queue size) indicates number
        # of nodes at current lelvel.
        count = len(q)

        # Dequeue all nodes of current level and
        # Enqueue all nodes of next level
        while count > 0:
            temp = q.pop(0)
            print(temp.node, end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

            count -= 1
        print(' ')
