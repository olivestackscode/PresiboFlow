try:
    from presiboflow.main import app
    print("Vercel entrypoint loaded successfully")
except Exception as e:
    import traceback
    from fastapi import FastAPI
    from fastapi.responses import PlainTextResponse
    
    app = FastAPI()
    error_msg = traceback.format_exc()
    print(f"ERROR: Failed to load app: {error_msg}")
    
    @app.get("/{path:path}")
    async def catch_all(path: str):
        import os
        debug_info = f"Initialization Error:\n\n{error_msg}\n\n"
        debug_info += f"CWD: {os.getcwd()}\n"
        debug_info += f"DIRNAME(__file__): {os.path.dirname(os.path.abspath(__file__))}\n"
        try:
            debug_info += f"Root Files: {os.listdir('.')}\n"
            debug_info += f"Parent Files: {os.listdir('..')}\n"
            if os.path.exists('/var/task'):
                debug_info += f"/var/task Files: {os.listdir('/var/task')}\n"
        except:
            pass
        return PlainTextResponse(debug_info, status_code=500)

# This file is used by Vercel as a Serverless Function entrypoint.
