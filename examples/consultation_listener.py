import asyncio
from loguru import logger
from presiboflow.core.transcript_processor import TranscriptProcessor

async def simulate_consultation():
    """
    Simulates a doctor-patient consultation transcript flow.
    Demonstrates how the agentic system reacts to voice segments.
    """
    processor = TranscriptProcessor()
    
    segments = [
        "Good morning, I'm here with Mr. Okon for his routine checkup.",
        "His current blood pressure is 145 over 95, a bit high.",
        "We should schedule a follow-up appointment in two weeks' time.",
        "Also, let's generate a referral letter for the cardiologist."
    ]
    
    logger.info("Starting Consultation Simulation...")
    
    for segment in segments:
        logger.info(f"🎤 [Doctor]: {segment}")
        await processor.process_segment(segment)
        await asyncio.sleep(1) # Simulate real-time delay

if __name__ == "__main__":
    asyncio.run(simulate_consultation())
