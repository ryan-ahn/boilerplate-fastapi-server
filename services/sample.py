from fastapi import HTTPException


async def fetch_data():
    return "데이터 있음"


async def get_sample_data():
    try:
        # service
        data = await fetch_data()
        # verify
        if data is None:
            raise Exception("F000001")
        # response
        return {
            "message": "S000001",
            "data": data,
        }
    except Exception as error:
        # error throw
        raise HTTPException(status_code=500, detail=str(error)) from error
