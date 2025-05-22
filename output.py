import json

class RootAddressPos:
    @classmethod
    def from_dict(cls, *args) -> "RootAddressPos":
        return cls()

    @classmethod
    def fromJson(cls, *args) -> "RootAddressPos":
        return cls()

    def toJson(self, *args) -> dict:
        return {}

class RootAddress:
    def __init__(self, city: str, pos: RootAddressPos):
        self.city = city
        self.pos = pos

    @classmethod
    def from_dict(cls, data: dict) -> "RootAddress":
        return cls(
            city=data['city'],
            pos=RootAddressPos.from_dict(data['pos'])
        )

    @classmethod
    def fromJson(cls, filename: str, encoding: str = 'u8') -> "RootAddress":
        with open(filename, 'r', encoding=encoding) as f:
            data = json.load(f)
        return cls.from_dict(data)

    def toJson(self) -> dict:
        return {
            "city": self.city,
            "pos": self.pos.toJson(),
        }

class Root:
    def __init__(self, name: str, age: int, isStudent: bool, grades: list[int], scores: list[int], address: RootAddress, pos: Any, z: Any):
        self.name = name
        self.age = age
        self.isStudent = isStudent
        self.grades = grades
        self.scores = scores
        self.address = address
        self.pos = pos
        self.z = z

    @classmethod
    def from_dict(cls, data: dict) -> "Root":
        return cls(
            name=data['name'],
            age=data['age'],
            isStudent=data['isStudent'],
            grades=data['grades'],
            scores=data['scores'],
            address=RootAddress.from_dict(data['address']),
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
            "scores": self.scores,
            "address": self.address.toJson(),
            "pos": self.pos,
            "z": self.z,
        }
