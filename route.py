__author__ = 'bbujisic'
import sys

'''
@todo: Isolate function which decides price of child node.
@todo: Refactor to be more by the book.
@todo: See if you can move geography to separate JSON files.
'''

from search import Search


def route(source, destination):
    search = Search(source, destination)


if __name__ == '__main__':
    total = len(sys.argv)

    if total > 2:
        route(sys.argv[1], sys.argv[2])
    else:
        print "You need two arguments, first one would be source, and second one target of your routing."