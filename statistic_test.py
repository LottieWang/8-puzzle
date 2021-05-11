from game import EightPuzzle
from game import FifteenPuzzle
from game import general_search
import numpy as np

#return (depth, encoded state, uniform, A* mis, A* manhatan)
def test(game,state): 
    state_code = game.encode(state)
    ans_3 = general_search(game, game.manhattan_distance, state)
    print(state_code,  end = " ")
    if not ans_3[0]:
        print("Fail")
        return (-1,-1,-1,-1,-1)
    ans_1 = general_search(game, lambda a:0, state)
    ans_2 = general_search(game, game.misplace_distance, state)
    print("Success")
    return (ans_1[2],state_code , ans_1[1], ans_2[1], ans_3[1])

def collect_data(game, repeat):
    depth_dict = dict()   #key is the depth
    for i in range(repeat):
        print("test {}".format(i), end=" ")
        state = list(np.random.permutation(9))
        ans = test(game, state)
        if (ans[0]== -1): # not solvable
            continue
        depth = ans[0]
        state_code = ans[1]
        cost  = (ans[2], ans[3], ans[4])
        if depth not in depth_dict:
            depth_dict[depth] = dict()
        depth_dict[depth][state_code]=cost
    return depth_dict

def statistic(depth_dict):
    depth_items = depth_dict.items()
    sorted_depth = sorted(depth_items)
    n_depth = len(sorted_depth)
    depth_list= np.zeros(n_depth)
    search_1 = np.zeros(n_depth)
    search_2 = np.zeros(n_depth)
    search_3 = np.zeros(n_depth)
    for i in range(n_depth):
        depth_list[i] = sorted_depth[i][0]
        cost1=0
        cost2=0
        cost3=0
        print(sorted_depth[i][1])
        for s,cost in sorted_depth[i][1].items():
            cost1+=cost[0]
            cost2+=cost[1]
            cost3+=cost[2]
        search_1[i] = (cost1+0.0)/len(sorted_depth[i][1])
        search_2[i] = (cost2+0.0)/len(sorted_depth[i][1])
        search_3[i] = (cost3+0.0)/len(sorted_depth[i][1])
    print("Depth")
    print(depth_list)
    print("Uniform")
    print(search_1)
    print("A* with Mis")
    print(search_2)
    print("A* with Manhatan")
    print(search_3)

def main():
    game = EightPuzzle()
    depth_dict = collect_data(game, 1000)
    # depth_dict = {29: {786053421: (181062, 90841, 10943)}, 20: {251803746: (62494, 4482, 724)}}
    #print(depth_dict)
    statistic(depth_dict)
    

if __name__ == "__main__":
    main()
            


        
