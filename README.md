# python-routing

Okay, so, what I'm trying to achieve here is two things: to learn Python and to learn AI. Saying that, code in this repo is probably disturbingly bad. Once I learn Python and get to understand AI search concepts... I'll probably delete this paragraph and brag about excellence of this piece of code.

## Anyhow, what this code does is...

There are cities and villages (well, *locations*) in Serbia. And there are roads connecting them. And those roads have their lengths. And the network of roads allow you to reach from point A to point B using several routes. The code investigates all the possible routes and chooses the best one.

Currently it uses a sort of Dijkstra's algorithm. So the search is uninformed and has no idea on "where" the destination is compared to the current location. So the algorythm basically does following:
* It pops a cheapest node (i.e. one with shortest distance to current location)
* It investigates cheapest node's children (i.e. all the locations connected to the investigated location but the previously investigated location).
* It adds all the children to a node queue. And then resorts the queue by price (i.e. it sorts locations by distance ascending)
* Then it loops back to the next cheapest child.

Process breaks when loop reaches to child which is actually a destination of the search. Then it returns all the childs ancesters, which actually represent the shortest route to the child.

Process also breaks when all the children were investigated (end of node queue) without finding a child which is a destination. In that case, process should inform consumer that route between two locations could not be made.
