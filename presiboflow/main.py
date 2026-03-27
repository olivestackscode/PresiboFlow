import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from presiboflow.config.settings import settings

app = FastAPI(title="PresiboFlow Backend")

# Get the path to the frontend directory
# Get the path to the frontend directory
import sys
if getattr(sys, 'frozen', False):
    # If running as an EXE
    base_path = sys._MEIPASS
    frontend_dir = os.path.join(base_path, "presiboflow", "frontend")
else:
    # Standard development mode
    frontend_dir = os.path.join(os.getcwd(), "frontend")

# Mount static files
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

@app.get("/{page:path}")
async def get_page(page: str):
    page_path = os.path.join(frontend_dir, page)
    if os.path.exists(page_path) and os.path.isfile(page_path):
        return FileResponse(page_path)
    return FileResponse(os.path.join(frontend_dir, "index.html"))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
