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
    # Robust path resolution for 'public' directory
    possible_roots = [
        os.getcwd(),                                      # Current working directory
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), # Project root relative to this file
        os.environ.get("VERCEL_PROJECT_ROOT", "/var/task") # Vercel specific
    ]
    
    frontend_dir = None
    for root in possible_roots:
        test_path = os.path.join(root, "public")
        if os.path.exists(test_path) and os.path.isdir(test_path):
            frontend_dir = test_path
            break
    
    if not frontend_dir:
        # Fallback to a temp directory with a real index.html file (not a directory)
        import tempfile
        temp_dir = tempfile.mkdtemp()
        dummy_index = os.path.join(temp_dir, "index.html")
        with open(dummy_index, "w") as f:
            f.write("<html><body><h1>PresiboFlow: Static assets not found.</h1></body></html>")
        frontend_dir = temp_dir
        print(f"WARNING: Static directory 'public' not found in {possible_roots}. Using temp dir.")

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
