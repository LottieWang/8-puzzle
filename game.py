import heapq
class EightPuzzle:
    def __init__(self):
        self.width=3
        self.size = self.width * self.width -1
        self.end_state = [1,2,3,4,5,6,7,8,0]
    def switch(self, a, i,j):
        t = a[i]
        a[i]=a[j]
        a[j]=t
    # def set_state(self, a):
    #     self.state = a.copy()
    def get_next(self, state):
        index  = state.index(0)
        i = index // self.width
        j = index % self.width
        next_states = []
        if i>0:
            new_state = state.copy()
            self.switch(new_state, index, index-self.width)
            next_states.append(new_state)
        if i<self.width-1:
            new_state = state.copy()
            self.switch(new_state,index, index+self.width)
            next_states.append(new_state)
        if j>0:
            new_state = state.copy()
            self.switch(new_state,index, index-1)
            next_states.append(new_state)
        if j<self.width-1:
            new_state = state.copy()
            self.switch(new_state,index,index+1)
            next_states.append(new_state)
        return next_states
    def if_end(self, state):
        return state == self.end_state
    def misplace_distance(self,  state):
        n_misplace = 0
        for i in range(self.size):
            if (self.end_state[i]!= state[i]):
                n_misplace +=1
        return n_misplace
    def manhattan_distance(self, state):
        distance = 0
        for i in range(self.width * self.width):
            if state[i] == 0:
                continue
            if state[i] == self.end_state[i]:
                continue
            desired_i = (state[i]-1)//self.width
            desired_j = (state[i]-1)% self.width
            index_i = i //self.width
            index_j = i % self.width
            distance += abs(index_i - desired_i) + abs(index_j - desired_j)
        return distance
    def encode(self, state):
        ans = 0
        for i in range(self.width * self.width):
            ans = ans*10 + state[i]
        return ans
    def decode(self, state):
        ans = []
        for i in range(self.width*self.width):
            ans.append(state % 10)
            ans = ans // 10
        ans.reverse()
        return ans
# @total_ordering
class node:
    def __init__(self,state, distance, heuristic):
        self.state = state
        self.distance = distance
        self.heuristic = heuristic
    def __le__(self, other):
        return self.distance+self.heuristic <= other.distance + other.heuristic
    def __lt__(self, other):
        return self.distance+self.heuristic < other.distance + other.heuristic
            

def general_search(game, heuristic_func, initial_state):
    visited = set()
    initial_node = node(initial_state, 0, heuristic_func(initial_state))
    working_queue = []
    heapq.heappush(working_queue, initial_node)
    while(len(working_queue)>0):
        current_node = heapq.heappop(working_queue)
        visited.add(game.encode(current_node.state))
        if game.if_end(current_node.state):
            return True
        #expand
        next_states = game.get_next(current_node.state)
        for state in next_states:
            if (game.encode(state) in visited):
                continue
            heapq.heappush(working_queue, node(state, current_node.distance+1,  heuristic_func(state)));
    return False


def main():
    game = EightPuzzle()
    initial_state =  [1,2,3,4,5,6,8,7,0]
    ans = general_search(game, lambda a: 0, initial_state)
    print(ans)

if __name__ == "__main__":
    main()