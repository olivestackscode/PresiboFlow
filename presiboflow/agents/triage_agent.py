from typing import Dict, Any
from presiboflow.agents.base_agent import BaseHealthcareAgent
from loguru import logger

class TriageAgent(BaseHealthcareAgent):
    def __init__(self):
        super().__init__(
            name="PresiboTriage",
            role="Healthcare Triage Specialist",
            prompt_path="presiboflow/prompts/triage_prompt.txt"
        )

    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        transcript = state.get("transcript", "")
        logger.info(f"TriageAgent analyzing transcript: {transcript[:50]}...")
        
        # In a real implementation, call an LLM with self.system_prompt
        # For the scaffold, we return detected intents
        updates = {"detected_intents": []}
        if "appointment" in transcript.lower() or "schedule" in transcript.lower():
            updates["detected_intents"].append("scheduling")
        if "bp" in transcript.lower() or "blood pressure" in transcript.lower() or "glucose" in transcript.lower():
            updates["detected_intents"].append("vital_signs")
            
        return updates
