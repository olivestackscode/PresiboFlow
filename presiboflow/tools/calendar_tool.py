from loguru import logger
from typing import Dict, Any

class CalendarTool:
    def __init__(self, calendar_id: str = "primary"):
        self.calendar_id = calendar_id

    async def create_appointment(self, details: Dict[str, Any]):
        """Create a Google Calendar appointment."""
        summary = details.get("summary", "Healthcare Appointment")
        start_time = details.get("start_time")
        logger.info(f"Creating appointment in {self.calendar_id}: {summary} at {start_time}")
        # Integration logic (Google Calendar API) would go here
        return {"status": "success", "event_id": "mock_event_123"}
