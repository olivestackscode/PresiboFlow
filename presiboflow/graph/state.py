from typing import Annotated, TypedDict, List, Dict, Any
from langchain_core.messages import BaseMessage
import operator

class HealthcareState(TypedDict):
    """Shared state for the healthcare agentic system."""
    transcript: str
    history: Annotated[List[str], operator.add]
    detected_intents: List[str]
    clinical_insights: Dict[str, Any]
    actions: List[Dict[str, Any]]
    errors: List[str]
    hospital_name: str
    currency: str
