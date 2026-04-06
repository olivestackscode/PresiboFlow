from typing import Dict, Any
from presiboflow.agents.base_agent import BaseHealthcareAgent
from loguru import logger

class ClinicalAgent(BaseHealthcareAgent):
    def __init__(self):
        super().__init__(
            name="PresiboClinical",
            role="Clinical Analyst",
            prompt_path="presiboflow/prompts/clinical_prompt.txt"
        )

    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        transcript = state.get("transcript", "")
        preferences = state.get("preferences", {})
        logger.info(f"ClinicalAgent analyzing with preferences: {list(preferences.keys())}")
        
        system_msg = self.get_system_message(preferences)
        human_msg = HumanMessage(content=f"Current Transcript: {transcript}")
        
        # In a real run, we'd call the LLM:
        # response = await self.llm.ainvoke([system_msg, human_msg])
        # For the demo, we'll simulate based on preferences:
        
        clinical_data = state.get("clinical_insights", {"symptoms": [], "metrics": {}})
        
        # Apply "Intelligent Clay" logic
        if "high_bp_protocol" in preferences and "145/95" in transcript:
            clinical_data["protocol_applied"] = preferences["high_bp_protocol"]
            clinical_data["education_note"] = "Hypertension management: Low salt, regular exercise."

        if "headache" in transcript.lower():
            clinical_data["symptoms"].append("headache")
            
        return {"clinical_insights": clinical_data}
from langchain_core.messages import HumanMessage
