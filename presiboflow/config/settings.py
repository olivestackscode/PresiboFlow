from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # LiveKit
    LIVEKIT_URL: str = ""
    LIVEKIT_API_KEY: str = ""
    LIVEKIT_API_SECRET: str = ""

    # LLM
    LLM_PROVIDER: str = "openai" # openai, ollama
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"
    OLLAMA_BASE_URL: str = "http://localhost:11434/v1"
    LLM_MODEL: str = "gpt-4o-mini"

    # Agent Settings
    AGENT_NAME: str = "PresiboClinicalAssistant"
    THRESHOLD_VAD: float = 0.5
    
    # Healthcare Context
    HOSPITAL_NAME: str = "Presibo General Hospital"
    DEFAULT_CURRENCY: str = "NGN"
    REDACT_PHI: bool = True

    # Tools
    GOOGLE_CALENDAR_ID: str = "primary"
    GOOGLE_DOCS_FOLDER_ID: Optional[str] = None

settings = Settings()
