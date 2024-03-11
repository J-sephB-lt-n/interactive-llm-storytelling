from src.location import Location
from src.prompt_generator import PromptGenerator


class Location:
    """A physical location in the story"""
    def __init__(
        self, prompt_generator: PromptGenerator, prev_location: Location | None
    ) -> None:
        self.name = prompt_generator.generate_new_location_name(
            prev_location=prev_location
        )
        self.description = None
        self.contents: dict[str, Item] = {}
        self.adjacent_locations: dict[str, Location] = []
