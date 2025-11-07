from fastapi import FastAPI
from clarifi_agent.api.endpoints import router as agent_router
from clarifi_agent.core.config import settings

app = FastAPI(title="Clarifi Agent API", version="1.0.0")

# Include routers
app.include_router(agent_router, prefix="/api/agent", tags=["agent"])

@app.get("/")
async def root():
    return {"message": "Clarifi Agent Service is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)