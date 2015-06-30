class Problem(object):

    def __init__(self, root_state, goal_state):
        self.root_state = root_state
        self.goal_state = goal_state

    def successors_get(self, state):
        pass

    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False

    def cost_get(self, state1, state2):
        return 0

    def heuristics_get(self, state):
        return 0