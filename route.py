__author__ = 'bbujisic'
import sys

from search import Search

def route(source, destination):
    search = Search(source, destination)



if __name__ == '__main__':
    total = len(sys.argv)

    if total > 2:
        route(sys.argv[1], sys.argv[2])
    else:
        print "You need two arguments, first one would be source, and second one target of your routing."