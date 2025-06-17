from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    """
    Endpoint to check if the server is running.
    """
    return {"message": "pong"}

@router.get("/health")
async def health():
    """
    Endpoint to check the health of the server.
    """
    return {"status": "Ok","uptime":"0s"}

@router.get("/sample-data")
async def sample_data():
    """
    Endpoint to return sample data.
    """
    return {
        "instances": [
            {"id": "i-012345", "state": "running"},
            {"id": "i-67890", "state": "stopped"}
        ]
    }