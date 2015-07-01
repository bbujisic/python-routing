from problem_routing import ProblemRouting
from search import Search, PathNotFoundException
import sys

if __name__ == '__main__':

    debug = False
    total = len(sys.argv)

    if total <= 2:
        print "You need two arguments, first one would be source, and second one target of your routing."
        exit()

    # Instantiate the problem
    source_location, destination_location = sys.argv[1], sys.argv[2]

    try:
        problem = ProblemRouting(source_location, destination_location)
    except ValueError as e:
        print "============================"
        print "Routing failed"
        print "============================"
        print e
        print "============================"
        exit()

    # Instantiate the search object
    search = Search(problem)

    try:
        path = search.go('astar')
    except PathNotFoundException:
        print "============================"
        print "Routing failed"
        print "============================"
        print "From: " + source_location
        print "To: " + destination_location
        print "============================"
        print "Route does not exist"
        print "============================"
    else:
        print "============================"
        print "Routing succeeded"
        print "============================"
        print "From: " + source_location
        print "To: " + destination_location
        print "============================"
        for postal_code in path:
            print problem.get_location_name(postal_code)
        print "============================"
