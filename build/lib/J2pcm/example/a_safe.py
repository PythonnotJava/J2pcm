import typing
import json
class Testing:
    def __init__(self,
        name : typing.Optional[str], 
        age : typing.Optional[int], 
        isStudent : typing.Optional[bool], 
        grades : typing.Optional[list], 
        profile : typing.Optional[typing.Any], 
        address : typing.Optional[dict], 
        pos : typing.Optional[typing.Any], 
        z : typing.Optional[typing.Any]
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
        return self.__dict__

    @classmethod
    def fromJson(cls, fileName : str, encoding : str = "u8") -> "Testing":
        jsonData : dict = json.load(open(fileName, "r", encoding=encoding))
        return Testing(
            name=jsonData.get("name"),
            age=jsonData.get("age"),
            isStudent=jsonData.get("isStudent"),
            grades=jsonData.get("grades"),
            profile=jsonData.get("profile"),
            address=jsonData.get("address"),
            pos=jsonData.get("pos"),
            z=jsonData.get("z"),
        )

__all__ = ["Testing"]


print(Testing.fromJson('mutable_leak.json').toJson())