class Node:
    def __init__(self, _state, _parent=None, _action=None, _cost=0):
        self.state = _state
        self.parent = _parent
        self.action = _action
        self.cost = _cost

    def total_path(self):
        path = []
        curr = self
        while curr.parent is not None:
            path.append(curr.action)
            curr = curr.parent
        return list(reversed(path))

    def __eq__(self, other):
        return self.state == other.state

