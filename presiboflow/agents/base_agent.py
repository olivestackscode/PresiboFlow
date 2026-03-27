from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage

class BaseHealthcareAgent(ABC):
    def __init__(self, name: str, role: str, prompt_path: str):
        self.name = name
        self.role = role
        self.prompt_path = prompt_path
        self.system_prompt = self._load_prompt()

    def _load_prompt(self) -> str:
        try:
            with open(self.prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"You are a helpful healthcare assistant named {self.name} acting as a {self.role}."

    @abstractmethod
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Process the current state and return updates."""
        pass
