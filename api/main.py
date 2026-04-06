try:
    from presiboflow.main import app
except Exception as e:
    import traceback
    from fastapi import FastAPI
    from fastapi.responses import PlainTextResponse
    
    app = FastAPI()
    error_msg = traceback.format_exc()
    
    @app.get("/{path:path}")
    async def catch_all(path: str):
        return PlainTextResponse(f"Initialization Error:\n\n{error_msg}", status_code=500)

# This file is used by Vercel as a Serverless Function entrypoint.
