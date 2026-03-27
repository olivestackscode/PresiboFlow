from typing import Dict, Any
from presiboflow.agents.base_agent import BaseHealthcareAgent
from loguru import logger

class OpsAgent(BaseHealthcareAgent):
    def __init__(self):
        super().__init__(
            name="PresiboOps",
            role="Healthcare Operations Manager",
            prompt_path="presiboflow/prompts/ops_prompt.txt"
        )

    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        intents = state.get("detected_intents", [])
        logger.info(f"OpsAgent processing intents: {intents}")
        
        actions = []
        if "scheduling" in intents:
            actions.append({
                "type": "calendar",
                "description": "Book a follow-up appointment"
            })
        if "vital_signs" in intents:
            actions.append({
                "type": "metrics_log",
                "description": "Log vital signs to patient record"
            })
            
        return {"actions": actions}
