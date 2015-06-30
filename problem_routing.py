from problem import Problem
import csv


class ProblemRouting(Problem):
    """
    Inherits Problem and adds file reading, conversion from names to postal codes etc.
    """

    # Locations and roads are crude representation of world, loaded from appropriate csv files.
    locations = []
    roads = []

    def __init__(self, source_location, destination_location):
        """
        Contrary to parent class which accepts search states, this baby accepts location names and converts them to
        postal codes, which are in fact states. So first we need to load the data from csv files, then we need to
        translate user provided values to states(eg: value: Beograd -> state: 11000)
        """

        # Load the list of allowed locations.
        with open('data/locations.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                postal_code, location_name = row
                self.locations.append((int(postal_code), location_name.strip()))

        # Load the list of roads between allowed locations.
        with open('data/roads.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                origin, destination, kilometers, comment = row
                self.roads.append((int(origin), int(destination), float(kilometers)))

        # Translate user provided values to states
        root_state = self.get_post_code(source_location)
        goal_state = self.get_post_code(destination_location)

        # Continue with parent's init.
        super(ProblemRouting, self).__init__(root_state, goal_state)

    def successors_get(self, state):
        """
        Basically, we are trying to get all the outbound roads for the given city
        (or successor states for the given state).

        NB: currently, this function does not know about previously uncovered nodes!
        """

        road_indices = [i for i, v in enumerate(self.roads) if (v[0] == state or v[1] == state)]

        successors = []

        for road_index in road_indices:
            if self.roads[road_index][0] == state:
                successor_state = self.roads[road_index][1]
            else:
                successor_state = self.roads[road_index][0]
            successors.append(successor_state)

        return successors

    def cost_get(self, state1, state2):
        """
        This is ugly function, especially because I already had the price in successors_get.
        But I felt it would be better to decouple states from prices, in terms of more flexibility in search class.

        @todo: See if there is a better, more pythonic way.
        """
        road_indices = [i for i, v in enumerate(self.roads) if ((v[0] == state1 and v[1] == state2) or (v[0] == state2 and v[1] == state1))]
        if len(road_indices) == 0:
            raise ValueError("Cost of change from state1 to state2 could not be calculated.")
        return self.roads[road_indices[0]][2]

    def heuristics_get(self, state):
        """
        Let's presume this will work...
        In order to have a nice heuristics, I will probably have to maintain coordinates of locations.

        1. Get latitude and longitude for the given postal_code (state)
        2. Use pythagorean theorem to get the straight line length between the state and the destination location
        3. Return the length.

        """
        return 0

    def get_post_code(self, location_name):
        """
        For the given name of location, returns its postal code. It is ugly, especially due to fact that we are never
        routing from city to city, but cross section to cross section but still... This is a student project...
        """
        post_codes = [i for i, v in enumerate(self.locations) if v[1] == location_name]

        # Raise the error if location could not be found.
        if len(post_codes) == 0:
            raise ValueError(location_name + " is not a valid location.")

        return self.locations[post_codes[0]][0]

    def get_location_name(self, post_code):
        """
        For the given post code, returns its name.
        """
        locations = [i for i, v in enumerate(self.locations) if v[0] == post_code]
        if len(locations) == 0:
            return ''
        return self.locations[locations[0]][1]