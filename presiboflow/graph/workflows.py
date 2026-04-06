from typing import Dict, Any
from langgraph.graph import StateGraph, END
from presiboflow.graph.state import HealthcareState
from presiboflow.agents.triage_agent import TriageAgent
from presiboflow.agents.clinical_agent import ClinicalAgent
from presiboflow.agents.ops_agent import OpsAgent
from presiboflow.config.settings import settings

from presiboflow.agents.instruction_engine import InstructionEngine
import json
import os

class HealthcareWorkflow:
    def __init__(self):
        self.triage = TriageAgent()
        self.clinical = ClinicalAgent()
        self.ops = OpsAgent()
        self.molder = InstructionEngine()
        self.workflow = self._create_workflow()

    def _create_workflow(self):
        builder = StateGraph(HealthcareState)

        # Define nodes
        builder.add_node("molder", self.molder.process)
        builder.add_node("triage", self.triage.process)
        builder.add_node("clinical", self.clinical.process)
        builder.add_node("ops", self.ops.process)

        # Set entry point
        builder.set_entry_point("molder")

        # Define edges
        builder.add_edge("molder", "triage")
        builder.add_edge("triage", "clinical")
        builder.add_edge("clinical", "ops")
        builder.add_edge("ops", END)

        return builder.compile()

    def _load_persisted_prefs(self):
        if os.path.exists("preferences.json"):
            try:
                with open("preferences.json", "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    async def run(self, input_data: Dict[str, Any]):
        initial_state = {
            "transcript": input_data.get("transcript", ""),
            "history": input_data.get("history", []),
            "detected_intents": [],
            "clinical_insights": {},
            "actions": [],
            "errors": [],
            "hospital_name": settings.HOSPITAL_NAME,
            "currency": settings.DEFAULT_CURRENCY,
            "preferences": self._load_persisted_prefs(),
            "canvas_flow": input_data.get("canvas_flow", [])
        }
        
        return await self.workflow.ainvoke(initial_state)
