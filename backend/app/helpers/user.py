from app.helpers.utils import EnumValuesMixin


class UserType(str, EnumValuesMixin):
    NORMAL = 'normal'
    SUPER = 'super'
