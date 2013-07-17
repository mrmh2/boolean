import itertools
from pprint import pprint

class BooleanNetwork(object):

    def __init__(self, size, start_state=None):
        self.size = size
        if start_state is None:
            self.state = [0] * size
        else:
            assert(len(start_state) == size)
            self.state = start_state

    def __repr__(self):
        return ''.join(str(i) for i in self.state)

    def update(self, update_rule):
        self.state = update_rule(self.state)
        
        
def up3(current_state):
    new_state = [0] * len(current_state)

    new_state[0] = current_state[1]
    new_state[1] = int(current_state[0] or current_state[2])
    new_state[2] = current_state[1]

    return tuple(new_state)


def update_network(network):
    new_state = network[:]

    new_state[0] = int(not(network[1]))
    new_state[1] = network[0]

    return new_state

def all_states(n):
    sl = [[0, 1]] * n
    state_it = itertools.product(*sl)
    return state_it

def main():
    bn = BooleanNetwork(3, [0, 0, 1])
    state_map = {s: up3(s) for s in all_states(3)}
    pprint(state_map)

if __name__ == '__main__':
    main()
