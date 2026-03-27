from loguru import logger
from typing import List, Dict, Any
from presiboflow.graph.workflows import HealthcareWorkflow

class TranscriptProcessor:
    def __init__(self):
        self.workflow = HealthcareWorkflow()
        self.full_transcript: List[str] = []

    async def process_segment(self, text: str):
        """Process a segment of speech and trigger agentic workflows."""
        self.full_transcript.append(text)
        
        # Redact PHI if configured (placeholder)
        # processed_text = self._redact_phi(text)
        
        logger.info(f"Processing transcript segment: {text[:50]}...")
        
        # Pass to LangGraph workflow
        result = await self.workflow.run({"transcript": text, "history": self.full_transcript})
        
        # Handle results (e.g., send to frontend, log metrics)
        if result.get("actions"):
            for action in result["actions"]:
                logger.info(f"Detected Action: {action['type']} - {action['description']}")

    def _redact_phi(self, text: str) -> str:
        # Placeholder for PHI redaction logic
        return text
