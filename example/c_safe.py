import json, typing
from dataclasses import dataclass

@dataclass
class Testing:
    profile : typing.Any
    pos : typing.Any
    z : typing.Any
    name : typing.Optional[str] = 'Alice'
    age : typing.Optional[int] = 25
    isStudent : typing.Optional[bool] = False
    grades : typing.Optional[str] = ''

    def toJson(self) -> dict:
        target = {}
        for key, value in self.__dict__.items():
            target[key] = value
        return target

    @classmethod
    def fromJson(cls, fileName : str, encoding : str = "u8") -> "Testing":
        jsonData : dict = json.load(open(fileName, "r", encoding=encoding))
        return cls(
            name=jsonData.get("name"),
            age=jsonData.get("age"),
            isStudent=jsonData.get("isStudent"),
            grades=jsonData.get("grades"),
            profile=jsonData.get("profile"),
            pos=jsonData.get("pos"),
            z=jsonData.get("z"),
        )
