from Game import EightPuzzle
from Game import FifteenPuzzle
from Game import general_search

def test(game,state):
    print("uniform search:")
    ans = general_search(game, lambda a:0, state)
    print(ans)
    print("A* search with misplace heuristic:")
    ans = general_search(game, game.misplace_distance, state)
    print(ans)
    print("A* search with manhatan distance:")
    ans = general_search(game, game.manhattan_distance, state)
    print(ans)

def main():
    game = EightPuzzle()
    states=[[1,2,3,4,5,6,7,8,0],[1,2,3,4,5,6,0,7,8],
    [1,2,3,5,0,6,4,7,8],[1,3,6,5,0,2,4,7,8],
    [1,3,6,5,0,7,4,8,2],[1,6,7,5,0,3,4,8,2],
    [7,1,2,4,8,5,6,3,0],[0,7,2,4,6,1,3,5,8]]
    for i in range(len(states)):
        print("test {}".format(i))
        print(states[i])
        test(game,states[i])
        print("----------------------------")
    print("testing for 15 puzzle")
    print("----------------------------")
    game2=FifteenPuzzle()
    state=[1,2,3,4,5,6,7,8,9,10,11,12,13,0,14,15]
    test(game2,state)

if __name__ == "__main__":
    main()