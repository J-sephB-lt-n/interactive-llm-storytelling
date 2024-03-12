import json
import logging

import src
import src.llm

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # initial game setup #
    prompt_generator = src.PromptGenerator()
    cleaning_prompt_generator = src.CleaningPromptGenerator()
    prompt_generator.set_global_story_style()
    active_llm = src.llm.OllamaLlm("mistral")
    logger.debug(json.dumps(prompt_generator.parts, indent=4))
    first_prompt = prompt_generator.generate_location_name()
    print(first_prompt)
    raw_response = active_llm.respond(first_prompt)
    print(raw_response)
    cleaning_prompt = cleaning_prompt_generator.get_clean_location_name(raw_response)
    print(cleaning_prompt)
    clean_response = src.remove_punctuation(active_llm.respond(cleaning_prompt))
    print(clean_response)
    # print(prompt_generator.generate_location_description("hospital"))
    # current_location = src.Location(prompt_generator)
