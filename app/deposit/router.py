from fastapi import APIRouter

from app.deposit.models import DepositBase
from app.deposit.services import deposit_service

deposit_router = APIRouter()


@deposit_router.post("/calculation",
                     status_code=200,
                     responses={400: {'content': {'application/json': {'example': {'error': 'error message'}}}},
                                200: {'content': {'application/json': {'example': {'date': 'amount', 'date_x': 'amount_x'}}}}})
async def get_deposit_calculation(deposit: DepositBase) -> dict:
    """Калькуляция для депозита"""
    return deposit_service.calculate_deposit(deposit)
