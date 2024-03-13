import json
import logging

import config
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
    logger.info("Generating locations")
    prompt_generator.set_global_story_style()
    logger.debug(json.dumps(prompt_generator.parts, indent=4))
    locations: list[src.obj.Location] = src.world_creation.generate_locations(
        n_locations=config.N_LOCATIONS, prompt_generator=prompt_generator, llm=llm
    )
    for x in locations:
        print(x.name)
