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

    def sort(self):
        # Sort the queue by price (2nd element of tuple).
        self.queue.sort(key=lambda tup: tup[1])


class Search:
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

        print "Parameters:"
        print "====================================="
        print "From: " + self.source_id.__str__()
        print "To: " + self.destination_id.__str__()
        print "====================================="


        while True:
            output = self.iterate()
            if output != 0:
                break


    def iterate(self):
        node_id, node_price, node_parents = self.queue.get_cheapest_child()

        # print node_id
        # print node_price
        # print node_parents

        # End of search. Route found!
        if node_id == self.destination_id:
            print node_parents.__str__()
            print node_price.__str__()
            return 1

        children = self.geography.get_outbount_roads(node_id)

        ancesters = list(node_parents)
        ancesters.append(node_id)

        for child in children:
            if not child[0] in ancesters:
                self.queue.add_child(child[0], child[1] + node_price, ancesters)

        self.queue.sort()

        # print "Idemo:"
        # print node_id
        # print self.queue.queue.__str__()

        return 0