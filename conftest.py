import pytest
from main import BooksCollector

# ссоздаем фикстуру collector
@pytest.fixture
def collector():
    return BooksCollector()