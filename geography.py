# coding=utf-8
__author__ = 'bbujisic'

import csv


class Geography:
    locations = []
    roads = []

    def __init__(self):
        """
        Geography class constructor loads data from roads.csv and locations.csv and fills in appropriate attributes.
        """

        # @todo: Handle exceptions!
        with open('locations.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                postal_code, location_name = row
                self.locations.append((int(postal_code), location_name.strip()))

        # @todo: Handle exceptions!
        with open('roads.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                origin, destination, kilometers, comment = row
                self.roads.append((int(origin), int(destination), float(kilometers)))

    def get_post_code(self, location_name):
        """
        For the given name of location, returns its postal code. It is ugly, especially due to fact that we are never
        routing from city to city, but cross section to cross section but still... This is a student project...
        """
        post_codes = [i for i, v in enumerate(self.locations) if v[1] == location_name];
        if len(post_codes) == 0:
            return -1
        return self.locations[post_codes[0]][0]

    def get_location_name(self, post_code):
        """
        For the given post code, returns its name.
        """
        locations = [i for i, v in enumerate(self.locations) if v[0] == post_code]
        if len(locations) == 0:
            return ''
        return self.locations[locations[0]][1]

    def get_outbound_roads(self, post_code):
        """
        For the given location, returns all the connected locations with distance to them.
        """
        # Find all roads originating from given post code.
        road_indices = [i for i, v in enumerate(self.roads) if (v[0] == post_code or v[1] == post_code)]

        outbound_roads = []

        # Normalize results in tuples with destination road and price.
        for road_index in road_indices:
            if self.roads[road_index][0] == post_code:
                outbound_roads.append((self.roads[road_index][1], self.roads[road_index][2]))
            else:
                outbound_roads.append((self.roads[road_index][0], self.roads[road_index][2]))

        return outbound_roads