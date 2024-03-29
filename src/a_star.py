from heapq import heapify, heappush, heappop

from src.Map import Map_Obj
from src.Node import Node

def a_star(task : int):
    map_obj = Map_Obj(task)
    closed_set = set()
    node_queue = []

    # Initialize goal_pos (used when creating nodes later) and goal_node (used to compare nodes later)
    goal_pos = map_obj.get_goal_pos()
    goal_node = Node(goal_pos, goal_pos, closed_set, None, map_obj.get_cell_value(goal_pos), float('Inf'), task)

    # Intialize start_node (the first node) and add it to node_queue
    start_node = Node(map_obj.get_start_pos(), goal_pos, closed_set, None, 0, 0, task)
    node_queue.append(start_node)

    while(True):
        if len(node_queue) < 1:
            # No nodes in node_queue --> No path found
            status, value = 404, "No path found"
            break

        # Current node is the node with the lowest expected total cost
        # Remove current_node from node_queue and add it to closed_set
        current_node = heappop(node_queue)
        closed_set.add(current_node)

        # Currently at goal_node ==> Path has been found!
        if current_node == goal_node:
            status = 0
            break

        # Iterate through neighbors in order to find kids
        for change_in_position in [(-1,0), (1,0), (0,-1), (0,1)]:
            temp_position = tuple(row + col for row, col in zip(current_node.position, change_in_position))

            # Get node cost and check if temp_position is illegal (value = -1), if so --> skip it
            temp_cost = map_obj.get_cell_value(temp_position)
            if temp_cost < 1:
                continue

            # Set temp_kid to be a node with position == temp_position
            try:
                # See if there exists a node with this position in node_queue
                temp_kid = next(kid for kid in node_queue if kid.position == temp_position)
            except StopIteration:
                # If no existing Node was found above - create new node and add to queue
                temp_kid = Node(temp_position, goal_pos, closed_set,
                                parent=current_node,
                                cost_of_step=temp_cost,
                                cost_to_node=current_node.cost_to_node + temp_cost,
                                task=task)

                # Ensure the new Node is not in closed set (meaning it has already been visited)
                if temp_kid in closed_set:
                    continue

                # Kid is actually a new node - add it to node_queue
                heappush(node_queue, temp_kid)

            # Add the kid to current_node's kids
            current_node.add_kid(temp_kid)


        # At this point, current_node has NOT been updated, but it does have all its kids.
        # The node will not itself change any values (as no path can be shorter than the current
        # path), but its kids might
        # It is therefore safe to run update_kids()
        current_node.update_kids()


        # Update goal. tick() is used in task 5 to update goal
        if task == 5:
            goal_pos, goal_moved = map_obj.tick()

            if goal_moved:
                for node in node_queue:
                    node.update_goal(goal_pos)

                goal_node.position = goal_pos

            # Edge case where the goal is updated "into" current_node
            if current_node.position == tuple(goal_pos):
                status = 0
                break
        # End task 5

        # Finalize the loop by heapifying node_queue, in order to ensure correct order
        heapify(node_queue)


    if status == 404:
        print(value)
        return
    
    # At this point, status should be 0 and current_node == goal_node
    assert(status == 0)


    # Iterate through path to update the map (to be able to print correctly)
    # Avoid iterating through start_node and end_node (to keep those different colors)
    current_node = current_node.parent
    while(current_node != start_node):
        map_obj.set_cell_value(current_node.position, "o")
        current_node = current_node.parent


    # Save file at the end
    map_obj.save_map(filename = F"results/Astar - task {task}")

        
if __name__ == "__main__":
    a_star(1)
