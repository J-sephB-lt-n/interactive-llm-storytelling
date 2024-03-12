class PromptGenerator:
    def __init__(self) -> None:
        self.parts: dict[str, str] = {
            "global_init": "You are telling a story. ",
            "perspective": (
                "Please address me directly "
                "(i.e. second-person perspective) as I am "
                "the main character in the story. "
            ),
        }

    def set_global_story_style(self) -> None:
        self.parts["global_story_style"] = input(
            "Please describe the desired genre and "
            "style of the story "
            "(and add any other details/requirements you like) "
            "Examples: \n"
            "   The story is a horror story set in the dystopian future.\n"
            "   The story takes place in the mind of a man who is slowly going mad.\n"
            "   The story is a thriller set in rural Nigeria.\n"
            "   The story is science fiction with an industrial feel.\n"
        ).strip()
        if self.parts["global_story_style"][-1] != ".":
            self.parts["global_story_style"] += "."
        self.parts["global_story_style"] += " "

    def generate_location_names(self, n_locations: int) -> str:
        return (
            self.parts["global_init"]
            + self.parts["global_story_style"]
            + f"Please provide {n_locations} different physical "
            + "locations that would make sense appearing in this "
            + "story. Please do not describe them. "
            + f"Please number them 1 to {n_locations}"
        )