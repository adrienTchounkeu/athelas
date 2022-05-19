from enum import Enum


class EnumValuesMixin(Enum):
    @classmethod
    def values(cls):
        return [el.value for el in list(cls)]
