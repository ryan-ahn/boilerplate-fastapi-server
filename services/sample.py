async def fetch_data():
    return "데이터"


async def get_sample_data():
    try:
        data = await fetch_data()
        if data is None:
            # 알려진 에러 상황
            raise ValueError("F000001")
        # 정상적인 응답 반환
        return {
            "message": "S000001",
            "data": data,
        }
    except ValueError as message:
        if str(message) == "F000001":
            raise message
        # 처리하지 못한 에러 케이스들
        raise ValueError("F000999") from message
    except Exception:
        raise ValueError("F000999") from message
