from typing import Dict, Any
from langgraph.graph import StateGraph, END
from presiboflow.graph.state import HealthcareState
from presiboflow.agents.triage_agent import TriageAgent
from presiboflow.agents.clinical_agent import ClinicalAgent
from presiboflow.agents.ops_agent import OpsAgent
from presiboflow.config.settings import settings

class HealthcareWorkflow:
    def __init__(self):
        self.triage = TriageAgent()
        self.clinical = ClinicalAgent()
        self.ops = OpsAgent()
        self.workflow = self._create_workflow()

    def _create_workflow(self):
        builder = StateGraph(HealthcareState)

        # Define nodes
        builder.add_node("triage", self.triage.process)
        builder.add_node("clinical", self.clinical.process)
        builder.add_node("ops", self.ops.process)

        # Set entry point
        builder.set_entry_point("triage")

        # Define edges
        # Simplified: Triage leads to Clinical and Ops
        builder.add_edge("triage", "clinical")
        builder.add_edge("clinical", "ops")
        builder.add_edge("ops", END)

        return builder.compile()

    async def run(self, input_data: Dict[str, Any]):
        initial_state = {
            "transcript": input_data.get("transcript", ""),
            "history": input_data.get("history", []),
            "detected_intents": [],
            "clinical_insights": {},
            "actions": [],
            "errors": [],
            "hospital_name": settings.HOSPITAL_NAME,
            "currency": settings.DEFAULT_CURRENCY
        }
        
        return await self.workflow.ainvoke(initial_state)
