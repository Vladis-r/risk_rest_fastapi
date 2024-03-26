import calendar

from db.models import DepositBase


class DepositService:
    def calculate_deposit(self, deposit: DepositBase) -> dict:
        """Расчёт депозита"""
        result = {}
        amount = deposit.amount
        date_map = self._get_dates(deposit)
        for period in range(int(deposit.periods)):
            amount = amount * (1 + deposit.rate / 12 / 100)
            result[date_map[period]] = round(amount, 2)
        return result

    def _get_dates(self, deposit: DepositBase) -> list[str]:
        """Получаем список с датой последнего дня каждого месяца в формате dd.mm.YYYY"""
        date_map = []
        date = deposit.date
        day, month, year = [int(i) for i in date.split('.')]
        for _ in range(deposit.periods):
            last_day = calendar.monthrange(year, month)[1]
            date_str = f"{last_day:02d}.{month:02d}.{year}"
            date_map.append(date_str)

            month += 1
            if month > 12:
                month = 1
                year += 1
        return date_map


deposit_service = DepositService()
