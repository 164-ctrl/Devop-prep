from fastapi import APIRouter, HTTPException, status
from utils.executor import run_system_command

router = APIRouter(prefix="/system", tags=["System Metrics"])

@router.get("/uptime")
def get_uptime():
    try:
        output = run_system_command(["uptime"])
        return {"command": "uptime", "output": output}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )

@router.get("/disk")
def get_disk_space():
    try:
        output = run_system_command(["df", "-h"])
        return {"command": "df -h", "output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/memory")
def get_memory_usage():
    try:
        output = run_system_command(["free", "-m"])
        return {"command": "free -m", "output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user")
def get_current_user():
    try:
        output = run_system_command(["whoami"])
        return {"command": "whoami", "output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))