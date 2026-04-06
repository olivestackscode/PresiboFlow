from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage

from langchain_openai import ChatOpenAI
from presiboflow.config.settings import settings

class BaseHealthcareAgent(ABC):
    def __init__(self, name: str, role: str, prompt_path: str):
        self.name = name
        self.role = role
        self.prompt_path = prompt_path
        self.system_prompt = self._load_prompt()
        
        # Initialize LLM based on settings
        if settings.LLM_PROVIDER == "openai":
            self.llm = ChatOpenAI(
                api_key=settings.OPENAI_API_KEY,
                base_url=settings.OPENAI_BASE_URL,
                model=settings.LLM_MODEL
            )
        else:
            self.llm = ChatOpenAI(
                api_key="ollama",
                base_url=settings.OLLAMA_BASE_URL,
                model=settings.LLM_MODEL
            )

    def _load_prompt(self) -> str:
        try:
            with open(self.prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"You are a helpful healthcare assistant named {self.name} acting as a {self.role}."

    def get_system_message(self, preferences: Dict[str, Any]) -> SystemMessage:
        """Construct the system message with dynamic preferences."""
        clay_instructions = "\n\n### USER CUSTOMIZATIONS (INTELLIGENT CLAY)\n"
        if preferences:
            for key, val in preferences.items():
                clay_instructions += f"- {key}: {val}\n"
        else:
            clay_instructions += "- No specific customizations provided. Follow standard protocols.\n"
            
        full_prompt = self.system_prompt + clay_instructions
        return SystemMessage(content=full_prompt)

    @abstractmethod
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Process the current state and return updates."""
        pass
