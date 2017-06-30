"""Assignment 1 - Node and Grid

This module contains the Node and Grid classes.

Your only task here is to implement the methods
where indicated, according to their docstring.
Also complete the missing doctests.
"""

import functools
import sys
from container import PriorityQueue


@functools.total_ordering
class Node:
    """
    Represents a node in the grid. A node can be navigable 
    (that is located in water)
    or it may belong to an obstacle (island).

    === Attributes: ===
    @type navigable: bool
       navigable is true if and only if this node represents a 
       grid element located in the sea
       else navigable is false
    @type grid_x: int
       represents the x-coordinate (counted horizontally, left to right) 
       of the node
    @type grid_y: int
       represents the y-coordinate (counted vertically, top to bottom) 
       of the node
    @type parent: Node
       represents the parent node of the current node in a path
       for example, consider the grid below:
        012345
       0..+T..
       1.++.++
       2..B..+
       the navigable nodes are indicated by dots (.)
       the obstacles (islands) are indicated by pluses (+)
       the boat (indicated by B) is in the node with 
       x-coordinate 2 and y-coordinate 2
       the treasure (indicated by T) is in the node with 
       x-coordinate 3 and y-coordinate 0
       the path from the boat to the treasure if composed of the sequence 
       of nodes with coordinates:
       (2, 2), (3,1), (3, 0)
       the parent of (3, 0) is (3, 1)
       the parent of (3, 1) is (2, 2)
       the parent of (2, 2) is of course None
    @type in_path: bool
       True if and only if the node belongs to the path plotted by A-star 
       path search
       in the example above, in_path is True for nodes with coordinates 
       (2, 2), (3,1), (3, 0)
       and False for all other nodes
    @type gcost: float
       gcost of the node, as described in the handout
       initially, we set it to the largest possible float
    @type hcost: float
       hcost of the node, as described in the handout
       initially, we set it to the largest possible float
    """
    def __init__(self, navigable, grid_x, grid_y):
        """
        Initialize a new node

        @type self: Node
        @type navigable: bool
        @type grid_x: int
        @type grid_y: int
        @rtype: None

        Preconditions: grid_x, grid_y are non-negative

        >>> n = Node(True, 2, 3)
        >>> n.grid_x
        2
        >>> n.grid_y
        3
        >>> n.navigable
        True
        """
        self.navigable = navigable
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.in_path = False
        self.parent = None
        self.gcost = sys.float_info.max
        self.hcost = sys.float_info.max

    def set_gcost(self, gcost):
        """
        Set gcost to a given value

        @type gcost: float
        @rtype: None

        Precondition: gcost is non-negative

        >>> n = Node(True, 1, 2)
        >>> n.set_gcost(12.0)
        >>> n.gcost
        12.0
        """
        self.gcost = gcost

    def set_hcost(self, hcost):
        """
        Set hcost to a given value

        @type hcost: float
        @rtype: None

        Precondition: gcost is non-negative

        >>> n = Node(True, 1, 2)
        >>> n.set_hcost(12.0)
        >>> n.hcost
        12.0
        """
        self.hcost = hcost

    def fcost(self):
        """
        Compute the fcost of this node according to the handout

        @type self: Node
        @rtype: float
        """
        return self.gcost + self.hcost

    def set_parent(self, parent):
        """
        Set the parent to self
        @type self: Node
        @type parent: Node
        @rtype: None
        """
        self.parent = parent

    def distance(self, other):
        """
        Compute the distance from self to other
        @self: Node
        @other: Node
        @rtype: int
        """
        dstx = abs(self.grid_x - other.grid_x)
        dsty = abs(self.grid_y - other.grid_y)
        if dstx > dsty:
            return 14 * dsty + 10 * (dstx - dsty)
        return 14 * dstx + 10 * (dsty - dstx)

    def __eq__(self, other):
        """
        Return True if self equals other, and false otherwise.

        @type self: Node
        @type other: Node
        @rtype: bool
        """
        # TODO
        pass

    def __lt__(self, other):
        """
        Return True if self less than other, and false otherwise.

        @type self: Node
        @type other: Node
        @rtype: bool
        """
        # TODO
        pass

    def __str__(self):
        """
        Return a string representation.

        @type self: Node
        @rtype: str
        """
        # TODO
        pass


class Grid:
    """
    Represents the world where the action of the game takes place.
    You may define helper methods as you see fit.

    === Attributes: ===
    @type width: int
       represents the width of the game map in characters
       the x-coordinate runs along width
       the leftmost node has x-coordinate zero
    @type height: int
       represents the height of the game map in lines
       the y-coordinate runs along height; the topmost
       line contains nodes with y-coordinate 0
    @type map: List[List[Node]]
       map[x][y] is a Node with x-coordinate equal to x
       running from 0 to width-1
       and y-coordinate running from 0 to height-1
    @type treasure: Node
       a navigable node in the map, the location of the treasure
    @type boat: Node
       a navigable node in the map, the current location of the boat

    === Representation invariants ===
    - width and height are positive integers
    - map has dimensions width, height
    """

    def __init__(self, file_path, text_grid=None):
        """
        If text_grid is None, initialize a new Grid assuming file_path
        contains pathname to a text file with the following format:
        ..+..++
        ++.B..+
        .....++
        ++.....
        .T....+
        where a dot indicates a navigable Node, a plus indicates a
        non-navigable Node, B indicates the boat, and T the treasure.
        The width of this grid is 7 and height is 5.
        If text_grid is not None, it should be a list of strings
        representing a Grid. One string element of the list represents
        one row of the Grid. For example the grid above, should be
        stored in text_grid as follows:
        ["..+..++", "++.B..+", ".....++", "++.....", ".T....+"]

        @type file_path: str
           - a file pathname. See the above for the file format.
           - it should be ignored if text_grid is not None.
           - the file specified by file_path should exists, so there
             is no need for error handling
           Please call open_grid to open the file
        @type text_grid: List[str]
        @rtype: None
        >>> g = Grid("", ["B.++", ".+..", "...T"])
        >>> g.text_grid
        ['B.++', '.+..', '...T']
        >>> g = Grid("", None)
        >>> g.text_grid
        ['..+..++', '++.B..+', '.....++', '++.....', '.T....+']
        """
        # TODO
        check = ''
        if file_path is check and text_grid is None:
            text_grid = ["..+..++", "++.B..+", ".....++", "++.....", ".T....+"]
        elif file_path is check:
            self.text_grid = text_grid
        else:
            text_grid = self.open_grid(file_path).readlines()
            for i in range(len(text_grid)):
                text_grid[i] = text_grid[i][:-2]
        self.text_grid = text_grid
        self.width = len(self.text_grid[0])
        self.height = len(self.text_grid)
        self.dict = {
            'NW': (-1, -1),
            'N': (0, -1),
            'NE': (1, -1),
            'E': (1, 0),
            'SE': (1, 1),
            'S': (0, 1),
            'SW': (-1, 1),
            'W': (-1, 0)
        }
        self.map = [[0 for i in range(self.height)] for j in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                if text_grid[y][x] == '.':
                    self.map[x][y] = Node(True, x, y)
                    continue
                if text_grid[y][x] == '+':
                    self.map[x][y] = Node(False, x, y)
                    continue
                if text_grid[y][x] == 'B':
                    self.map[x][y] = Node(True, x, y)
                    self.boat = Node(True, x, y)
                    self.boat.in_path = True
                    continue
                if text_grid[y][x] == 'T':
                    self.map[x][y] = Node(True, x, y)
                    self.treasure = Node(True, x, y)
                    self.treasure.in_path = True
                    continue
        pass

    @classmethod
    def open_grid(cls, file_path):
        """
        @rtype TextIOWrapper: 
        """
        return open(file_path)

    def __str__(self):
        """
        Return a string representation.

        @type self: Grid
        @rtype: str

        >>> g = Grid("", ["B.++", ".+..", "...T"])
        >>> print(g)
        B.++
        .+..
        ...T
        """
        # TODO
        g = ''
        for i in range(len(self.text_grid)):
            g += str(self.text_grid[i] + '\n')
        g = g[:-1]
        return g

    def move(self, direction):
        """
        Move the boat in a specific direction, if the node
        corresponding to the direction is navigable
        Else do nothing

        @type self: Grid
        @type direction: str
        @rtype: None

        direction may be one of the following:
        N, S, E, W, NW, NE, SW, SE
        (north, south, ...)
        123
        4B5
        678
        1=NW, 2=N, 3=NE, 4=W, 5=E, 6=SW, 7=S, 8=SE
        >>> g = Grid("", ["B.++", ".+..", "...T"])
        >>> g.move("S")
        >>> print(g)
        ..++
        B+..
        ...T
        """
        # TODO
        boat_x = self.boat.grid_x
        boat_y = self.boat.grid_y
        (potential_x, potential_y) = self.dict[direction]
        if self.check_valid_move(boat_x + potential_x, boat_y + potential_y) is True:
            self.text_grid[boat_y + potential_y] = self.text_grid[boat_y + potential_y][:boat_x + potential_x] + 'B' + \
                                                   self.text_grid[boat_y + potential_y][boat_x + potential_x + 1:]
            self.text_grid[boat_y] = self.text_grid[boat_y][:boat_x] + '.' + self.text_grid[boat_y][boat_x + 1:]
            self.boat.grid_x += potential_x
            self.boat.grid_y += potential_y
        pass

    def check_valid_move(self, prop_boat_x, prop_boat_y):
        '''
        Checks if the boat can navigate in that direction
        @type self: Grid
        @type prop_boat_x: int
        @type prop_boat_y: int
        >>> g = Grid("", ["B.++", ".+..", "...T"])
        >>> g.check_valid_move(2,0)
        False
        >>> g.check_valid_move(3,3)
        False
        '''
        if prop_boat_x < 0 or prop_boat_y < 0 or prop_boat_x > self.width - 1 or prop_boat_y > self.height - 1:
            return False
        if self.map[prop_boat_x][prop_boat_y].navigable is False:
            return False
        return True

    # def find_boat(self):
    #     '''
    #     Finds the current position of boat
    #     '''
    #     for i in range(len(self.text_grid)):
    #         try:
    #             if (type(self.text_grid[i].index("B")) == int):
    #                 self.boat.grid_x = self.text_grid[i].index("B")
    #                 self.boat.grid_y = i
    #         except ValueError:
    #             pass
    # def find_treasure(self):
    #     '''
    #     Finds the current position of boat
    #     '''
    #     for i in range(len(self.text_grid)):
    #         try:
    #             if (type(self.text_grid[i].index("T")) == int):
    #                 self.treasure.grid_x = self.text_grid[i].index("T")
    #                 self.treasure.grid_y = i
    #         except ValueError:
    #             pass

    # def find_path(self, start_node, target_node):
    #     """
    #     Implement the A-star path search algorithm
    #     If you will add a new node to the path, don't forget to set the parent.
    #     You can find an example in the docstring of Node class
    #     Please note the shortest path between two nodes may not be unique.
    #     However all of them have same length!
    #
    #     @type self: Grid
    #     @type start_node: Node
    #        The starting node of the path
    #     @type target_node: Node
    #        The target node of the path
    #     @rtype: None
    #     >>> g = Grid("", ["B.++", ".+..", "...T"])
    #     >>> g.find_path(g.boat,g.treasure)
    #     >>> g.treasure.parent is None
    #     False
    #     """
    #
    #     # TODO
    #
    #     def shorter(a, b):
    #         '''
    #         Comparing the f costs of the 2 nodes
    #         @type a: Node
    #         @type b: Node
    #         '''
    #         return a.f < b.f
    #
    #     start_node.gcost = 0
    #     start_node.hcost = Node.distance(start_node, target_node)
    #     start_node.f = start_node.fcost()
    #     open_list = PriorityQueue(shorter)
    #     open_list.add(start_node)
    #     is_found = False
    #     closed_list = []

        while open_list.is_empty() is not True or is_found is False:
            q = open_list.remove()

            for i in range(3):
                for j in range(3):
                    if self.check_valid_move(q.grid_x + i - 1, q.grid_y + j - 1) is False:
                        continue
                    successor = Node(True, q.grid_x + i - 1, q.grid_y + j - 1)
                    successor.parent = q
                    add = True
                    if successor == q:
                        add = False
                    if successor == target_node:
                        self.treasure = successor
                        return
                    successor.gcost = q.gcost + Node.distance(q, successor)
                    successor.hcost = Node.distance(successor, target_node)
                    # successor.f = Node.fcost(successor)
                    if successor in open_list:
                        add = False
                    # for k in range(len(open_list._queue)):
                    #     if successor == open_list._queue[k]:
                    #         if successor.f >= open_list._queue[k].f:
                    #             add = False
                    if self.traverse_closed_list(successor, closed_list):
                        add = False
                    # for x in range(len(closed_list)):
                    #     if successor == closed_list[x]:
                    #         if successor.f >= closed_list[x].f:
                    #             add = False
                    if add is True:
                        open_list.add(successor)
            closed_list.append(q)
        pass

    def retrace_path(self, start_node, target_node):
        """
        Return a list of Nodes, starting from start_node,
        ending at target_node, tracing the parent
        Namely, start from target_node, and add its parent
        to the list. Keep going until you reach the start_node.
        If the chain breaks before reaching the start_node,
        return and empty list.

        @type self: Grid
        @type start_node: Node
        @type target_node: Node
        @rtype: list[Node]
        """
        # TODO
        pass

    def get_treasure(self, s_range):
        """
        Return treasure node if it is located at a distance s_range or
        less from the boat, else return None
        @type s_range: int
        @rtype: Node, None
        """
        # TODO
        pass

    def plot_path(self, start_node, target_node):
        """
        Return a string representation of the grid map,
        plotting the shortest path from start_node to target_node
        computed by find_path using "*" characters to show the path
        @type self: Grid
        @type start_node: Node
        @type target_node: Node
        @rtype: str
        >>> g = Grid("", ["B.++", ".+..", "...T"])
        >>> print(g.plot_path(g.boat, g.treasure))
        B*++
        .+*.
        ...T
        """
        # TODO
        pass

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    import python_ta
    python_ta.check_all(config='pylintrc.txt')
