# coding=utf-8
__author__ = 'bbujisic'

# I have no idea how to connect Python with a database. But basic structure I want to create (well, emulate here) would
# be to have two tables (or lists). One would contain the list of locations (Belgrade, Pancevo, Novi Sad), another would
# contain roads and their lengths in kilometers (Belgrade - Pancevo - 19, Belgrade - Novi Sad - 78).

class Geography:

    locations = [
        (11000, "Beograd"),
        (21000, "NoviSad"),
        (21240, "Titel"),
        (21241, "Kac"),
        (26000, "Pancevo"),
        (26201, "Jabuka"),
        (26204, "Opovo"),
        (26210, "Kovacica"),
        (26213, "Crepaja"),
        (26214, "Debeljaca"),
        ]

    roads = [
        (11000, 21000, 93.7),  # Beograd - Novi Sad
        (11000, 26000, 21.6),  # Beograd - Pancevo
        (26201, 26000, 11.4),  # Pancevo - Jabuka
        (26201, 26204, 20.1),  # Jabuka - Opovo
        (26204, 21240, 31.2),  # Opovo - Titel
        (21241, 21240, 34),    # Titel - Kac
        (11000, 21240, 68.9),  # Beograd - Titel
        (21000, 21241, 13.3),  # Kac - Novi Sad
        ]

    def get_post_code(self, location_name):
        post_codes = [i for i, v in enumerate(self.locations) if v[1] == location_name];
        if len(post_codes) == 0:
            return -1
        return self.locations[post_codes[0]][0]

    def get_outbount_roads(self, post_code):

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