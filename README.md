# 8-puzzle

This is the first project of the course CS205 in UCR Spring 2021 \
Author: Letong Wang

## File Description
**game.py**

It is the algorithm code, which includes 8-puzzle related functions and the general search algorithm. You can not directly run it, because it does not have main function.  It is like a header file included by other files.

**test.py**

It is code for testing. You can run it by "python test.py". It hardcoded eight solvable 8-puzzle cases and one 15-puzzle case as input, and ran three research algorithms on each of them. 

**play.py**

It is the interactive code, where you can give it an input as you like. You can run it by "python play.py". It will firstly ask you to choose whether 8-puzzle or 15-puzzle, and the answer shoule be number 8 or 15.
Then it will ask you to input an initial state, like [1,2,3,4,5,6,7,8,0], which begins with "[", ends with "]" and is seperated by ",". 
If the input format is invalid, it will tell you "Invlid Input", otherwise, it will print the result of the search.

