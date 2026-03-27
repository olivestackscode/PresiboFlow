import uvicorn
import webbrowser
import sys
import os
from presiboflow.main import app

def main():
    print("Starting PresiboFlow backend...")
    
    # Configuration
    host = "127.0.0.1"
    port = 8000
    url = f"http://{host}:{port}"
    
    print(f"PresiboFlow backend is ready at: {url}")
    print("Note: Automatic browser opening is disabled. Please open the URL manually.")
    
    # Run uvicorn directly in the main thread
    # This is more reliable for PyInstaller onefile bundles
    try:
        uvicorn.run(
            app, 
            host=host, 
            port=port, 
            log_level="info",
            access_log=True
        )
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
