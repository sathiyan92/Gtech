"""
Single-entrypoint server runner for IoT Fleet Platform.
Can be executed from any folder or terminal.
"""
import os
import sys

# Ensure backend root is always in Python's import search path
project_root = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(project_root, "backend")

if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import uvicorn

if __name__ == "__main__":
    print("==================================================")
    print(">>> Starting IoT Fleet Platform Server...")
    print(f">>> Backend Directory: {backend_dir}")
    print(">>> Local Portal URL : http://localhost:8000/portal")
    print("==================================================")
    uvicorn.run(
        "src.main:app",
        app_dir=backend_dir,
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
