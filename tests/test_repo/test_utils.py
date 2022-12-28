from datetime import date
from repository.utils import last_compra_date


def test_last_compra_date(init_db, session):
    last_date = last_compra_date(1, session)

    assert last_date is not None
    assert isinstance(last_date, date)
    assert last_date == date(2022, 9, 1)
