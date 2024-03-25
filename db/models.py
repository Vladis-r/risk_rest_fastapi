from datetime import datetime
from typing import Optional

from fastapi.exceptions import RequestValidationError
from pydantic import field_validator
from sqlmodel import SQLModel, Field


class DepositBase(SQLModel):
    date: str = Field(..., description='Дата заявки')
    periods: int = Field(..., description='Количество месяцев по вкладу')
    amount: int = Field(..., description='Сумма вклада')
    rate: float = Field(..., description='Процент по вкладу')

    @field_validator("date")
    @classmethod
    def validate_date_format(cls, v: str) -> str:
        try:
            datetime.strptime(v, '%d.%m.%Y')
        except ValueError:
            raise RequestValidationError("Invalid date format. Date must be in the format dd.mm.YYYY")
        return v

    @field_validator("periods")
    @classmethod
    def validate_periods(cls, v: int) -> int:
        if not 1 <= v <= 60:
            raise RequestValidationError('Invalid number of months on deposit. Must be from 1 to 60.')
        return v

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, v: int) -> int:
        if not 10000 <= v <= 3000000:
            raise RequestValidationError('Invalid deposit amount. Must be from 10,000 to 3,000,000.')
        return v

    @field_validator("rate")
    @classmethod
    def validate_rate(cls, v: float) -> float:
        if not 1 <= v <= 8:
            raise RequestValidationError('Incorrect rate on deposit. Must be from 1 to 8.')
        return v


class Deposit(DepositBase, table=True):
    __tablename__ = 'deposit'
    deposit_id: Optional[int] = Field(default=None, primary_key=True)
