from fastapi import FastAPI
from routes import system

app = FastAPI(
    title="Linux Command Executor API",
    description="A secure API to run selective system diagnostic commands",
    version="1.0.0"
)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "healthy"}

app.include_router(system.router)