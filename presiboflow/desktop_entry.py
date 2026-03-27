import subprocess
import webbrowser
import time
import sys
import os
from pathlib import Path

def main():
    # Start backend (FastAPI + LiveKit worker)
    # Using 'python -m uvicorn' approach to ensure portability in the EXE
    print("Starting PresiboFlow backend...")
    
    # In a packaged EXE, sys.executable is the EXE itself
    # We need to make sure uvicorn is available or call it via multiprocess
    executable = sys.executable
    
    # Basic command to start the server
    backend_cmd = [
        executable, "-m", "uvicorn", "presiboflow.main:app", 
        "--host", "127.0.0.1", "--port", "8000", "--log-level", "info"
    ]
    
    backend = subprocess.Popen(
        backend_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
    )

    # Give backend time to start
    time.sleep(5)

    # Open browser to the entry interface
    url = "http://127.0.0.1:8000"
    print(f"Opening PresiboFlow in browser: {url}")
    webbrowser.open(url)

    print("\nPresiboFlow is running! Close this window to stop (or Ctrl+C).")
    try:
        # Keep the process alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        backend.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()
