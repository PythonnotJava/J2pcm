import json
from typing import Any


class Root:
    def __init__(self, name: str, age: int, isStudent: bool, grades: str, profile: Any, pos: Any, z: Any):
        self.name = name
        self.age = age
        self.isStudent = isStudent
        self.grades = grades
        self.profile = profile
        self.pos = pos
        self.z = z

    @classmethod
    def from_dict(cls, data: dict) -> "Root":
        return cls(
            name=data['name'],
            age=data['age'],
            isStudent=data['isStudent'],
            grades=data['grades'],
            profile=data['profile'],
            pos=data['pos'],
            z=data['z']
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "Root":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "isStudent": self.isStudent,
            "grades": self.grades,
            "profile": self.profile,
            "pos": self.pos,
            "z": self.z,
        }
