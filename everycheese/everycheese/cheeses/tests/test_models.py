import pytest

# connects test to db
pytestmark = pytest.mark.django_db 

from ..models import Cheese
from .factories import CheeseFactory

def test___str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name