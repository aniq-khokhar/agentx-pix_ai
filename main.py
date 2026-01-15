import os
from google.adk.api_server import create_app
import uvicorn

# This helper automatically discovers agents in your directories
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)