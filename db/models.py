from sqlmodel import SQLModel, Field
from typing import Optional


class Deposit(SQLModel, table=True):
    __tablename__ = 'deposit'
    deposit_id: Optional[int] = Field(default=None, primary_key=True)
    date: str
    periods: int
    amount: int
    rate: float

