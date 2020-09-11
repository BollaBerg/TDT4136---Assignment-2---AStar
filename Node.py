from typing import Tuple, Set

class Node:
    """The Node to be used when traversing the map.

    Has the following properties:

        position     : tuple, with (x,y)-coordinates for the node
        cost_to_node : cost of getting to the node
        cost_to_goal : estimated cost of getting to the goal
        cost_total   : estimated total cost. Sum of the other costs
        parent       : pointer to parent, shows best route to this node
        kids         : list of successor node, used to update children
    """

    def __init__(self, position : Tuple[int, int],
                goal_pos : Tuple[int, int],
                closed_set : Set,
                parent : 'Node',
                cost_of_step : int,
                cost_to_node : int,
                task : int):
        self.position = position
        self.parent = parent

        self.cost_of_step = cost_of_step
        self.cost_to_node = cost_to_node

        self.cost_to_goal = abs(self.position[0] - goal_pos[0]) + abs(self.position[1] - goal_pos[1])
        if task == 5:
            expected_movement = int(abs(self.position[1] - goal_pos[1]) / 4)
            self.cost_to_goal = abs(self.position[0] - goal_pos[0]) + \
                                abs(self.position[1] - goal_pos[1] - expected_movement)

        self.closed_set = closed_set

        self.kids = []

    def __eq__(self, other):
        return type(self) == type(other) and self.position == other.position

    def __lt__(self, other : 'Node'):
        return self.cost_total < other.cost_total

    def __hash__(self):
        return hash(self.position)

    def __str__(self):
        return F"Node{self.position}: {self.cost_total}"

    def __repr__(self):
        return str(self)

    @property
    def cost_total(self):
        return self.cost_to_node + self.cost_to_goal

    def add_kid(self, kid : 'Node'):
        if kid not in self.kids:
            self.kids.append(kid)

    def update_kids(self):
        """Update kids. Runs update_value for all kids not in closed_set"""
        for kid in self.kids:
            if kid in self.closed_set:
                continue
            kid.update_value(self.cost_to_node + kid.cost_of_step, self)


    def update_value(self, cost_to_node : int, parent : 'Node'):
        """Update values. Should be called when a parent updates

        :param cost_to_node: New cost to this node
        :param parent: Parent through which the new route goes
        :returns: nothing.
        """
        if cost_to_node >= self.cost_to_node:
            return
        
        self.cost_to_node = cost_to_node
        self.parent = parent

        self.update_kids()

    def update_goal(self, goal_pos):
        self.cost_to_goal = abs(self.position[0] - goal_pos[0]) + abs(self.position[1] - goal_pos[1])
