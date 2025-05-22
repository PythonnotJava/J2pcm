import typing
import json
from typing import TypedDict

class Testing(TypedDict, total=False):
    name : str
    age : int
    isStudent : bool
    grades : list
    profile : typing.Any
    address : dict
    pos : typing.Any
    z : typing.Any

def fromJson(fileName : str, encoding : str = "u8") -> Testing:
    jsonData : dict = json.load(open(fileName, "r", encoding=encoding))
    return Testing(**jsonData)

