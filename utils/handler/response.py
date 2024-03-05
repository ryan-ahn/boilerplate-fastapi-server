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
