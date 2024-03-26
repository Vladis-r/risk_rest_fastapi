import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.anyio


async def test_get_deposit_calculation(ac_client: AsyncClient):
    data = {
        "date": "31.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 6
    }
    resp = await ac_client.post('/deposit_calculation', json=data)
    assert resp.status_code == 200
    assert resp.json() == {"31.01.2021": 10050, "28.02.2021": 10100.25, "31.03.2021": 10150.75}


async def test_get_deposit_calculation_invalid_date(ac_client: AsyncClient):
    data = {
        "date": "99.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 6
    }
    resp = await ac_client.post('/deposit_calculation', json=data)
    assert resp.status_code == 400
    assert resp.json() == {'error': 'Invalid date format. Date must be in the format dd.mm.YYYY'}


async def test_get_deposit_calculation_invalid_periods(ac_client: AsyncClient):
    data = {
        "date": "31.01.2021",
        "periods": 0,
        "amount": 10000,
        "rate": 6
    }
    resp = await ac_client.post('/deposit_calculation', json=data)
    assert resp.status_code == 400
    assert resp.json() == {'error': 'Invalid number of months on deposit. Must be from 1 to 60.'}


async def test_get_deposit_calculation_invalid_amount(ac_client: AsyncClient):
    data = {
        "date": "31.01.2021",
        "periods": 3,
        "amount": 9999,
        "rate": 6
    }
    resp = await ac_client.post('/deposit_calculation', json=data)
    assert resp.status_code == 400
    assert resp.json() == {'error': 'Invalid deposit amount. Must be from 10,000 to 3,000,000.'}


async def test_get_deposit_calculation_invalid_rate(ac_client: AsyncClient):
    data = {
        "date": "31.01.2021",
        "periods": 3,
        "amount": 25000,
        "rate": 9
    }
    resp = await ac_client.post('/deposit_calculation', json=data)
    assert resp.status_code == 400
    assert resp.json() == {'error': 'Incorrect rate on deposit. Must be from 1 to 8.'}


