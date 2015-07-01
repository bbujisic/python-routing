__author__ = 'bbujisic'


class Search(object):
    fringe = []
    closed = []
    def __init__(self, problem):
        self.problem = problem
        root_node = Node(problem.root_state)
        self.fringe.append(root_node)

    def go(self, funct):
        while True:
            status = getattr(self, 'astar')()

            if status == 1:
                states = []
                for node in self.path:
                    states.append(node.state)
                return states

    def astar(self):

        # Check if fringe is empty. If yes -- return -1: status which signalizes that search completed without result
        if len(self.fringe) == 0:
            raise PathNotFoundException()

        # Find the next node (one with least cost) in the fringe.
        min_cost = min(node.cost for node in self.fringe)
        for parent_node in self.fringe:
            if parent_node.cost == min_cost:
                break

        # Check if we solved the problem (i.e. found searched node). If yes -- return 1.
        if self.problem.goal_test(parent_node.state):
            self.path = parent_node.get_path()
            return 1

        # Move the examined node from fringe to closed.
        self.closed.append(parent_node)
        self.fringe.remove(parent_node)

        # Load all possible successors to a given state.
        children = self.problem.successors_get(parent_node.state)

        # Add to fringe only the states that were not already examined.
        for child_state in children:
            if not any(closed_node.state == child_state for closed_node in self.closed):
                child_cost = self.problem.cost_get(parent_node.state, child_state)
                child_heuristics = self.problem.heuristics_get(child_state)
                self.fringe.append(Node(child_state, parent_node, child_cost + child_heuristics + parent_node.cost))

        return 0



class Node(object):
    """
    A node knows about itself, it knows about its parents and it knows about its depth.
    And it is responsible to return the list of all of its ancestors!
    """
    depth = 0

    def __init__(self, state, parent=None, cost=0):
        """
        Initialization of variables
        """
        self.state, self.parent, self.cost = state, parent, cost
        if parent:
            self.depth = parent.depth + 1

    def __str__(self):
        """
        Let's simply make the debugging beautiful...
        """
        return self.state + " (parent: " + self.parent.state + "; cost: " + self.cost + ")"


    def get_path(self):
        """
        Iterate through all node's parents and create a list out of them.
        """
        node, result = self, [self]
        while node.parent:
            result.append(node.parent)
            node = node.parent
        return list(reversed(result))


class PathNotFoundException(Exception):
    pass