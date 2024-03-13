import logging
import math
import re
import sys
import time

from src.obj import Location
from src.llm import Llm
from src.prompting.prompt_generator import PromptGenerator
from src.string_cleaning import remove_punctuation

logger = logging.getLogger(__name__)


def generate_locations(
    n_locations: int, prompt_generator: PromptGenerator, llm: Llm
) -> list[Location]:
    raw_response: str = llm.respond(
        prompt_generator.generate_location_names(n_locations)
    )
    location_strings: list[str] = [
        remove_punctuation(x) for x in re.split(r"\d+", raw_response) if len(x) > 5
    ]

    locations: list[Location] = [Location(location_name) for location_name in location_strings]
    
    if len(locations) != n_locations:
        logger.warning(
            "Requested %s locations but parsed %s locations from LLM response",
            n_locations,
            len(locations),
        )

    return locations
