from fastapi import APIRouter, status
from utils.handler.response import success_response, error_response
from services.sample import get_sample_data

router = APIRouter()


@router.get("/data")
async def sample_data():
    try:
        # service
        service_response = await get_sample_data()
        # handler
        return success_response(
            status.HTTP_200_OK, service_response["message"], service_response["data"]
        )
    except Exception as error:
        # handler
        return error_response(status.HTTP_400_BAD_REQUEST, str(error))
