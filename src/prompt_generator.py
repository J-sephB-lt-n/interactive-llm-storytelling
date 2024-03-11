
from src.location import Location

class PromptGenerator:
    def __init__(self) -> None:
        self.parts: dict[str, str] = {
            "global_init": (
                "You are telling me a story. "
                "Please address me directly (second-person perspective) as I am the main character in the story. "
                )
        }

    def set_global_story_style(self) -> None:
        self.parts["global_story_style"] = input(
                "Please describe the desired genre and "
                "style of the story "
                "(and any other details you would like) "
                "Examples: \n"
                "   The story is a horror story set in the dystopian future.\n"
                "   The story is a romantic comedy / murder mystery.\n"
                "   The story is a thriller set in rural Nigeria.\n"
        ).strip()
        if self.parts["global_story_style"][-1] != ".":
            self.parts["global_story_style"] += "."
        self.parts["global_story_style"] += " "

    def generate_new_location_name(self, prev_location: Location) -> str:
        pass

        


     
