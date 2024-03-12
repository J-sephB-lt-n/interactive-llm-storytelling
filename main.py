import json
import logging

import src
import src.llm

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# if __name__ == "__main__":
#     # initial game setup #
#     prompt_generator = src.PromptGenerator()
#     prompt_generator.set_global_story_style()
#     logger.debug(json.dumps(prompt_generator.parts, indent=4))
#     current_location = src.Location(prompt_generator)
