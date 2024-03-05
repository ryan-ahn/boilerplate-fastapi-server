from fastapi import FastAPI
from routers.sample import router as sample_router

app = FastAPI()

# routers
app.include_router(sample_router)


# server state
@app.get("/")
async def root():
    return {"message": "Server clear!!"}
