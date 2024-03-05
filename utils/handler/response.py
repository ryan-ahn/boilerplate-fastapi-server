from typing import Optional, Any
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


class SuccessResponse(BaseModel):
    status_code: int
    success: bool = Field(default=True, description="성공")
    message: str
    data: Optional[Any] = None


class ErrorResponse(BaseModel):
    status_code: int
    success: bool = Field(default=False, description="실패")
    message: str


def success_response(status_code: int, message: str, data: Any = None):
    response = SuccessResponse(status_code=status_code, message=message, data=data)
    return JSONResponse(status_code=status_code, content=response.dict())


def error_response(status_code: int, message: str):
    response = ErrorResponse(status_code=status_code, message=message)
    return JSONResponse(status_code=status_code, content=response.dict())


# 예시 사용법
# @app.get("/")
# async def read_root():
#     # 성공 응답 예시
#     return success_response(status.HTTP_200_OK, "성공 메시지", {"key": "value"})
#     # 실패 응답 예시
#     # return error_response(status.HTTP_400_BAD_REQUEST, "실패 메시지")
