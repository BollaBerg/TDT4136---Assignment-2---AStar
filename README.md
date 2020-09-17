# TDT4136 - Assignment 1 - A*
This is my (Andreas Berg's) solution to Assignment 1 in TDT4136 fall 2020.

---

## How to run the code
1) Navigate into the folder where the code is (whether it's from GitHub or the delivered zip-file)
2) Using pip, install all requirements (there are some):
```bash
pip install -r requirements.txt
```
3a) To solve all tasks, simply run the code. This will save all solutions as separate images titled `Astar - task i.jpeg` where i = task number.
```bash
python main.py
```

3b) To solve only some tasks, simply edit `main.py` to solve only some tasks, or have the following in your own python file:
```python
from src.a_star import a_star

a_star(i)   # Solve task i
```

---

## Assignment
The assignment is as follows:
> In this assignment, you will become familiar with the A* algorithm by applying it to a classical use case for A*, namely that of finding the shortest path in a two-dimensional grid-like world.

The assignment to move between different parts of a map (representing Studentersamfundet i Trondhjem). It is split into five separate tasks:

| Task          | Starting position     | Goal position                          | Comment |
| :-----------: | --------------------- | -------------------------------------- | ------- |
| 1             | Rundhallen (27,18)    | Strossa (40,32)                        | Basic A* |
| 2             | Strossa (40,32)       | Selskapssiden (8,5)                    | Basic A* |
| 3             | Lyche (28,32)         | Klubben (6,32)                         | Steps have varying cost |
| 4             | Lyche (28,32)         | Klubben (6,32)                         | Steps have varying cost. Edgar is packed (slow) |
| 5 (optional)  | Rytterhallen (14,18)  | Klubben (6,36) --> Selskapssiden (6,7) | Steps have varying cost. The goal moves 1/4 step every iteration of the algorithm |

All tasks come with a CSV-file representing tiles. These can be found in `./maps`

## Results
Color guide:

| Color  | Information |
| -----  | ----------- |
| ![red](https://via.placeholder.com/15/FF0000/000000?text=+) Red    | Walls / obstacles |
| ![Purple](https://via.placeholder.com/15/FF00FF/000000?text=+) Purple | Starting position |
| ![Blue](https://via.placeholder.com/15/0088FF/000000?text=+) Blue   | Goal position |
| ![Yellow](https://via.placeholder.com/15/FFFF00/000000?text=+) Yellow | Path found |
| ![Gray](https://via.placeholder.com/15/CCCCCC/000000?text=+) Gray   | Legal tiles |
| ![Gray 2](https://via.placeholder.com/15/A6A6A6/000000?text=+) ![Gray 3](https://via.placeholder.com/15/606060/000000?text=+) ![Gray 4](https://via.placeholder.com/15/242424/000000?text=+) Gray (task 3-5) | The darker the tile, the more expensive the tile is |

### Task 1
![Task 1](https://github.com/BollaBerg/TDT4136---Assignment-1---AStar/blob/master/results/A*%20-%20task%201.jpeg)

### Task 2
![Task 2](https://github.com/BollaBerg/TDT4136---Assignment-1---AStar/blob/master/results/A*%20-%20task%202.jpeg)

### Task 3
![Task 3](https://github.com/BollaBerg/TDT4136---Assignment-1---AStar/blob/master/results/A*%20-%20task%203.jpeg)

### Task 4
![Task 4](https://github.com/BollaBerg/TDT4136---Assignment-1---AStar/blob/master/results/A*%20-%20task%204.jpeg)

### Task 5
Note: The goal indicated is the final goal, meaning the place where the goal ended up. It has moved, I promise!
![Task 5](https://github.com/BollaBerg/TDT4136---Assignment-1---AStar/blob/master/results/A*%20-%20task%205.jpeg)
