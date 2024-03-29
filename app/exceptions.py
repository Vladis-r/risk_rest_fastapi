from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from fastapi import Request


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> ORJSONResponse:
    """Меняем формат вывода ошибки валидации"""
    return ORJSONResponse({'error': str(exc)}, status_code=400)


def include_exc(app):
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
