class Node:
    """
    Class for each node in binary tree representation of snailfish number. Each node has reference to its parent
    """
    def __init__(self, value, parent):
        if type(value) == int:
            self.l = None
            self.r = None
            self.v = value
        else:
            self.l = Node(value[0], self)
            self.r = Node(value[1], self)
        self.parent = parent

class Tree:
    """
    Class for binary tree representation of snailfish number.
    """
    def __init__(self, snailfish_number):
        # Use None as parent for root
        self.root = Node(snailfish_number, None)

    def tolist(self, node):
        """
        Convert all nodes below this to list of lists
        """
        if hasattr(node, 'v'):
            return node.v
        else:
            this_data = []
            if node.l:
                this_data.append(self.tolist(node.l))
            if node.r != None:
                this_data.append(self.tolist(node.r))
            return this_data

    def inordertraversal(self, root):
        """
        Traverse the binary tree in order
        Args:
            root: The root
        Returns: List of nodes in order
        """
        res = []
        if root:
            res = self.inordertraversal(root.l)
            res.append(root)
            res = res + self.inordertraversal(root.r)
        return res

    def explodenode(self, node):
        """
        Explode a pair in a given node in the tree. Do an ordered traversal and figure out nodes to update based on
        value nodes before and after the explodingnode.

        Args:
            node: The node with the pair to explode
        """
        # TODO: This method is very hacky and not nice, needs update when time
        orderednodes = self.inordertraversal(self.root)

        lastvaluenode, leftnode, rightnode = None, None, None
        this = None
        lookforright = False
        for orderednode in orderednodes:
            previous = this
            this = orderednode

            if hasattr(this, 'v') and not this.parent == node:
                lastvaluenode = this
                if lookforright and lastvaluenode != leftnode:
                    rightnode = this
                    break

            if this == node:
                leftnode = lastvaluenode
                lookforright = True

        if leftnode != None:
            leftnode.v += node.l.v
        if rightnode != None:
            rightnode.v += node.r.v

        node.l = None
        node.r = None
        node.v = 0

    def splitnode(self, node):
        """
        Split number in a given node in the tree
        Args:
            node: The node to split
        """
        node.l = Node(int(node.v // 2), node)
        node.r = Node(int(-(-node.v // 2)), node)
        del node.v

    def get_explodingnode(self, node, depth):
        """
        Get node to explode
        Args:
            node: Node to search from
            depth: The depth of the current node

        Returns: A node to explode, if found. Else, return None
        """
        # TODO: This is also a bit hacky and could be made better
        if depth > 3 and not hasattr(node, 'v') and hasattr(node.l, 'v') and hasattr(node.r, 'v'):
            return node
        else:
            if node.l != None:
                retval = self.get_explodingnode(node.l, depth + 1)
                if retval != None:
                    return retval
            if node.r != None:
                retval = self.get_explodingnode(node.r, depth + 1)
                if retval != None:
                    return retval
        return None

    def get_splittingnode(self, node):
        """
        Get node to split
        Args:
            node: Node to search from

        Returns: A node to split, if found. Else, return None
        """
        # TODO: This is also a bit hacky and could be made better
        if hasattr(node, 'v') and node.v >= 10:
            return node
        else:
            if node.l != None:
                retval =  self.get_splittingnode(node.l)
                if retval != None:
                    return retval
            if node.r != None:
                retval = self.get_splittingnode(node.r)
                if retval != None:
                    return retval
        return None

    def calculate_magnitude(self, node):
        """
        Calculate magnitude for the tree, starting from the given node
        Args:
            node: The node to start from

        Returns: The magnitude of the tree
        """
        if hasattr(node, 'v'):
            return node.v
        magnitude = 0
        if node.l != None:
            magnitude += 3 * self.calculate_magnitude(node.l)
        if node.r != None:
            magnitude += 2 * self.calculate_magnitude(node.r)
        return magnitude

# Open and read file to a list of snailfish numbers
snailfish_numbers = []
input = open('18_input.txt', 'r')
for line in input:
    snailfish_numbers.append(eval(line.strip()))
input.close()

"""
Task 1
"""

# First get the first number
this_number = snailfish_numbers[0]
snailfish_tree = None

# For all these numbers
for i in range(1, len(snailfish_numbers)):

    # Get next number to add to this
    next_number = snailfish_numbers[i]

    # Add numbers together
    snailfish_sum = [this_number, next_number]

    # Convert to binary tree
    snailfish_tree = Tree(snailfish_sum)

    # Reduce it
    reduced = False
    while not reduced:

        # First check for exploding
        node_to_explode = snailfish_tree.get_explodingnode(snailfish_tree.root, 0)
        if node_to_explode != None:
            snailfish_tree.explodenode(node_to_explode)
            # If we found a node to explode, keep searching for nodes to explode
            continue

        # Then check for splitting
        node_to_split = snailfish_tree.get_splittingnode(snailfish_tree.root)
        if node_to_split != None:
            snailfish_tree.splitnode(node_to_split)
            # We split a node, so keep reducing
            continue

        # Did not find any reductions remaining, we have thus reduced the number
        reduced = True

    # Convert the reduced binary tree back to list of lists
    this_number = snailfish_tree.tolist(snailfish_tree.root)

print(f'Final snailfish number magnitude = {snailfish_tree.calculate_magnitude(snailfish_tree.root)}')

"""
Task 2
"""

largest_magnitude = 0
for i in range(0, len(snailfish_numbers)):
    for j in range(0, len(snailfish_numbers)):

        # Get two snailfish numbers
        x = snailfish_numbers[i]
        y = snailfish_numbers[j]

        if x == y:
            continue

        # Add numbers together both ways to produce sums to be reduced
        sum_xy = [x, y]
        sum_yx = [y, x]

        # Convert to trees
        tree_xy = Tree(sum_xy)
        tree_yx = Tree(sum_yx)

        # Reduce the trees
        reduced_xy = False
        while not reduced_xy:

            # First check for exploding
            node_to_explode = tree_xy.get_explodingnode(tree_xy.root, 0)
            if node_to_explode != None:
                tree_xy.explodenode(node_to_explode)
                # If we found a node to explode, keep searching for nodes to explode
                continue

            # Then check for splitting
            node_to_split = tree_xy.get_splittingnode(tree_xy.root)
            if node_to_split != None:
                tree_xy.splitnode(node_to_split)
                # We split a node, so keep reducing
                continue

            # Did not find any reductions remaining, we have thus reduced the number
            reduced_xy = True

        reduced_yx = False
        while not reduced_yx:

            # First check for exploding
            node_to_explode = tree_yx.get_explodingnode(tree_yx.root, 0)
            if node_to_explode != None:
                tree_yx.explodenode(node_to_explode)
                # If we found a node to explode, keep searching for nodes to explode
                continue

            # Then check for splitting
            node_to_split = tree_yx.get_splittingnode(tree_yx.root)
            if node_to_split != None:
                tree_yx.splitnode(node_to_split)
                # We split a node, so keep reducing
                continue

            # Did not find any reductions remaining, we have thus reduced the number
            reduced_yx = True

        # Calculate magnitudes and store if larger
        largest_magnitude = max(tree_xy.calculate_magnitude(tree_xy.root), tree_yx.calculate_magnitude(tree_yx.root),
                                largest_magnitude)

print(f'Largest possible magnitude for two snailfish numbers = {largest_magnitude}')
