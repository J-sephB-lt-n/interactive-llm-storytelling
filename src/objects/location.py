class Location:
    """A physical location in the story"""

    def __init__(self, prompt_generator, prev_location) -> None:
        self.name = prompt_generator.generate_new_location_name(
            prev_location=prev_location
        )
        self.description = prompt_generator.generate_location_description(self.name)
        self.contents = {}
        self.adjacent_locations = []