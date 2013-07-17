import itertools
import pygraphviz as pgv
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

    new_state[0] = int(not(current_state[1]))
    new_state[1] = int(current_state[0] or current_state[2])
    new_state[2] = current_state[1]

    return tuple(new_state)

def up3_and(current_state):
    new_state = [0] * len(current_state)

    new_state[0] = int(not(current_state[1]))
    new_state[1] = int(current_state[0] and current_state[2])
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

def draw_state_map(update_rule, size, output_filename):
    state_map = {s: update_rule(s) for s in all_states(size)}
    G = pgv.AGraph(directed=True)
    [G.add_node(k) for k in state_map]
    [G.add_edge(k, v) for k, v in state_map.items()]
    G.layout(prog='dot')
    G.draw(output_filename)
    
def main():
    bn = BooleanNetwork(3, [0, 0, 1])
    output_filename = 'or.png'
    draw_state_map(up3, 3, output_filename)
    draw_state_map(up3_and, 3, 'and.png')

if __name__ == '__main__':
    main()
