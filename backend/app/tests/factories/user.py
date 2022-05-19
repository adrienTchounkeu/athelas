import factory
from . import (
    ffactory,
    BaseFactory,
)

from app.models import User
from app.helpers import (
    UserType,
)


class UserFactory(BaseFactory):
    class Meta:
        model = User

    firstname = factory.LazyFunction(ffactory.name)
    lastname = factory.LazyFunction(ffactory.name)
    email = factory.LazyFunction(ffactory.free_email)
