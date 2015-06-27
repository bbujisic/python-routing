__author__ = 'bbujisic'
import sys
from geography import Geography


'''
@todo: Isolate function which decides price of child node.
@todo: Refactor to be more by the book.
'''

from search import Search


def route(source, destination):
    geography = Geography()
    search = Search(source, destination)

    result = search.go()

    print "Parameters:"
    print "====================================="
    print "From: " + source
    print "To: " + destination
    print "====================================="
    print result
    print "====================================="
    #print search.selected_route
    for postal_code in search.selected_route:
        print(geography.get_location_name(postal_code))
    print "====================================="
    print "Total number of nodes searched: " + search.count_nodes.__str__()


if __name__ == '__main__':
    total = len(sys.argv)

    if total > 2:
        route(sys.argv[1], sys.argv[2])
    else:
        print "You need two arguments, first one would be source, and second one target of your routing."