import pytest
from settings import Settings


@pytest.fixture
def envs(monkeypatch):
    monkeypatch.setenv("DB_USER", "test_user")
    monkeypatch.setenv("DB_PASSWORD", "test_pass")
    monkeypatch.setenv("DB_HOST", "test_host")
    monkeypatch.setenv("DB_PORT", "1234")
    monkeypatch.setenv("DB_NAME", "test_db")


def test_settings_instantiation(envs):
    settings = Settings()

    assert settings.DB_USER == "test_user"


def test_settings_db_uri(envs):
    settings = Settings()

    assert (
        settings.db_uri == "postgresql://test_user:test_pass@test_host:1234/test_db"
    )
