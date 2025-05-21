import typing
import json
from typing import TypedDict

class Testing(TypedDict, total=False):
    name : typing.Optional[str]
    age : typing.Optional[int]
    isStudent : typing.Optional[bool]
    grades : typing.Optional[str]
    profile : typing.Optional[typing.Any]
    pos : typing.Optional[typing.Any]
    z : typing.Optional[typing.Any]

def fromJson(fileName : str, encoding : str = "u8") -> Testing:
    jsonData : dict = json.load(open(fileName, "r", encoding=encoding))
    return Testing(
        name=jsonData.get("name"),
        age=jsonData.get("age"),
        isStudent=jsonData.get("isStudent"),
        grades=jsonData.get("grades"),
        profile=jsonData.get("profile"),
        pos=jsonData.get("pos"),
        z=jsonData.get("z"),
    )

