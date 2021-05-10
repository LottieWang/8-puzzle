from game import EightPuzzle
from game import FifteenPuzzle
from game import general_search

def test(game,state):
    print("uniform search: ")
    ans = general_search(game, lambda a:0, state)
    print("     explored nodes: {} depth: {}".format(ans[1], ans[2]))
    print("A* search with misplace heuristic: ")
    ans = general_search(game, game.misplace_distance, state)
    print("     explored nodes: {} depth: {}".format(ans[1], ans[2]))
    print("A* search with manhatan distance: ")
    ans = general_search(game, game.manhattan_distance, state)
    print("     explored nodes: {} depth: {}".format(ans[1], ans[2]))

def main():
    mode = eval(input("8-puzzle or 15-puzzle? type 8 or 15: "))
    if mode == 8:
        game = EightPuzzle()
    elif mode == 15:
        game = FifteenPuzzle()
    else:
        print("Bad Input!")
        exit()
    try:
        if (mode == 8):
            state = eval(input("Please input an initial state, like: [1,2,3,4,5,6,7,8,0] \n"))
        else:
            state = eval(input("Please input an initial state, like: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0] "))
        if not game.is_valid(state):
            exit()
    except:
        print("Invalid Input State!")
        exit()
    
    print("The input state is: ")
    for i in range(game.size+1):
        print(state[i], end=' ')
        if (i % game.width == game.width-1):
            print("")
    ans = general_search(game, game.manhattan_distance, state)
    if not ans[0]:
        print("Not Solvable! Explored {} Nodes".format(ans[1]))
    else:
        test(game,state)
        

if __name__ == "__main__":
    main()
    
