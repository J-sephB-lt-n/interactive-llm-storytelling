from abc import ABC, abstract_method


class Llm(ABC):
    @abstract_method
    def respond(self, prompt: str) -> str:
        """Respond to a prompt"""
        raise NotImplementedError
