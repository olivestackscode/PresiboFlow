import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from presiboflow.config.settings import settings

app = FastAPI(title="PresiboFlow Backend")

# Get the path to the frontend directory
# Get the path to the frontend directory
import sys
import json
from presiboflow.graph.workflows import HealthcareWorkflow

# Robust path resolution for 'frontend' directory
if getattr(sys, 'frozen', False):
    # If running as an EXE
    base_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.getcwd()
    frontend_dir = os.path.join(base_path, "frontend")
else:
    # If running in development (e.g., python main.py)
    # The frontend is likely in the project root
    frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")

if not os.path.exists(frontend_dir):
    # Fallback/Error handling
    logger.error(f"Frontend directory not found at {frontend_dir}")
    os.makedirs(frontend_dir, exist_ok=True)
    with open(os.path.join(frontend_dir, "index.html"), "w") as f:
        f.write("<html><body><h1>PresiboFlow: Static assets not found.</h1></body></html>")

# Mount static files
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

workflow_engine = HealthcareWorkflow()

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": "0.2.0 (Clay)"}

@app.get("/api/preferences")
async def get_preferences():
    if os.path.exists("preferences.json"):
        with open("preferences.json", "r") as f:
            return json.load(f)
    return {}

@app.post("/api/preferences")
async def save_preferences(prefs: dict):
    with open("preferences.json", "w") as f:
        json.dump(prefs, f)
    return {"status": "success"}

@app.get("/api/canvas/flow")
async def get_canvas_flow():
    if os.path.exists("canvas_flow.json"):
        with open("canvas_flow.json", "r") as f:
            return json.load(f)
    return {"nodes": [], "edges": []}

@app.post("/api/canvas/flow")
async def save_canvas_flow(flow: dict):
    with open("canvas_flow.json", "w") as f:
        json.dump(flow, f)
    return {"status": "success"}

@app.post("/api/mold")
async def mold_flow(instruction: dict):
    # Process a natural language instruction to mold the flow
    text = instruction.get("text", "")
    # Run the workflow with just this instruction as transcript
    result = await workflow_engine.run({"transcript": text})
    return {"status": "success", "preferences": result.get("preferences")}

@app.get("/{page:path}")
async def get_page(page: str):
    page_path = os.path.join(frontend_dir, page)
    if os.path.exists(page_path) and os.path.isfile(page_path):
        return FileResponse(page_path)
    return FileResponse(os.path.join(frontend_dir, "index.html"))
