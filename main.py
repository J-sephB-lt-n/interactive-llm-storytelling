import json
import logging
import random

import config
import src.game_state
import src.llm
import src.obj
import src.prompting
import src.world_creation

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    prompt_generator = src.prompting.PromptGenerator()
    cleaning_prompt_generator = src.prompting.CleaningPromptGenerator()
    llm = src.llm.OllamaLlm("mistral")
    prompt_generator.set_global_story_style()
    logger.debug(json.dumps(prompt_generator.parts, indent=4))
    current_location: src.obj.Location = src.world_creation.generate_locations(
        n_locations=config.N_LOCATIONS, prompt_generator=prompt_generator, llm=llm
    )
    player_choice = "describe_current_location"
    while player_choice != "exit":
        player_choice = src.game_state.run_game_step(player_choice)
