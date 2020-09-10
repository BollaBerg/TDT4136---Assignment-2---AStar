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

    def __init__(self, position, parent = None, cost_of_step = 1, cost_to_node = 0, cost_to_goal = 0):
        self.position = position
        self.parent = parent

        self.cost_of_step = cost_of_step
        self.cost_to_node = cost_to_node
        self.cost_to_goal = cost_to_goal

        self.kids = []

    def __eq__(self, other):
        return self.position == other.position

    @property
    def cost_total(self):
        return self.cost_to_node + self.cost_to_goal

    def add_kid(self, kid):
        self.kids.append(kid)

    def update_kids(self):
        """Update kids. Should only be called in update_value()!"""
        for kid in self.kids:
            if kid in closed_set:
                continue
            kid.update_value(self.cost_to_node + kid.cost_of_step, self)


    def update_value(self, cost_to_node, parent):
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
