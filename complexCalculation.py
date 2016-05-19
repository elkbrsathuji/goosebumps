# in manager:
junctions_dict = {}  # all the junctions: key is the junction id, value is the junction's object itself
neighbors_dict = {}  # key is junction id, value is triplet: the junction's neighbors' ids, the lane of the junction in key for where they enter, their distance

# we need to calculate for each lane in each junction, the number of cars that want to reach this lane
def get_entering_cars_number(junction_id):
    sum = 0
    result = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
    neighbors = get_neighbors(junction_id)
    for neighbor in neighbors:
        neighbor_lights = neighbor.get_lights();  # 4x4 array of pair (boolean light state, time in this state)
        neighbor_stats = neighbor.get_stats();  # 4x4 array - on each entry there is a list of numbers (that represent time that each car on this lane alredy waits)

