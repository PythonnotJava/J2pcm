import typing
import json
from dataclasses import dataclass

@dataclass
class Testing:
    profile : typing.Any
    pos : typing.Any
    z : typing.Any
    name : str = 'Alice'
    age : int = 25
    isStudent : bool = False
    grades : str = ''

    def toJson(self) -> dict:
        return self.__dict__

    @classmethod
    def fromJson(cls, fileName : str, encoding : str = "u8") -> "Testing":
        jsonData : dict = json.load(open(fileName, "r", encoding=encoding))
        return cls(**jsonData)

