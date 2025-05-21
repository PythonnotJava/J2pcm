import typing
import json
class Testing:
    def __init__(self,
        name : str, 
        age : int, 
        isStudent : bool, 
        grades : list, 
        profile : typing.Any, 
        address : dict, 
        pos : typing.Any, 
        z : typing.Any
    ):
        self.name = name
        self.age = age
        self.isStudent = isStudent
        self.grades = grades
        self.profile = profile
        self.address = address
        self.pos = pos
        self.z = z

    def toJson(self) -> dict:
        target = {}
        for key, value in self.__dict__.items():
            target[key] = value
        return target

    @classmethod
    def fromJson(cls, fileName : str, encoding : str = "u8") -> "Testing":
        jsonData : dict = json.load(open(fileName, "r", encoding=encoding))
        return cls(**jsonData)

__all__ = ["Testing"]
