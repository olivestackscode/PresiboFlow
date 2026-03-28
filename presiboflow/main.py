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
    frontend_dir = os.path.join(base_path, "presiboflow", "public")
else:
    # Get absolute path to the project root (one level up from presiboflow/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    frontend_dir = os.path.join(project_root, "public")

# Mount static files if directory exists, otherwise use a temporary directory
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")
else:
    import tempfile
    temp_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir, "index.html"), exist_ok=True) # Dummy
    app.mount("/static", StaticFiles(directory=temp_dir), name="static")
    print(f"WARNING: Static directory {frontend_dir} not found. Using temp dir.")

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
