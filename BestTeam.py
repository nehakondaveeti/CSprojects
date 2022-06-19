#  File: BestTeam.py

#  Description: Determine which subteam is best (highest average score).

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:

from typing import Optional

class Node(object):
    """ An employee/node in the business hierarchy. """
    def __init__(
        self,
        val: int,
        left = None,
        right = None
    ) -> None:
        self.val = val
        self.lChild = left
        self.rChild = right

    def __str__(self) -> str:
        return f'({self.val})'

def parse_node_from_string(data: str) -> Optional[Node]:
    """ Parses node from string: (name:data).=> Node object."""

    if data == 'None':
        return None
    # Remove parantheses surrounding and split.
    cleaned = data.replace('(', '').replace(')', '')
    return Node(int(cleaned))

def deserialize(data: str) -> Optional[Node]:
    """ Deserializes the level order string into a tree, returns root node. """
    if len(data) == 0:
        return None
    
    level_order = data.split(', ')
    n = len(level_order)
    
    mapping = {i: parse_node_from_string(level_order[i]) for i in range(n) }
    # slow pointer for parent, fast pointer for child.
    slow = 0
    fast = 1
    
    # denotes where to place child (left or right).
    filled = 0
    
    # assign all children to a parent, stop when none left.
    while fast < len(level_order):
        if filled == 2:
            filled = 0
            slow += 1
        cur = mapping[slow]
        
        if cur is None:
            slow += 1
            continue

        if filled == 0:
            cur.lChild = mapping[fast]
        elif filled == 1:
            cur.rChild = mapping[fast]
        
        filled += 1
        fast += 1

    return mapping[0]


########################################## MODIFY CODE ABOVE AT YOUR OWN RISK ##########################################

def best_team(manager: Node) -> float:
    """ Determine which subteam is best (highest average score).

    Args:
        manager (Node): Root node of the business hierarchy.

    Returns:
        float: The average score of the best subteam.

    """
    #return the max average between the three nodes manag, manager.left, manager.right
    this_result = find_average(manager)
    return float(this_result[2])

    pass

def find_average(node):
    # returns list with[sum at node, count at node, maximum average at node]
    # for each child it calls find average
    # when those calls all finish the root node has the sum of all, the count of nodes, and the max avg found
    if node.lChild == None and node.rChild == None:
        return [node.val,1, node.val]
    
    #otherwise it has children
    left_result = [0,0,0]
    right_result = [0,0,0]
    if node.lChild != None:
        left_result = find_average(node.lChild)
    if node.rChild != None:
        right_result = find_average(node.rChild)
        
    this_result = [0,0,0]
    this_result[0] = left_result[0] + right_result[0] + node.val # sum at this node
    this_result[1] = left_result[1] + right_result[1] + 1        #coutnt at this node
    this_result[2] = max(left_result[2],right_result[2], this_result[0]/this_result[1])

    return this_result
    


if __name__ == '__main__':
    serialized = input().strip()
    root = deserialize(serialized)
    
    # round to hundredth decimal place.
    result = best_team(root)
    print(round(result, 2))

