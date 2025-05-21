"""Testing is a testing class."""
import typing

class Testing:
    name : typing.Optional[str] = 'Alice'
    age : typing.Optional[int] = 25
    isStudent : typing.Optional[bool] = False
    grades : typing.Optional[list] = [90, 85, 82]
    profile : typing.Optional[typing.Any] = None
    address : typing.Optional[dict] = {'city': 'Beijing', 'K': {}}
    pos : typing.Optional[typing.Any] = None
    z : typing.Optional[typing.Any] = None

    @classmethod
    def toJson(cls) -> dict:
        target = {}
        for key in cls.__annotations__.keys():
            target[key] = getattr(cls, key)
        return target

__all__ = ["Testing"]

print(Testing.toJson())