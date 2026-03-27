import asyncio
from loguru import logger
from livekit.agents import JobContext, WorkerOptions, cli, JobProcess
from presiboflow.core.pipeline import HealthcareVoicePipeline
from presiboflow.config.settings import settings

async def entrypoint(ctx: JobContext):
    logger.info(f"Starting healthcare voice worker for room: {ctx.room.name}")
    
    pipeline = HealthcareVoicePipeline(ctx)
    await pipeline.start()
    
    # Stay alive until the participant leaves or the job is cancelled
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        logger.info("Worker cancelled")
    finally:
        await pipeline.stop()
        logger.info("Worker stopped")

def main():
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))

if __name__ == "__main__":
    main()
