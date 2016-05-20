

"""
class manager:
    def __init__(self):
        self.junctions_dict = {}  # all the junctions: key is the junction id, value is the junction's object itself
        self.neighbors_dict = {}  # key is junction id, value is a list of four-ples: the junction's neighbors' ids, the lane id of the junction in key for where they enter, the lane id of the junction in value from where they exit, their distance
        self.junction_id = 0  # also the counter of the number of junctions


    def add_junction(self):
        self.junction_id = self.junction_id + 1
        new_junction = junction([]) # TODO lanes array ?
        self.junctions_dict[self.junction_id] = new_junction


    def get_junction_by_id(self, junction_id):
        pass
"""


# we need to calculate for each lane in each junction, the number of cars that want to reach this lane
def get_entering_cars_number(junction_id):
    sum = 0
    current_junction = get_junction_by_id(junction_id)
    result = l = [[[0, 0], [0, 0], [0, 0], [0, 0]]]*4
    neighbors = get_neighbors(junction_id)
    for neighbor in neighbors:
        neighbor_lights = neighbor.get_lights();  # 4x4 array of pair (boolean light state, time in this state)
        neighbor_stats = neighbor.get_stats();  # 4x4 array - on each entry there is a list of numbers (that represent time that each car on this lane alredy waits)
        relevant_lane = get_relevant_lane(junction_id, neighbor.get_id())
        neighbor_exit_lane = get_neighbor_exit_lane(junction_id, neighbor.get_id())
        for i in xrange(4):
            result[relevant_lane][i][1] = get_distance(junction_id, neighbor.get_id())
            if neighbor_lights[i][neighbor_exit_lane]:
                sum =+ len(neighbor_stats[i][neighbor_exit_lane])
        for i in xrange(4):
            result[relevant_lane][i][0] = sum*current_junction.get_prob(relevant_lane,i)
        sum = 0