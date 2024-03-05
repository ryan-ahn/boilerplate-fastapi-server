from fastapi import APIRouter
from controllers.sample import router as sample_controller_router

router = APIRouter()

router.include_router(sample_controller_router, prefix="/sample", tags=["sample"])
