from enum import Enum

class JobStatus(Enum):
    ACTIVE = "В акивном поиске"
    INACTIVE = "Не ищу работы"
    HIRED = "Уже занят"
    CHECKING = "Рассматриваю предложения"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class MaritalStatus(Enum):
    SINGLE = "Холост"
    MARRIED = "Женат/Замужем"
    NO_ANSWER = 'Не отвечать'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class Gender(Enum):
    MEN = "Мужчина"
    WOMAN = "Женщина"
    NO_ANSWER = "Не отвечать"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]
