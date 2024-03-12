import json
import logging

import config
import src.llm
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
    locations = src.world_creation.generate_locations(
        n_locations=config.N_LOCATIONS, prompt_generator=prompt_generator, llm=llm
    )
    for x in locations:
        print(x)
    # first_prompt = prompt_generator.generate_location_name()
    # print(first_prompt)
    # raw_response = active_llm.respond(first_prompt)
    # print(raw_response)
    # cleaning_prompt = cleaning_prompt_generator.get_clean_location_name(raw_response)
    # print(cleaning_prompt)
    # clean_response = src.remove_punctuation(active_llm.respond(cleaning_prompt))
    # print(clean_response)
    # # print(prompt_generator.generate_location_description("hospital"))
    # # current_location = src.Location(prompt_generator)
