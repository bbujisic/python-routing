__author__ = 'bbujisic'

from geography import Geography


class Queue:
    def __init__(self, sourceID):
        self.queue = [(sourceID, 0, [])]

    def add_child(self, id, price, ancesters):
        # Adds a child to the queue list.
        self.queue.append((id, price, ancesters))

    def get_cheapest_child(self):
        # Returns cheapest child and removes it from the queue list.
        return self.queue.pop(0)

    def count(self):
        # Returns cheapest child and removes it from the queue list.
        return len(self.queue)

    def sort(self):
        # Sort the queue by price (2nd element of tuple).
        self.queue.sort(key=lambda tup: tup[1])


class Search:
    count_nodes = 0
    selected_route = []
    selected_route_price = 0

    search_depth = 0

    def __init__(self, source, destination):
        self.geography = Geography()

        self.source_id = self.geography.get_post_code(source)
        self.destination_id = self.geography.get_post_code(destination)

        if self.source_id == -1:
            raise ValueError(source + " is not a valid location.")

        if self.destination_id == -1:
            raise ValueError(destination + " is not a valid location.")

        # Add root element to the search queue
        self.queue = Queue(self.source_id)

    def go(self):
        while True:
            output = self.iterate()
            if output == -1:
                return "Route could not be calculated."
            if output == 1:
                return "Route successfully calculated."


    def iterate(self):

        # End of search. No route found.
        if self.queue.count() == 0:
            return -1

        # Load next candidate for search. Still decoupled from geography!
        node_id, node_price, node_parents = self.queue.get_cheapest_child()

        # It is easier to me to store information of all ancestors within child's tuple, even though it is not
        # efficient. @todo: See to keep separate list with active tree. That way we won't waste too much memory.
        ancestors = list(node_parents)
        ancestors.append(node_id)

        # Increase node counter. It's a benchmark thing.
        self.count_nodes += 1
        if len(ancestors) != self.search_depth:
            self.search_depth = len(ancestors)
            print self.count_nodes.__str__() + ' | ' + self.queue.count().__str__() + ' | ' + len(ancestors).__str__()


        # End of search. Route found!
        # @todo: Maybe switch destination_id to target_state_id -- something more decoupled from geography.
        if node_id == self.destination_id:
            self.selected_route = ancestors
            self.selected_route_price = node_price
            return 1

        # Load all the node's children.
        # @todo: Decouple from geography by renaming the function to get_children!
        children = self.geography.get_outbound_roads(node_id)

        # Iterate through children, create nodes (which are basically 3-item tupples) and add them to the queue.
        for child in children:
            if not child[0] in ancestors:
                # NB: child price is a sum of entire branch's price.
                # @todo: Something appears to be wrong in price calculation!
                self.queue.add_child(child[0], child[1] + node_price, ancestors)

        # Oh man! This is EXTREMELY expensive procedure!
        self.queue.sort()

        return 0