class Location:
    def __init__(self):
        self.name = None
        self.description = None
        self.contents: dict[str,Item] = {}
        self.adjacent_locations: dict[str, Location] = {}
