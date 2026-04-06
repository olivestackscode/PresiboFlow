from typing import Dict, Any, List
import json
from langchain_core.messages import HumanMessage, SystemMessage
from presiboflow.agents.base_agent import BaseHealthcareAgent
from loguru import logger
import os

class InstructionEngine(BaseHealthcareAgent):
    def __init__(self):
        super().__init__(
            name="PresiboMolder",
            role="System Architect",
            prompt_path="presiboflow/prompts/molder_prompt.txt"
        )
        self.pref_file = "preferences.json"

    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        transcript = state.get("transcript", "")
        # Heuristic: only trigger if "From now on" or "molding" keywords are present
        trigger_keywords = ["from now on", "always", "never", "prefer", "instead of", "mold", "change the way"]
        
        if not any(kw in transcript.lower() for kw in trigger_keywords):
            return {"preferences": state.get("preferences", {})}

        logger.info(f"InstructionEngine detecting molding instructions in: {transcript[:50]}...")
        
        # In a real scenario, this would call the LLM to extract JSON rules.
        # For this "Clay" demo, we'll simulate the extraction or use a simple LLM call if configured.
        # For now, let's assume we update the preferences directly if we find a pattern.
        
        # Load existing prefs
        prefs = state.get("preferences", {})
        
        # Simulate LLM extraction for the demo requirements:
        if "bp is high" in transcript.lower() and "hypertension protocol" in transcript.lower():
            prefs["high_bp_protocol"] = "Include Nigerian hypertension protocol and generate patient education note."
        
        if "elderly" in transcript.lower() and "polite" in transcript.lower():
            prefs["tone_elderly"] = "Use extremely polite and respectful tone for elderly patients."
            
        if "malaria" in transcript.lower() and "track" in transcript.lower():
             prefs["malaria_workflow"] = "Track malaria test results and auto-suggest follow-up."

        # Save to local file for persistence
        with open(self.pref_file, "w") as f:
            json.dump(prefs, f)
            
        return {"preferences": prefs}
