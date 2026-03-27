from loguru import logger
from livekit.agents import JobContext
from livekit.agents.stt import SpeechEventType
from presiboflow.core.transcript_processor import TranscriptProcessor

class HealthcareVoicePipeline:
    def __init__(self, ctx: JobContext):
        self.ctx = ctx
        self.processor = TranscriptProcessor()

    async def start(self):
        logger.info("Healthcare Voice Pipeline started")
        
        @self.ctx.room.on("participant_connected")
        def on_participant_connected(participant):
            logger.info(f"Participant connected: {participant.identity}")

        # In a real scenario, we'd attach a STT engine here
        # For the scaffold, we simulate processing incoming transcripts
        # via the room's data channel or STT events.
        
        # Example of handling STT events (simplified)
        @self.ctx.room.on("speech_event")
        def on_speech_event(event):
            if event.type == SpeechEventType.FINAL_TRANSCRIPT:
                transcript = event.alternatives[0].text
                logger.info(f"New Transcript: {transcript}")
                asyncio.create_task(self.processor.process_segment(transcript))

    async def stop(self):
        logger.info("Healthcare Voice Pipeline stopping")
